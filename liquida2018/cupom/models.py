import qrcode
from io import StringIO

from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from participante.models import DocumentoFiscal
from django.urls import reverse
from django_currentuser.db.models import CurrentUserField
from django.db import models
from django.urls import reverse
from django.core.files.uploadedfile import InMemoryUploadedFile


# Create your models here.
class Cupom(models.Model):
    numeroCupom = models.CharField(verbose_name=u'Número do Cupom', max_length=12, blank=False, null=False, unique=True)
    user =  models.ForeignKey(User, related_name='rel_cupom_participante',editable=False, on_delete=models.PROTECT)
    documentoFiscal = models.ForeignKey(DocumentoFiscal, related_name='rel_cupom_doc', null=False, blank=False, default=1, on_delete=models.PROTECT)
    operador = CurrentUserField(verbose_name=u'Cadastrado Por', related_name='rel_cupom_operador', editable=False)
    dataCriacao = models.DateTimeField(verbose_name=u'Cadastrado em', auto_now_add=True, editable=False)
    impresso = models.BooleanField(default=False)
    dataImpressao = models.DateTimeField()

    def __str__(self):
        return 'Cupom número: {}'.format(self.numeroCupom)

    qrcode = models.ImageField(upload_to='qrcode', blank=True, null=True)

    def get_absolute_url(self):
        return reverse('cupom:details', args=[str(self.numeroCupom)])

    def generate_qrcode(self):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=6,
            border=0,
        )
        qr.add_data(self.get_absolute_url())
        qr.make(fit=True)

        img = qr.make_image()

        buffer = io.StringIO.StringIO()
        img.save(buffer)
        filename = 'cupons-%s.png' % (self.id)
        filebuffer = InMemoryUploadedFile(
            buffer, None, filename, 'image/png', buffer.len, None)
        self.qrcode.save(filename, filebuffer)

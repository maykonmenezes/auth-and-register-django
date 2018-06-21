from cryptography.fernet import Fernet
from .models import Cupom
from django.contrib.auth.decorators import login_required, user_passes_test


class Crpto(object):

    def __init__(self):
        self.__masterkey = "b'jpvBrLzACz-NHI12Z5Yo7UTOC90fSLLM0Lp84SW_Pmw='"

    @property
    def tokenGen(self, code):
        f = Fernet(self.__masterkey)
        return f.encrypt(code)

from cupom.models import Cupom
from participante.models import DocumentoFiscal
from django.http import HttpResponse
from django.http import HttpResponseBadRequest
from django.urls import reverse
from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings

try:
    from cStringIO import StringIO
except ImportError:
    from io import BytesIO


def print_barcode_embed_example(request, code, barcode_type, template='embed_example.html'):
    """
    This is a test page showing how you can embed a request to print a barcode
    """
    bcp_url = reverse('bcp:print', kwargs = {'barcode_type': barcode_type, 'code': code,})
    context = { 'bcp_url': bcp_url, }
    return render(request, template, context)

def print_qrcode(request, code, numerodocumento, template='print.html'):
    """
    This page causes the browser to request the barcode be printed
    """
    pdf_url = reverse('bcp:generate', kwargs = {'numerodocumento': numerodocumento, 'code': code,})
    context = { 'pdf_url': pdf_url, }
    return render(request, template, context)

def print_barcode(request, code, barcode_type, template='print.html'):
    """
    This page causes the browser to request the barcode be printed
    """
    pdf_url = reverse('bcp:generate', kwargs = {'barcode_type': barcode_type, 'code': code,})
    context = { 'pdf_url': pdf_url, }
    return render(request, template, context)


def generate(request, code, numerodocumento,  barcode_type='Standard39', auto_print=True):
    """
     Returns a PDF Barcode using ReportLab
    """

    from reportlab.graphics.shapes import String, Drawing
    from reportlab.graphics import renderPDF
    from reportlab.graphics.barcode import qr
    from reportlab.pdfbase import pdfdoc
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename=%s.pdf' % (code,)

    # Config
    import bcp.settings as bcp_settings
    font_size = bcp_settings.FONT_SIZE
    bar_height = bcp_settings.BAR_HEIGHT
    bar_width = bcp_settings.BAR_WIDTH
    font_name = bcp_settings.FONT_NAME
    font_path = bcp_settings.FONT_PATH
    doc = get_object_or_404(DocumentoFiscal, numeroDocumento=numerodocumento)
    cupom = get_object_or_404(Cupom, documentoFiscal=doc)
        # If this is extended to different barcode types, then these options will need to be specified differently, eg not all formats support checksum.
    qr_code = qr.QrCodeWidget(code)

    bounds = qr_code.getBounds()
    width = bounds[2] - bounds[0]
    height = bounds[3] - bounds[1]
    x = width
    y = height
    c = Drawing(70, 70, transform=[30./width, 0, 0, 30./height, 0, 0])
    # Register the font
    pdfmetrics.registerFont(TTFont(font_name, font_path))

    # Set JS to Autoprint document
    if auto_print:
        pdfdoc.PDFCatalog.OpenAction = '<</S/JavaScript/JS(this.print\({bUI:true,bSilent:false,bShrinkToFit:true}\);)>>'
        pdfdoc.PDFInfo.title = code # nicety :)
    lineUp = String(105, 212, "_______________________________________________________", textAnchor='middle', fontSize=font_size)
    title = String(105, 196, "** LIQUIDA TERESINA 2018 **", textAnchor='middle', fontSize=12)
    lineTop = String(105, 190, "_______________________________________", textAnchor='middle', fontName=font_name, fontSize=font_size)
    lineTitle = String(105, 171, "_______________________________________", textAnchor='middle', fontName=font_name, fontSize=font_size)
    dadosParticipante = String(105, 177, "Dados do Participante", textAnchor='middle', fontSize=font_size)
    nome = String(30, 160, "Nome:", textAnchor='middle', fontSize=font_size)
    nomeParticipante = String(70, 160, '{}'.format(doc.user), textAnchor='middle', fontSize=font_size)
    cpf = String(27, 145, "CPF:", textAnchor='middle', fontSize=font_size)
    cidade = String(31, 130, "Cidade:", textAnchor='middle', fontSize=font_size)
    estado = String(150, 130, "Estado:", textAnchor='middle', fontSize=font_size)
    bairro = String(30, 115, "Bairro:", textAnchor='middle', fontSize=font_size)
    fone = String(147, 115, "Fone:", textAnchor='middle', fontSize=font_size)
    loja = String(48, 100, "Comprou na loja?", textAnchor='middle', fontSize=font_size)
    vendedor = String(155, 100, "Vendedor:", textAnchor='middle', fontSize=font_size)
    data = String(147, 70, "Data:", textAnchor='middle', fontSize=font_size)
    cupom = String(140, 50, "Cupom", textAnchor='middle', fontSize=15)
    lineBottom = String(105, 8, "_____________________________________________________", textAnchor='middle',  fontSize=font_size)
    c.add(lineUp)
    c.add(title)
    c.add(lineTop)
    c.add(dadosParticipante)
    c.add(lineTitle)
    c.add(nome)
    c.add(nomeParticipante)
    c.add(cpf)
    c.add(cidade)
    c.add(estado)
    c.add(bairro)
    c.add(fone)
    c.add(loja)
    c.add(vendedor)
    c.add(data)
    c.add(cupom)
    c.add(qr_code)
    c.add(lineBottom)
    buffer = BytesIO() # buffer for the output
    renderPDF.drawToFile(c, buffer, autoSize=1) # write PDF to buffer

    # Get the value of the StringIO buffer and write it to the response.
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)

    return response

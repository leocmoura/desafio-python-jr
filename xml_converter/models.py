from django.db import models

class ArquivoXML(models.Model):
    # nome = models.CharField(max_length=255)
    arquivo = models.FileField(upload_to='uploads/xml/')
    data_upload = models.DateTimeField(auto_now_add=True)
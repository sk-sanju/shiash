from django.db import models

class EncryptedFile(models.Model):
    file_name = models.CharField(max_length=255)
    encrypted_data = models.BinaryField()
    encryption_key = models.BinaryField()

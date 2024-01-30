from django.db import models

class EncryptedFile(models.Model):
    file = models.FileField(upload_to='encrypted_files/')

class FileFolder(models.Model):
    file_name = models.CharField(max_length=255)
    file_path = models.CharField(max_length=255)
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file_name
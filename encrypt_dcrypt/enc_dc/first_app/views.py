from django.shortcuts import render, redirect

from first_app.forms import EncryptedFile
from .forms import EncryptedFileForm
from cryptography.fernet import Fernet
from .models import EncryptedFile, FileFolder

def encrypt_file(file_content, key):
    cipher = Fernet(key)
    encrypted_data = cipher.encrypt(file_content)
    return encrypted_data

def decrypt_file(encrypted_data, key):
    cipher = Fernet(key)
    decrypted_data = cipher.decrypt(encrypted_data)
    return decrypted_data

def upload_file(request):
    if request.method == 'POST':
        form = EncryptedFileForm(request.POST, request.FILES)
        if form.is_valid():
            file_instance = form.save(commit=False)
            file_content = file_instance.file.read()

            # Use a secure key generation mechanism in a real-world scenario
            key = Fernet.generate_key()

            encrypted_data = encrypt_file(file_content, key)
            file_instance.file = encrypted_data
            file_instance.save()
            return redirect('file_list')
    else:
        form = EncryptedFileForm()
    return render(request, 'upload_file.html', {'form': form})

def file_list(request):
    files = EncryptedFile.objects.all()
    return render(request, 'file_list.html', {'files': files})

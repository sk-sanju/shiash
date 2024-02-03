from django.shortcuts import render, redirect
from .models import EncryptedFile
from .utils import decrypt_data, encrypt_data, generate_key

def home(request):
    files = EncryptedFile.objects.all()
    return render(request, 'home.html', {'files': files})

def upload_file(request):
    if request.method == 'POST':
        file = request.FILES['file']
        key = generate_key()
        encrypted_data = encrypt_data(file.read(), key)

        EncryptedFile.objects.create(
            file_name=file.name,
            encrypted_data=encrypted_data,
            encryption_key=key
        )

    return redirect('home')

def view_file(request, file_id):
    file = EncryptedFile.objects.get(pk=file_id)
    decrypted_data = decrypt_data(file.encrypted_data, file.encryption_key)
    return render(request, 'view_file.html', {'file': file, 'decrypted_data': decrypted_data})
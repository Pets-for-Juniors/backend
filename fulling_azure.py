from azure.storage.blob import BlobServiceClient
import os
from dotenv import load_dotenv

load_dotenv()

account_name = os.getenv('AZURE_ACCOUNT_NAME')
account_key = os.getenv('AZURE_ACCOUNT_KEY')

container_name = os.getenv('AZURE_CONTAINER')

# Инициализация клиента
blob_service_client = BlobServiceClient(account_url=f'https://{account_name}.blob.core.windows.net',
                                        credential=account_key)
container_client = blob_service_client.get_container_client(container_name)

# Путь к вашей локальной папке с медиа-файлами
media_folder = 'media'

# Загрузка файлов в Azure
for root, dirs, files in os.walk(media_folder):
    for file in files:
        file_path = os.path.join(root, file)
        blob_name = os.path.relpath(file_path, media_folder)
        blob_client = container_client.get_blob_client(blob_name)

        with open(file_path, "rb") as data:
            blob_client.upload_blob(data, content_type="image/jpeg")

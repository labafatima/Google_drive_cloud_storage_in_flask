from authentication import authenticate
from googleapiclient.http import MediaFileUpload

def upload_file(service, file_path, mime_type):
    """Upload a file to Google Drive."""
    file_metadata = {'name': file_path.split('/')[-1]}  # Extract the file name
    media = MediaFileUpload(file_path, mimetype=mime_type)
    uploaded_file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
    print(f"File uploaded successfully! File ID: {uploaded_file.get('id')}")
    return uploaded_file.get('id')

if __name__ == "__main__":
    # Step 1: Authenticate and initialize the service
    service = authenticate()

    # Step 2: Upload a file
    file_id = upload_file(service, 'testt.png', 'image/png')
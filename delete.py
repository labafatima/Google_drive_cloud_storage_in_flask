# from authentication import authenticate

# def get_file_id_by_name(service, file_name):
#     """
#     Get the file ID by searching for its name in Google Drive.
#     """
#     # Search for files with the given name
#     results = service.files().list(
#         q=f"name = '{file_name}'",
#         fields="files(id, name)",
#         spaces="drive"
#     ).execute()
#     files = results.get('files', [])
    
#     if not files:
#         print(f"No file found with the name: {file_name}")
#         return None
#     return files[0]['id']

# def delete_file_by_name(service, file_name):
#     """
#     Delete a file in Google Drive by its name.
#     """
#     file_id = get_file_id_by_name(service, file_name)
#     if file_id:
#         service.files().delete(fileId=file_id).execute()
#         print(f"File '{file_name}' deleted successfully!")
#     else:
#         print(f"Deletion failed. File '{file_name}' not found.")

# if __name__ == "__main__":
#     # Authenticate and initialize the service
#     service = authenticate()

#     # Delete a file by its name
#     delete_file_by_name(service, 'testt.png')
from authentication import authenticate

def delete_file_by_id(service, file_id):
    """
    Delete a file in Google Drive by its unique ID.
    """
    try:
        service.files().delete(fileId=file_id).execute()
        print(f"File with ID '{file_id}' deleted successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")
        print(f"Deletion failed. File with ID '{file_id}' not found or cannot be deleted.")

if __name__ == "__main__":
    # Authenticate and initialize the service
    service = authenticate()

    # Delete a file by its unique ID
    # Replace 'your_file_id_here' with the actual file ID
    delete_file_by_id(service, '1brfki-PPqOSg9bSVgCL9Bcmem1-BAF0Q')

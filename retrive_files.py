# from authentication import authenticate

# def list_files(service, page_size=10):
#     """List files in Google Drive."""
#     results = service.files().list(
#         pageSize=page_size,
#         fields="nextPageToken, files(id, name)"
#     ).execute()
#     items = results.get('files', [])
#     if not items:
#         print('No files found.')
#     else:
#         print('Files:')
#         for item in items:
#             print(f"{item['name']} ({item['id']})")
#     return items

# if __name__ == "__main__":
#     # Step 1: Authenticate and initialize the service
#     service = authenticate()

#     # Step 2: List files
#     list_files(service)

from authentication import authenticate

def list_files_with_links(service, page_size=10):
    """List files in Google Drive with direct links."""
    results = service.files().list(
        pageSize=page_size,
        fields="nextPageToken, files(id, name)"
    ).execute()
    items = results.get('files', [])
    if not items:
        print('No files found.')
    else:
        print('Files:')
        for item in items:
            file_id = item['id']
            file_name = item['name']
            file_link = f"https://drive.google.com/file/d/{file_id}/view"
            print(f"{file_name} ({file_id}) -\n Link: {file_link}")
    return items

if __name__ == "__main__":
    # Step 1: Authenticate and initialize the service
    service = authenticate()

    # Step 2: List files with links
    list_files_with_links(service)

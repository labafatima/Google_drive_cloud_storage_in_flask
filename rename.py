# from authentication import authenticate

# def rename_file(service, file_id, new_name):
#     """Rename a file in Google Drive."""
#     file_metadata = {'name': new_name}
#     updated_file = service.files().update(fileId=file_id, body=file_metadata, fields='id, name').execute()
#     print(f"File renamed successfully! New Name: {updated_file.get('name')}")
#     return updated_file

# if __name__ == "__main__":
#     # Step 1: Authenticate and initialize the service
#     service = authenticate()

#     # Step 4: Rename the uploaded file
#     rename_file(service, file_id, 'renamed_example.jpg')


from authentication import authenticate

def rename_file(service, file_id, new_name):
    """Rename a file in Google Drive."""
    file_metadata = {'name': new_name}
    updated_file = service.files().update(fileId=file_id, body=file_metadata, fields='id, name').execute()
    print(f"File renamed successfully! New Name: {updated_file.get('name')}")
    return updated_file

if __name__ == "__main__":
    # Step 1: Authenticate and initialize the service
    service = authenticate()

    # Step 2: Provide the file_id manually
    file_id = input("Enter the file ID to rename: ")
    new_name = input("Enter the new name for the file: ")

    # Step 3: Rename the file
    rename_file(service, file_id, new_name)

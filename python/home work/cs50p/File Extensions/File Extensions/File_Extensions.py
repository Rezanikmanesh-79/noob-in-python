def main():
    user_input=input("File name: ")
    print(File_name(user_input))
def File_name (user_i):
    if ".gif"in user_i:
        return "image/gif"
    elif ".jpg"in user_i:
        return "image/jpeg"
    elif ".jpeg"in user_i:
        return "image/jpeg"
    elif ".png"in user_i:
        return "image/png"
    elif ".pdf"in user_i:
        return "application/pdf"
    elif ".txt"in user_i:
        return "text/plain"
    elif ".zip"in user_i:
        return "application/zip"
    else:
        return "format is not valid"
        
        
main()

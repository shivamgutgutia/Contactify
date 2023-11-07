from flask import request

def headers():

    #Check if a file is uploaded
    if "file" not in request.files or not request.files["file"]:
        return("No file uploaded")

    return("Success")

    
from flask import request, jsonify
import pandas as pd

def headers():

    #Check if a file is uploaded
    if "file" not in request.files or not request.files["file"]:
        return("No file uploaded")

    file=request.files["file"]

    if (file.filename.endswith(".csv")):
        df = pd.read_csv(file)
    elif (file.filename.endswith(".xlsx")):
        df = pd.read_excel(file)
    else:
        return("Please send a valid file format")
    
    return(jsonify({"headers":list(df.columns)}))

    
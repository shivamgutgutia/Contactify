from flask import request
import pandas as pd
import json

def vcf():
    actualHeaders = []
    requiredHeaders = request.form["heads"].split(",")
    headersMap = request.form["headsmap"].split(",")

    file=request.files["file"]
    
    #Check if a file is uploaded
    if "file" not in request.files or not request.files["file"]:
        return("No file uploaded")

    file=request.files["file"]

    if (file.filename.endswith(".csv")):
        df = pd.read_csv(file)
    elif (file.filename.endswith(".xlsx") or file.filename.endswith(".xls")):
        df = pd.read_excel(file)
    else:
        return("Please send a valid file format")


    




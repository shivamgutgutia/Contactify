from flask import request
from utils.createDf import createDf
from utils.vcfGenerator import generateVcf

def vcf():
    actualHeaders = [
        "First Name",
        "Last Name", 
        "Middle Name", 
        "Prefix", 
        "Suffix", 
        "Phone Number",
        "E-Mail",
        "Gender",
    ]

    headersMap = dict(zip(
        request.form["heads"].split(","),
        request.form["headsmap"].split(",")
    ))

    validity=createDf(request.files)
    if not validity[0]:
        return(validity[1])
    else:
        df = validity[1]

    if request.form["removeWithoutNumber"]=="true" and "Phone Number" in headersMap:
        df = df[str(df[headersMap["Phone Number"]])!=""]

    #Less than 10 or not equal to 10 - must check
    if request.form["removeLessThan10"]=="true" and "Phone Number" in headersMap:
        df = df[len(str(df[headersMap["Phone Number"]]))!=10]

    if request.form["removeDuplicate"]=="true" and "Phone Number" in requiredHeaders:
        df = df.drop_duplicates(subset=headersMap["Phone Number"],keep="first")

    vcfString = generateVcf(df, headersMap, split=(request.form["split"]=="true"))   


    




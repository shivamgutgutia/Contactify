from flask import request, Response, make_response
from utils.createDf import createDf
from utils.vcfGenerator import generateVcf
import json


def vcf():
    '''actualHeaders = [
        "First Name",
        "Last Name", 
        "Middle Name", 
        "Prefix", 
        "Suffix", 
        "Phone Number",
        "E-Mail",
        "Gender",
    ]'''

    '''
    headersMap = dict(zip(
        request.form["heads"].split(","),
        request.form["headsMap"].split(",")
    )) 
    '''
    validity=createDf(request.files)
    if not validity[0]:
        return(validity[1],400)
    else:
        df = validity[1].astype(str)

    headersMap = json.loads(request.form["headersMap"])

    if "First Name" not in headersMap:
        return("The file must have atleast the first name field set",400)

    if request.form.get("removeWithoutNumber","")=="true" and "Phone Number" in headersMap:
        df = df[df[headersMap["Phone Number"]] != "nan"]

    #Less than 10 or not equal to 10 - must check
    if request.form.get("removeLessThan10","")=="true" and "Phone Number" in headersMap:
        df = df[df[headersMap["Phone Number"]].str.len()==10]

    if request.form.get("removeDuplicate","")=="true" and "Phone Number" in headersMap:
        df = df.drop_duplicates(subset=headersMap["Phone Number"],keep="first")


    if request.form.get("splitVCF","")=="false":
        vcfString = generateVcf(df, headersMap, split=(request.form.get("splitVCF","")=="true"))   
        response = Response(vcfString, content_type='text/vcard',headers={"Content-Disposition": "attachment; filename=contacts.vcf"})
        #response.headers['Content-Disposition'] = 'attachment; filename=contacts.vcf'
        return response,200
    else:
        vCardZip = generateVcf(df, headersMap, split=(request.form.get("splitVCF","")=="true"))
        response= make_response(vCardZip)
        response.headers["Content-Type"] = "application/zip"
        response.headers["Content-Disposition"] = "attachment; filename=Contacts.zip"
        return response
        


    




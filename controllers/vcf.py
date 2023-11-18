from flask import request, Response, jsonify
from utils.createDf import createDf
from utils.vcfGenerator import generateVcf
import json
import vobject


def vcf():
    '''actualHeaders = [
        "First Name",
        "Last Name", 
        "Middle Name", 
        "Prefix", 
        "Suffix", 
        "Phone Number",
        "E-Mail",,
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
        columns = headersMap["Phone Number"].split(",") if headersMap["Phone Number"] else []
        if columns:
            mask = df[columns].apply(lambda x: all(x == ""), axis=1)
            df = df[~mask]

    #Less than 10 or not equal to 10 - must check
    if request.form.get("removeLessThan10","")=="true" and "Phone Number" in headersMap:
        columns = headersMap["Phone Number"].split(",") if headersMap["Phone Number"] else []
        for column in columns:
            df[column]=df[column].apply(lambda x: x if len(x)>=10 else "")

    if request.form.get("removeDuplicate","")=="true" and "Phone Number" in headersMap:
        columns = headersMap["Phone Number"].split(",") if headersMap["Phone Number"] else []
        df = df.drop_duplicates(subset=columns,keep="first") if columns else df

    if request.form.get("sample","")=="false":
        if request.form.get("splitVCF","")=="false":
            vcfString = generateVcf(df, headersMap, split=(request.form.get("splitVCF","")=="true"))   
            response = Response(vcfString, content_type='text/vcard',headers={"Content-Disposition": "attachment; filename=contacts.vcf"})
            #response.headers['Content-Disposition'] = 'attachment; filename=contacts.vcf'
            return response,200
        else:
            vCardZip = generateVcf(df, headersMap, split=(request.form.get("splitVCF","")=="true"))
            response = Response(vCardZip, content_type='application/zip',headers={"Content-Disposition": "attachment; filename=Contacts.zip"})
            return response,200
        
    else:
        vcfString = generateVcf(df.iloc[[0]].copy(),headersMap,split=False)
        vcard = vobject.readOne(vcfString)

        jcard = jsonify({
            "Name": vcard.fn.value if hasattr(vcard, 'fn') else "",
            "Phone Number(s)": "/".join([tel.value for tel in vcard.tel_list]) if hasattr(vcard, 'tel') else "",
            "E-Mail": "/".join([email.value for email in vcard.email_list]) if hasattr(vcard, 'email') else ""
        })
        return jcard
        



    

        


    




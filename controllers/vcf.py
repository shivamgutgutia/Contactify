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
        request.form["headsMap"].split(",")
    ))

    if "First Name" not in headersMap:
        return("The file must have atleast the first name field set")

    validity=createDf(request.files)
    if not validity[0]:
        return(validity[1])
    else:
        df = validity[1]

    df= df.astype(str)

    if request.form["removeWithoutNumber"]=="true" and "Phone Number" in headersMap:
        df = df[df[headersMap["Phone Number"]] != "nan"]

    #Less than 10 or not equal to 10 - must check
    if request.form["removeLessThan10"]=="true" and "Phone Number" in headersMap:
        df = df[df[headersMap["Phone Number"]].str.len()==10]

    if request.form["removeDuplicate"]=="true" and "Phone Number" in headersMap:
        df = df.drop_duplicates(subset=headersMap["Phone Number"],keep="first")

    vcfString = generateVcf(df, headersMap, split=(request.form["splitVCF"]=="true"))   
    return(vcfString)


    




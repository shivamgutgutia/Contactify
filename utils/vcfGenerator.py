import vobject
import zipfile
import io
#import random
from flask import request
def generateVcard(row, headers, vCards):
    vcard = vobject.vCard()

    fnParameters = [row.get(headers.get(string,""),"") for string in ["First Name","Middle Name","Last Name"]]
    prefix = [request.form.get("Prefix")] if "Prefix" in request.form else []
    suffix = [request.form.get("Suffix")] if "Suffix" in request.form else []
    fnParameters=prefix+fnParameters+suffix
    fn = " ".join(filter(None,fnParameters))
    if fn:
        vcard.add("fn").value = fn
    else:
        vcard.add("fn").value = "N/A"

    vcard.add("n").value = vobject.vcard.Name(
        family=row.get(headers.get("Last Name",""),""),
        given=row.get(headers.get("First Name",""),""),
        additional=row.get(headers.get("Middle Name",""),""),
        suffix=request.form.get("Suffix","")+" "+str(row.name+1) if request.form.get("autoIncrement","") == "true" else request.form.get("Prefix",""),
        prefix=request.form.get("Prefix","")
    )

    fields=headers.get("Phone Number","")
    fields = fields.split(",") if fields else []
    for field in fields:
        phone = row.get(field,"")
        if phone:
            telephone = vcard.add("tel")
            telephone.type_param = ["HOME"]
            telephone.value = phone

    fields=headers.get("E-Mail","")
    fields = fields.split(",") if fields else []
    for field in fields:
        email = row.get(field,"")
        if email:
            mail = vcard.add("email")
            mail.type_param = ["HOME"]
            mail.value = email
    
    vcard.add('version').value = '4.0'
    vCards.append(vcard)

def generateVcf(df, headers,split):
    vCards=[]
    df.apply(lambda row: generateVcard(row,headers,vCards),axis=1)
    if not split:
        vCards = [vCard.serialize() for vCard in vCards]
        vcardString = "\n".join(vCards)
        return vcardString
    else:
        zipMemoryFile = io.BytesIO()
        with zipfile.ZipFile(zipMemoryFile,"w") as zipFile:
            for vCard in vCards:
                textFile = io.StringIO(vCard.serialize())
                zipFile.writestr(f"{vCard.fn.value} contact.vcf",textFile.getvalue())

        zipMemoryFile.seek(0)
        return zipMemoryFile.getvalue()



import vobject
import zipfile
import io
#import random
from flask import request
def generateVcard(row, headers, vCards):
    vcard = vobject.vCard()

    fn = (row.get(headers.get("prefix","Not Found"),"") + " " +row.get(headers.get("First Name","Not Found"),"")+" "+row.get(headers.get("Middle Name","Not Found"),"")+" "+\
        row.get(headers.get("Last Name","Not Found"),"")+" "+row.get(headers.get("suffix","Not Found"),"")).strip()
    if fn:
        vcard.add("fn").value = fn
    else:
        vcard.add("fn").value = "N"

    vcard.add("n").value = vobject.vcard.Name(
        family=row.get(headers.get("Last Name","Not Found"),""),
        given=row.get(headers.get("First Name","Not Found"),""),
        additional=row.get(headers.get("Middle Name","Not Found"),""),
        suffix=request.form.get("suffix",""),
        prefix=request.form.get("prefix","")
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
    print(df.columns)
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



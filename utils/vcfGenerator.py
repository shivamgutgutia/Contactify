import vobject

def generateVcard(first,middle,last,prefix,phone,vcards):
    vcard = vobject.vCard()
    vcard.add("fn").value = first+" "+middle+" "+last
    vcard.add("n").value = vobject.vcard.Name(
        family=last,
        given=first,
        additional=middle,
        suffix="CC Junior"
    )
    telephone = vcard.add("tel")
    telephone.type_param = ["HOME"]
    telephone.value = phone
    vcard.add('version').value = '4.0'
    vcards.append(vcard.serialize())

def generateVcf(df, headers,split):
    vCards=[]
    df.apply(lambda row: generateVcard(row["First"],row["Middle"],row["Last"],str(row["Phone"]),vCards),axis=1)
    vcardString = "\n".join(vCards)
    return vcardString

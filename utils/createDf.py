from pandas import read_csv, read_excel

def createDf(requestFiles):
    if "file" not in requestFiles or not requestFiles["file"]:
        return False,"No file uploaded"
    file=requestFiles["file"]

    if (file.filename.endswith(".csv")):
        df = read_csv(file,dtype=str)
    elif (file.filename.endswith(".xlsx") or file.filename.endswith(".xls")):
        df = read_excel(file,dtype=str)
    elif (file.filename.endswith(".ods")):
        df = read_excel(file,engine="odf",dtype=str)
    else:
        return False,"Please upload valid file format"

    df = df.applymap(lambda x: x.strip() if isinstance(x,str) else "")
    df = df.loc[~(df == "").all(axis=1)]

    if not len(df):
        return False,"Empty file uploaded"
    return True,df

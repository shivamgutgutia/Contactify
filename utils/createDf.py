import pandas as pd

def createDf(requestFiles):
    if "file" not in requestFiles or not requestFiles["file"]:
        return False,"No file uploaded"
    file=requestFiles["file"]

    if not((file.filename.endswith(".csv")) or (file.filename.endswith(".xlsx") or file.filename.endswith(".xls"))):
        return False,"Please upload valid file format"
    
    if (file.filename.endswith(".csv")):
        df = pd.read_csv(file)
    elif (file.filename.endswith(".xlsx") or file.filename.endswith(".xls")):
        df = pd.read_excel(file)
    return True,df

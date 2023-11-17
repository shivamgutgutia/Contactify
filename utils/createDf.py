#import pandas as pd
from pandas import read_csv, read_excel

def createDf(requestFiles):
    if "file" not in requestFiles or not requestFiles["file"]:
        return False,"No file uploaded"
    file=requestFiles["file"]

    if not((file.filename.endswith(".csv")) or (file.filename.endswith(".xlsx") or file.filename.endswith(".xls"))):
        return False,"Please upload valid file format"
    
    if (file.filename.endswith(".csv")):
        df = read_csv(file,dtype=str)
    elif (file.filename.endswith(".xlsx") or file.filename.endswith(".xls")):
        df = read_excel(file,dtype=str)

    if not len(df):
        return False,"Empty file uploaded"
    return True,df

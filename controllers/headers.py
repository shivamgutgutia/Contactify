from flask import request, jsonify
from utils.createDf import createDf

def headers():

    validity=createDf(request.files)
    if not validity[0]:
        return(validity[1],400)
    else:
        df = validity[1]

    return(jsonify({"headers":list(df.columns)}),200)

    
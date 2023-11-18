from flask import Flask, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os
from routers import router
load_dotenv()

app= Flask(__name__)
CORS(app)
app.config['MAX_CONTENT_LENGTH'] = 1024*1024*1024

@app.errorhandler(Exception)
def errorHandler(error):
    return jsonify({"error":error}),500

app.register_blueprint(router)


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=os.getenv("PORT",5000))

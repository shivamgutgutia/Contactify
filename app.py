from flask import Flask, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os
from routers import router
import traceback
load_dotenv()

app= Flask(__name__)
CORS(app, resources={r"/*": {"origins": "https://contactify.codechefvit.com"}, "methods": ["GET", "POST"],})
app.config['MAX_CONTENT_LENGTH'] = 1024*1024*1024

@app.errorhandler(Exception)
def errorHandler(error):
    response = jsonify({'error': 'Server Error', 'message': str(error)})
    response.status_code = 500
    app.logger.error('Server Error: %s', error)
    app.logger.error(traceback.format_exc())  # Log the traceback
    return response

app.register_blueprint(router)


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=os.getenv("PORT",5000))

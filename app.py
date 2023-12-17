from flask import Flask, jsonify, request
from flask_cors import CORS
from dotenv import load_dotenv
import os
from routers import router
import traceback
load_dotenv()


app= Flask(__name__)
#CORS(app)
CORS(app, resources={r"/*": {"origins": "https://contactify.codechefvit.com", "methods": ["GET", "POST"]}})
app.config['MAX_CONTENT_LENGTH'] = 1024*1024*1024

# def check_origin():
#     if "Origin" not in request.headers or request.headers["Origin"] != "https://contactify.codechefvit.com":
#         return False
#     return True

# @app.before_request
# def before_request():
#     # Check if the request origin is allowed
#     if request.method != 'OPTIONS' and not check_origin():
#         return jsonify({"error": "Forbidden"}), 403

app.register_blueprint(router)

# @app.errorhandler(Exception)
# def errorHandler(error):
#     response = jsonify({'error': 'Server Error', 'message': str(error)})
#     response.status_code = 500
#     app.logger.error('Server Error: %s', error)
#     app.logger.error(traceback.format_exc())  # Log the traceback
#     return response


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=os.getenv("PORT",5000))

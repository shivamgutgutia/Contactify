from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
import os
from routers import router
load_dotenv()

app= Flask(__name__)
CORS(app)
app.config['MAX_CONTENT_LENGTH'] = 1024*1024*1024

app.register_blueprint(router)

if __name__ == "__main__":
    app.run(port=os.getenv("PORT",5000))

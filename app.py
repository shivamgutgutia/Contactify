from flask import Flask
from dotenv import load_dotenv
import os
from routers import router
load_dotenv()

app= Flask(__name__)

app.register_blueprint(router)

if __name__ == "__main__":
    app.run(port=os.getenv("PORT",5000))

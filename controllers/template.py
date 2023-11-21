from flask import send_file
import os

baseDir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

filePath = os.path.join(baseDir, 'files', 'templates.zip')

def template():
    return send_file(
        filePath,
        mimetype="application/zip",
        as_attachment=True,
        download_name="Template Files.zip"
    ),200
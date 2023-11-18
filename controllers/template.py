from flask import send_file

def template():
    return send_file(
        r".\utils\templates.zip",
        mimetype="application/zip",
        as_attachment=True,
        download_name="Template Files.zip"
    )
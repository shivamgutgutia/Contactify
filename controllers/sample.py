from flask import send_file

def sample():
    return send_file(
        r".\utils\samples.zip",
        mimetype="application/zip",
        as_attachment=True,
        download_name="Sample Files.zip"
    )
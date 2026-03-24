import subprocess
from io import BytesIO

from flask import Flask, send_file
from PIL import Image

app = Flask(__name__)


@app.route("/image/show")
def show_image():
    filename = "src/poppet_holder.tif"
    image = Image.open(filename)
    try:
        image.load()
        buf = BytesIO()
        image.save(buf, format="PNG")
        buf.seek(0)
        return send_file(buf, mimetype="image/png")
    except Exception as e:
        return "error"


@app.route("/tiff_version")
def tiff_version():
    command = "tiffinfo -h"
    try:
        result = subprocess.run(
            command,
            capture_output=True,
            check=True,
            shell=True,
            text=True,
        )
        return result.stdout.split("\n")[0]
    except subprocess.CalledProcessError as e:
        return "unknown version"


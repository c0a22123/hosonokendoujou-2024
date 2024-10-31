from flask import Flask, render_template, request, redirect, url_for, session, send_file, jsonify
import qrcode
import io
from .database import *
from .bingodatabase import *

def generate_qr(url):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    return img

@app.route('/generate_qr/<int:cell_id>')
def generate_qr_code(cell_id):
    url = str(cell_id)
    img = generate_qr(url)

    img_io = io.BytesIO()
    img.save(img_io, 'PNG')
    img_io.seek(0)
    return send_file(img_io, mimetype='image/png')
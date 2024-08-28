import os
from qrcode_utils import generate_qr

# QRコードを保存するディレクトリを作成
if not os.path.exists('static/qrcodes'):
    os.makedirs('static/qrcodes')

# 9つのQRコードを生成
for i in range(9):
    data = f'QR-{i+1}'
    file_name = f'static/qrcodes/qr_{i+1}.png'
    generate_qr(data, file_name)
    print(f"Generated QR code for {data} at {file_name}")

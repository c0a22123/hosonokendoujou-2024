import qrcode # type: ignore
from PIL import Image # type: ignore
import cv2 # type: ignore

def generate_qr(data, file_name):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img.save(file_name)

def read_qr(image_path):
    img = cv2.imread(image_path)
    detector = cv2.QRCodeDetector()
    data, bbox, _ = detector.detectAndDecode(img)
    if bbox is not None:
        print(f"QR Code data: {data}")
    return data

def read_qr_from_camera():
    cap = cv2.VideoCapture(0)
    detector = cv2.QRCodeDetector()
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        data, bbox, _ = detector.detectAndDecode(frame)
        if bbox is not None:
            print(f"QR Code data: {data}")
            for i in range(len(bbox)):
                cv2.line(frame, tuple(bbox[i][0]), tuple(bbox[(i+1) % len(bbox)][0]), color=(255, 0, 0), thickness=2)
            cv2.putText(frame, data, (int(bbox[0][0][0]), int(bbox[0][0][1]) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
            cap.release()
            cv2.destroyAllWindows()
            return data
        cv2.imshow("QR Code Scanner", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
    return None

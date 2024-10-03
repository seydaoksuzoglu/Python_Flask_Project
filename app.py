# Gerekli kütüphaneleri import edelim
from flask import Flask, render_template
import cv2
from ultralytics import YOLO

# Flask uygulamasını başlat
app = Flask(__name__, template_folder='apps-20241002T205536Z-001/apps/templates', static_folder='static-20241002T210124Z-001/static')

# YOLO modelini yükle
model = YOLO('best.pt')

# Resim işleme fonksiyonu
def process_images():
    image_1_path = "images-20241002T205543Z-001/images/akhand_b43_325_jpg.rf.583eea641ed8fb6893d946b671c2348b.jpg"
    image_1 = cv2.imread(image_1_path)

    # Car-Damage işlemleri
    results_1 = model(image_1)
    car_damage_class = 0
    filtered_boxes_1 = [box for box in results_1[0].boxes if int(box.cls[0]) == car_damage_class]
    for box in filtered_boxes_1:
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        score = box.conf[0]
        cv2.rectangle(image_1, (x1,y1), (x2,y2), (0,215,255), 4)
        cv2.putText(image_1, f'Car-Damage: {score:.2f}', (x1+10, y1+30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,215,255), 2)

    cv2.imwrite('static-20241002T210124Z-001/static/image_1.jpg', image_1)

    image_2_path = "images-20241002T205543Z-001/images/akhand_b43_345_jpg.rf.21fb0de29feb94e89adfb699801ab1d8.jpg"
    image_2 = cv2.imread(image_2_path)

    # Dent işlemleri
    results_2 = model(image_2)
    dent_class = 1
    filtered_boxes_2 = [box for box in results_2[0].boxes if int(box.cls[0]) == dent_class]
    for box in filtered_boxes_2:
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        score = box.conf[0]
        cv2.rectangle(image_2, (x1,y1), (x2,y2), (240,32,160), 4)
        cv2.putText(image_2, f'Dent: {score:.2f}', (x1+10, y1+30), cv2.FONT_HERSHEY_SIMPLEX, 1, (240,32,160), 2)

    cv2.imwrite('static-20241002T210124Z-001/static/image_2.jpg', image_2)

@app.route('/')
def home():
    process_images()
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # GitHub veya yerel sunucu için ayar
    
      

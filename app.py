# Gerekli kütüphaneleri import edelim
from flask import Flask, render_template
import cv2

# Flask uygulamasını başlat
app = Flask(__name__, template_folder='apps-20241002T205536Z-001/apps/templates', static_folder='static-20241002T210124Z-001/static')

# Resim işleme fonksiyonu
def process_images():

    cv2.imwrite('static-20241002T210124Z-001/static/image_1.jpg', image_1)


    cv2.imwrite('static-20241002T210124Z-001/static/image_2.jpg', image_2)

@app.route('/')
def home():
    process_images()
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # GitHub veya yerel sunucu için ayar
    
      

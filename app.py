from flask import Flask, render_template, request
from PIL import Image
from datetime import datetime
from werkzeug.utils import secure_filename

import qrcode
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/qrcodes'

current_year = datetime.now().year


    # TODO: paginas de error / renderizado errores
    # TODO: Guardar la imagen igual en Linux, Mac y Windows



def save_image(image, filename):
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))



@app.route('/')
def index():
    return render_template('index.html', current_year=current_year)



@app.route('/generate', methods=['POST', 'GET'])
def generate():
    if request.method == 'POST':
            
        data = request.form.get('url')

        # Genero el código QR
        qr = qrcode.QRCode(version=1, box_size=7, border=1)
        qr.add_data(data)
        qr.make(fit=True)

        # Genero la imagen
        image = qr.make_image(fill="black", back_color="white")

        # Construyo el nombre del archivo según el datetime actual
        current_timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        source = current_timestamp + ".png"

        # Guardo la imagen
        # path = 'static/qrcodes/' + source
        save_image(image, source)
        

        # Muestro la imagen (puede que no sea necesario)
        # Image.open(path).show()

        path = 'qrcodes/' + source

        return render_template('confirmacion.html', path=path, current_year=current_year) 
    
    else:
        return render_template('index.html', current_year=current_year)



if __name__ == '__main__':
    app.run()

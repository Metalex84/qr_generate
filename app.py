from flask import Flask, render_template, request
import qrcode
import datetime
from PIL import Image
from datetime import datetime

app = Flask(__name__)

current_year = datetime.now().year

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

        path = 'static/qrcodes/' + source
        # TODO: Configurar guardado de imagen para que sea igual en Linux, Windows y Mac
        # image.save(path)

        # TODO: Cuando eso esté listo, podré mostrar la imagen
        # Image.open(path).show()

        path = 'qrcodes/' + source

        return render_template('confirmacion.html', path=path, current_year=current_year) 
    
    else:
        return render_template('index.html', current_year=current_year)



if __name__ == '__main__':
    app.run()

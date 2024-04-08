from flask import Flask, render_template, request
import qrcode
import datetime
from PIL import Image
from datetime import datetime

app = Flask(__name__)
current_year = datetime.now().year


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', curent_year=current_year)
    # TODO: conseguir que el año se visualice en la pagina index, además de en confirmacion


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
            
        data = request.form.get('url')
        # Generating the QR code
        qr = qrcode.QRCode(version=1, box_size=7, border=1)
        qr.add_data(data)
        qr.make(fit=True)

        # Creating the image itself
        image = qr.make_image(fill="black", back_color="white")

        # Building the filename
        current_timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        path = current_timestamp + ".png"

        # Saving the image
        image.save(path)

        # Display the image
        Image.open(path).show()

        return render_template('confirmacion.html', path=path, current_year=current_year) 
        # TODO: ¿qué le pasa a la ruta de la imagen? ¿Por qué no la coge?
    
    else:
        return render_template('login.html', current_year=current_year)


if __name__ == '__main__':
    app.run()

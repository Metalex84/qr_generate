import qrcode
import datetime
from PIL import Image

# Fetching data from the user, avoiding empty input
while True:
    data = input("Please enter an URL: ")
    if len(data) != 0:
        break

# Generating the QR code
qr = qrcode.QRCode(version=1, box_size=7, border=1)
qr.add_data(data)
qr.make(fit=True)

# Creating the image itself
image = qr.make_image(fill="black", back_color="white")

# Building the filename
current_timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
filename = current_timestamp + ".png"

# Saving the image
image.save(filename)

# Display the image
Image.open(filename).show()
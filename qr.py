import qrcode
#from PIL import Image

# The data you want to encode in the QR code
data = "https://github.com/Metalex84"

# Generate the QR code
qr = qrcode.QRCode(version=1, box_size=7, border=1)
qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR code
image = qr.make_image(fill="black", back_color="white")

# Save the image
image.save("myqrcode.png")
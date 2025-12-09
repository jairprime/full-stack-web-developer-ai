import qrcode

# Generate QR code for the given link

link = "https://intelligent-assistance-system-production.up.railway.app/"
img = qrcode.make(link)
img.save("ias.png")
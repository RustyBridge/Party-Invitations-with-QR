from PIL import Image
import glob
import os


os.chdir("C:/GitHub Repositories/Experiments/Party Invitations with QR")
data_folder = os.path.join("QRS", "QR_1_100")
listing = glob.glob(os.path.join(data_folder, '*.png'))

counter = 0
for filename in listing:
    print(filename)
    counter+=1
    template = Image.open(r'C:/GitHub Repositories/Experiments/Party Invitations with QR/Template/Invitation.png')
    qr = Image.open(os.path.join("", filename)).convert("RGBA")
    x, y = qr.size
    newsize = (260, 260)
    qr1 = qr.resize(newsize)

    Image.Image.paste(template, qr1, (100, 650,))

    template.save("C:/GitHub Repositories/Experiments/Party Invitations with QR/Invitations/{}.png".format(counter), format="png")
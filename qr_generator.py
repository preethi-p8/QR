# #####open an image and read a qr code#####
# #generate

import qrcode
from PIL import Image
import numpy as np

qr = qrcode.QRCode(version=1,
                    error_correction=qrcode.constants.ERROR_CORRECT_H,
                    box_size=10,
                    border=4)

qr.add_data("https://forms.gle/3p1yyR2vzwYxjfnx8")
qr.make(fit=True)

print("\n")
print('Shape of QR Image :', np.array(qr.get_matrix()).shape)

img = qr.make_image(fill_color="white",
                    back_color="black").convert('RGB')

img.save("test.png")

logo_disp = Image.open('D:\OptiSol\Flask\QR\happy_html.jpg')
logo_disp.thumbnail((60,60))

logo_pos = ((img.size[0] - logo_disp.size[0]) // 2, (img.size[1] - logo_disp.size[1]) // 2)
img.paste(logo_disp, logo_pos)

img.save("test2.png")

# #read

import cv2

def read_qr_code(filename):
    try:
        img = cv2.imread(filename)
        d = cv2.QRCodeDetector()
        value, points, straight = d.detectAndDecode(img)
        
        if points is not None:
            return value

    except:
        print('There is some error in execution!')
        return


print(read_qr_code("form.jpg"))   #function call

# # ***********************

# # read a directory of images and extract the qr code values

import glob
import pathlib
import pandas as pd

df = pd.DataFrame(columns=['filename','qr'])
files_dir = glob.glob('dir_qr/*.png')

for file1 in files_dir:

    qr = read_qr_code(file1)
    row = {'filename': file1, 'qr' : qr}

    df = df.append(row, ignore_index=True)

print(df.head())
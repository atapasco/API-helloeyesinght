import pytesseract as tess
from PIL import Image
import cv2
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

#my_image = Image.open('D:\\PROGRAMMING\\3-Python\\My_Virtual_Envs\\ocr_youtube\\routing.PNG')

def textRecognition():
    my_image = cv2.imread('imagenAPI.jpeg')
    my_image = cv2.cvtColor(my_image, cv2.COLOR_BGR2GRAY)
    #my_image = cv2.convertScaleAbs(my_image, alpha=1.2, beta=0)
    #_, my_image = cv2.threshold(my_image, int(0.6 * 255), 245, cv2.THRESH_BINARY)
    cv2.imwrite('./imagen.jpeg',my_image)
    txt = tess.image_to_string(my_image, lang='spa')
    json = {"text": str(txt)}
    return json
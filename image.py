import cv2 
import pytesseract 
import requests
import shutil
import pyttsx3
engine = pyttsx3.init()

#image_url = "https://www.wirefly.com/sites/wirefly.com/files/styles/guide_landing/public/search-for-text-on-webpage-on-iphone_0.jpg?itok=2EQmvPp9"
#filename = image_url.split("/")[-1]
#r = requests.get(image_url, stream = True)
#if r.status_code == 200: 
#	r.raw.decode_content = True
#	with open(filename,'wb') as f:
#		shutil.copyfileobj(r.raw, f)
#	print("Image successfuly downloaded: ", filename)
#else:
#	print("Failed")


pytesseract.pytesseract.tesseract_cmd  = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

img = cv2.imread("j.jpeg")

text = pytesseract.image_to_string(img)
print(text)
engine.say(text)
engine.runAndWait()

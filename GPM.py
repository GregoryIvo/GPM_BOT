#Gregory Ivo
#bot the uses OCR to play a elementry school level math game
#https://www.mathplayground.com/ASB_GrandPrixMultiplication.html
#to set up, please fill in the cordenates of the 2 boxes
#eqnLocation = main equation
#box1 = box hilighting all the numbers

#code needs to be cleaned

import pyautogui #this lets us control mouse and keyboard

from PIL import ImageGrab
import os
import time
from PIL import Image
import pytesseract

#Main game loop
def play_round():
    eqnLocation = (317,431,574,466)
    box1 = (269, 486 , 507 , 507)
    ImageGrab.grab().crop(eqnLocation).save("screen_capture.png", "PNG")
    eqn = pytesseract.image_to_string(Image.open("screen_capture.png"), config='-psm 6').strip().lower().split(' ')[0]
    print(eqn)
    answer = int(eqn.split('x')[0]) * int (eqn.split('x')[1])
    print("The Calculated is: " + str(answer))
    #time.sleep(5)
    
    
    ImageGrab.grab().crop(box1).save("screen_capture.png", "PNG")
    key = pytesseract.image_to_string(Image.open("screen_capture.png"), config='-psm 6 -c tessedit_char_whitelist=0123456789|').strip()
    print(key)
    keys = key.split('|')
    for i in range (0, 4):
            number = int(keys[i])
            if (number == answer):
                #print("Answer is key: " + str(i+1))
                pyautogui.typewrite(str(i+1))

pyautogui.alert('Close This to Pwn')
while(True):
    try:
        play_round()
    except:
        print("cant detect game!")
    

print("___________________________")

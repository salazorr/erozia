import telebot
import time
import pyautogui

#Bot_Token = "7954587598:AAHj_Xuk3-mwMfbnrOnVs19LuUV-BXX3xJc"
Chat_ID = "461387325"
#Chat_ID = "357885725"
Screen_Area = (300, 200, 400, 300)
White = 230
Check = 1

bot = telebot.TeleBot("7954587598:AAHj_Xuk3-mwMfbnrOnVs19LuUV-BXX3xJc")

def skolko_pixel(image):
    white_pixel = 0
    for pixel in image.getdata():
        if sum(pixel) / 3 > White:
            white_pixel += 1
    return white_pixel

def main():
    while True:
        screenshot = pyautogui.screenshot(region=Screen_Area)
        white_pixel = skolko_pixel(screenshot)

        if white_pixel > 1000:
            if white_pixel > 50000:
                bot.send_message(Chat_ID, "Ошибка")
            else:
                bot.send_message(Chat_ID, "Окончание")

        time.sleep(Check)

if __name__ == "__main__":
    main()
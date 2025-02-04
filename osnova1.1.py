import telebot
import time
import pyautogui

#Bot_Token = "7954587598:AAHj_Xuk3-mwMfbnrOnVs19LuUV-BXX3xJc"
Chat_ID = "461387325"
Screen_Area = (300, 200, 400, 300)
White = 230
Check = 3

bot = telebot.TeleBot("7954587598:AAHj_Xuk3-mwMfbnrOnVs19LuUV-BXX3xJc")

state = None

def skolko_pixel(image):
    white_pixel = 0
    for pixel in image.getdata():
        if sum(pixel) / 3 > White:
            white_pixel += 1
    return white_pixel

def main():
    global state

    while True:
        screenshot = pyautogui.screenshot(region=Screen_Area)
        white_pixel = skolko_pixel(screenshot)

        if white_pixel > 1000:
            if white_pixel > 50000:
                new_state = "Ошибка"
            else:
                new_state = "Окончание"
        else:
            new_state = "Окна нет"

        if new_state !=state:
            if new_state == "Ошибка":
                bot.send_message(Chat_ID, "Ошибка")
            elif new_state == "Окончание":
                bot.send_message(Chat_ID, "Окончание")
            elif new_state == "Окна нет":
                bot.send_message(Chat_ID, "Окна нет")

            state = new_state

        time.sleep(Check)

if __name__ == "__main__":
    main()
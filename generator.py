import random
import tkinter as tk
import logging
import os
import datetime
import os

print("starting application")

log_directory = 'logs'
if not os.path.exists(log_directory):
    os.makedirs(log_directory)
date = datetime.datetime.now().strftime('%Y-%m-%d')
time = datetime.datetime.now().strftime('%H-%M-%S')
log_file_name = f'{log_directory}/Debug_{date}_{time}.log'
logging.basicConfig(filename=log_file_name, level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')



# Функция для генерации ключей
def generate_keys_OEM():  # Функция генерации ключей OEM
    numberday = random.randint(100, 366)
    logging.info("Number A Generated : " + str(numberday))

    numberyear = random.randint(10, 95)
    logging.info("Number B Generated : " + str(numberyear))

    numberdou7 = random.randint(100000, 999999)
    logging.info("Number C Generated : " + str(numberdou7))
    logging.info("Checkin is number ...")

    while sum(map(int, str(numberdou7))) % 7 != 0:
        logging.warning("Number invalid.")
        numberdou7 = random.randint(100000, 999999)

    logging.info("Number c Generated :" + str(numberdou7))
    randomnumber = random.randint(10000, 99999)
    logging.info("Number d Generated :  " + str(randomnumber))

    key_str = str(numberday) + str(numberyear) + "-OEM-0" + str(numberdou7) + "-" + str(randomnumber)
    print("Generated key windows 95 " + str(numberday) + str(numberyear) + "-OEM-0" + str(numberdou7) + "-" + str(
        randomnumber))
    logging.info("Answered in window")
    logging.info("Generated OEM key : " + str(numberday) + str(numberyear) + "-OEM-0" + str(numberdou7) + "-" + str(
        randomnumber))
    key_label.config(text=key_str)

def generation_key_notoem():
    num = random.randint(100, 999)
    logging.info("Generated 1num : " + str(num))
    num2 = random.randint(100000, 999999)
    logging.info("Number num2 Generated : " + str(num2))
    logging.info("Checkin is number ...")

    while sum(map(int, str(num2))) % 7 != 0:
        logging.warning("Number invalid.")
        num2 = random.randint(100000, 999999)

    key_notoem = str(num) + "-" + str(num2)
    print("Generated office 95 " + str(num) + "-" + str(num2))
    logging.info("Answered in window")
    logging.info("Generated Office 95 key : " + str(num) + "-" + str(num2))
    key_label.config(text=key_notoem)


# Функция для выхода из приложения
def exit_app():  # Функция exit_app
    root.destroy()
    logging.info("Application is quit")


def version_app():  # Функция version_app
    key_str = "Версия приложения 1.1"
    logging.info("Click button 'version'")
    logging.info("Version application 1.1")
    key_label.config(text=key_str)


root = tk.Tk()
logging.info("Created window")
root.title("Generator Keys")
root.configure(bg="pink")
root.iconbitmap("icon.ico")

key_label = tk.Label(root, text="Нажмите 'Генерировать ключи'", font=("Arial", 12))
logging.info("Created text Click to the generated key")
key_label.pack(padx=20, pady=20)

key_description = tk.Label(root, text="Правильные ключи сохраняются в консоль", font=("bolt", 10))
logging.info("Created text Click to the generated key")
key_description.pack(padx=20, pady=20)

generate_button = tk.Button(root, text="Генерировать ключи", command=generate_keys_OEM)
logging.info("Click to the generated OEM key")
generate_button.pack(pady=10)

version_button = tk.Button(root, text="Сгенерировать Office 95 ключ", command=generation_key_notoem)
logging.info("Click to the generated Office 95 key")
version_button.pack(pady=10)

exit_button = tk.Button(root, text="Выход", command=exit_app)
logging.info("Click to the quit button")
exit_button.pack(pady=10)

version_button = tk.Button(root, text="Версия", command=version_app)
logging.info("Click to the version button")
version_button.pack(pady=10)

root.mainloop()

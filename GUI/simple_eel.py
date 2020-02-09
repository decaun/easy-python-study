import eel
import os

eel.init('front_end')


@eel.expose
def say_hello_py():
    os.system("gnome-terminal")
    print('Hello !!!')


eel.start('index.html')

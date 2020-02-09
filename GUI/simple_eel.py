import eel


eel.init('front_end')


@eel.expose
def say_hello_py():
    print('Hello !!!')


eel.start('index.html')

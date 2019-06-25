import eel


eel.init('web')
eel.start('index.html', block=False)

while True:
    eel.sleep(10)

import plyer
from plyer import notification
import time

print("HI,Welcome TO  DRinking water remainder !!")
while True:
    time.sleep(3600)
    notification.notify(
    title = 'Drinking Water Remainder',
    message = 'Hi,Buddy its time to have a glass of Water \nand a short Break',
    app_icon = 'icon.ico',
    timeout = 20,)
    
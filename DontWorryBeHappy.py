from socket import timeout 
import time 
from plyer import notification 

while(True):
    notification.notify(
        title = "You Are Good, I Am Proud Of You",
        message = "Remember To Eat & Drink Water ❤️",
        app_icon = '',
        timeout = 20
    )
    time.sleep(60*60*1)
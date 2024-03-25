from plyer import notification
#notif pyhton lib that incorporated the notif feature...
import time #time used for notif duration

def send_notification(title, message): #notif fucntio.
    notification.notify(
        title=title,
        message=message,
        timeout=10  # Notification will disappear after 10 seconds
    )

#in action
if __name__ == "__main__":

    #notif sent 
    #Title and message of notif 
    send_notification("Have You Played Today?", "Dont forget to play a round of Snake Hunt!")

    # Simulate a delay
    time.sleep(5)

    
from plyer import notification

def send_notification(title, message):
    notification.notify(
        title=title,
        message=message,
        app_icon="icon.ico"
    )

send_notification("This is Title", "This is Description")
import subprocess

def notify_send(title, text, urgency="normal"):
    subprocess.Popen(["notify-send", str(title), str(text), "-u", urgency])

import threading

class Messenger(threading.Thread):
    def run(self):
        for _ in range(10):
            print(threading.current_thread().getName())

send = Messenger(name="Sending out messages")
receive = Messenger(name="Receiving Messages")

send.start()
receive.start()
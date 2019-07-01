import socket
from datetime import datetime
import tkinter as tk

UDP_PORT = 10006
MESSAGE = "CTCTime:F:2019.04.30-23:27:00.00:Manual"
sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP

class Application:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("ChronoSync") 
          
        self.txt_ip = tk.Entry(self.window,
                          justify = tk.CENTER,
                          width = 25, font = ("Oswald", 15))

        self.txt_ip.insert(tk.END, "172.20.23.98")

        button_fileData = tk.Button(self.window, fg="red",
                                    text = 'SYNC',
                                    font = ("Oswald", 15),
                                    width=25, height=1,
                                    borderwidth = 3,
                                    command = self.send)
        self.txt_ip.grid()
        button_fileData.grid()
        self.window.mainloop()

    def send(self):
        UDP_IP = self.txt_ip.get()
        now = datetime.now()
        dt_string = now.strftime("%Y.%m.%d-%H:%M:%S.%f")[:-4]
        MESSAGE = "CTCTime:F:{}:Manual".format(dt_string)
        sock.sendto(MESSAGE.encode('utf-8'), (UDP_IP, UDP_PORT))
        print(MESSAGE)
        print(UDP_IP)

apl = Application()

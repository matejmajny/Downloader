#import and functions

import tkinter as tk
import requests, os, sys
from colorama import *
init()

def button():
    x1 = entry2.get()
    x2 = entry1.get()
    
    if x1 != "":
        os.chdir(x1)

    root.destroy()
    download(x2)
    print(Fore.GREEN + "\n Succesful!")
    print(Fore.RED + "\n\n")
    input("Press enter to exit...")

def clearConsole():
    os.system("cls" if os.name == "nt" else "clear")

def filename(url):
    return url.split("/")[-1]

def download(link):
    file_name = filename(link)
    print(Fore.YELLOW + "")
    with open(file_name, "wb") as f:
        print("Downloading " + file_name)
        response = requests.get(link, stream=True)
        total_length = response.headers.get('content-length')

        if total_length is None: # no content length header
            f.write(response.content)
        else:
            dl = 0
            total_length = int(total_length)
            for data in response.iter_content(chunk_size=4096):
                dl += len(data)
                f.write(data)
                done = int(50 * dl / total_length)
                sys.stdout.write("\r[%s%s]" % ('=' * done, ' ' * (50-done)) )    
                sys.stdout.flush()

root = tk.Tk()
root.title("DownloaderGUI v1.0")
canvas1 = tk.Canvas(root, width=350, height=250)
canvas1.pack()

#entries

entry1 = tk.Entry(root)
canvas1.create_window(250, 140, window=entry1)

entry2 = tk.Entry(root)
canvas1.create_window(250, 115, window=entry2)

#labels

label1 = tk.Label(root, text="Enter location or keep empty: ")
canvas1.create_window(100, 115, window=label1)

label2 = tk.Label(root, text='Enter URL: ')
canvas1.create_window(150, 140, window=label2)

label3 = tk.Label(root, text="DownloaderGUI")
label3.config(font=("helvetica", 15))
canvas1.create_window(160, 80, window=label3)

#buttons

button1 = tk.Button(text="Download! ", bg="green", fg="white", command=button)
canvas1.create_window(170, 200, window=button1)

root.mainloop()
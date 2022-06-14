#import and functions

import requests, os, sys
from colorama import *
init()

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

#program itself

while True:
    print(Fore.CYAN + "")
    clearConsole()
    link = input("Enter link to that what you want download: ")
    location = input("Do you want enter custom location? If yes write it here, if no hit ENTER: ")

    match location:

        case "":
            print("")
        case _:
            print("")
            os.chdir(location)

    download(link)
    print(Fore.GREEN + "Succesful!")
    print(Fore.RED + "\n")
    another = input("Do you want to download another file? Y/N ").lower()

    match another: 
        case "n":
            break
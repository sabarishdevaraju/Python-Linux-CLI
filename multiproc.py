import multiprocessing
import os
import subprocess


def downloadFile(url, output):
    print(f"Process {output}, PID: {os.getpid()}")
    subprocess.run(["wget", "-O", output, url], stderr=subprocess.DEVNULL, check=True)
    
    # os.system(f'wget -O {output} {url} > /dev/null')

if __name__ == "__main__":
    try:
        while True:
            multiprocessing.Process(target=downloadFile, args=(input('Enter URL to download: '), input("Output Name: "))).start()
    except KeyboardInterrupt as e:
        print("Quitting...")

from time import sleep

fileName = 'image.png'
delay = 5

def main():
    from pyperclip import copy

    path = checkClipboard()
    decoded = decodeQR(img=path)
    if decoded:
        copy(text=decoded[0])
        deleteFile(path=fileName)

def checkClipboard():
    from PIL import ImageGrab

    while True:
        sleep(delay)
        im = ImageGrab.grabclipboard()

        if im:
            im.save(fileName, 'PNG')
            return f'./{fileName}'

def decodeQR(img):
    from cv2 import imread, QRCodeDetector

    image = imread(img)
    qcd = QRCodeDetector()

    retval, decoded_info, points, straight_qrcode = qcd.detectAndDecodeMulti(image)

    if retval:
        return decoded_info
    else:
        return None

def deleteFile(path):
    from os import remove
    remove(path)

if __name__ == '__main__':
    while True:
        sleep(delay)
        try:
            main()
        except:
            deleteFile(path=fileName)
            continue

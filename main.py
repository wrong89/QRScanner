fileName = 'image.png'

def main():
    from pyperclip import copy

    path = checkClipboard()
    decoded = decodeQR(img=path)
    copy(text=decoded[0])
    deleteFile(path=fileName)

def checkClipboard():
    from PIL import ImageGrab

    while True:
        im = ImageGrab.grabclipboard()

        if im:
            im.save(fileName, 'PNG')
            print('out while loop')
            return f'./{fileName}'

def decodeQR(img):
    from cv2 import imread, QRCodeDetector

    image = imread(img)
    qcd = QRCodeDetector()

    retval, decoded_info, points, straight_qrcode = qcd.detectAndDecodeMulti(image)

    if retval:
        return decoded_info
    else:
        return ['QR code is not defined']

def deleteFile(path):
    from os import remove
    remove(path)

if __name__ == '__main__':
    while True:
        try:
            main()
        except:
            deleteFile(path=fileName)
            continue

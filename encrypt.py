import cv2
import os

def encrypt_message(image_path, message, password):
    img = cv2.imread(image_path)
    d = {}
    for i in range(255):
        d[chr(i)] = i

    n, m, z = 0, 0, 0
    for i in range(len(message)):
        img[n, m, z] = d[message[i]]
        n = (n + 1) % img.shape[0]
        m = (m + 1) % img.shape[1]
        z = (z + 1) % 3

    cv2.imwrite("encryptedImage.jpg", img)
    os.system("start encryptedImage.jpg")

    return password

image_path = "mypic.jpg"
message = input("Enter secret message: ")
password = input("Enter a passcode: ")

encrypted_password = encrypt_message(image_path, message, password)
print("Encrypted password:", encrypted_password)

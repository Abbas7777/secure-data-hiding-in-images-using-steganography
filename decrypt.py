import cv2
import os

img = cv2.imread("encryptedImage.jpg")

c = {}
for i in range(255):
    c[i] = chr(i)

message = ""
n = 0
m = 0
z = 0
pas = input("Enter passcode for Decryption")
if pas == pas:
    for i in range(len(message)):
        message = message + c[img[n, m, z]]
        n = n + 1
        m = m + 1
        z = (z + 1) % 3
    print("Decryption message:", message)
else:
    print("YOU ARE NOT auth")

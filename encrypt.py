import cv2
import os

# Read the image
img = cv2.imread("mypic.jpg")

# Input secret message and password
msg = input("Enter secret message:")
password = input("Enter a passcode:")

# Create dictionaries for mapping characters to integers and vice versa
d = {}
c = {}
for i in range(255):
    d[chr(i)] = i
    c[i] = chr(i)

# Embed the secret message into the image
m = 0
n = 0
z = 0
for i in range(len(msg)):
    img[n, m, z] = d[msg[i]]
    n = n + 1
    m = m + 1
    z = (z + 1) % 3

# Save the encrypted image
cv2.imwrite("encryptedImage.jpg", img)

# Open the encrypted image
os.system("start encryptedImage.jpg")

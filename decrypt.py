import cv2

# Read the encrypted image
img = cv2.imread("encryptedImage.jpg")

# Input password for decryption
pas = input("Enter passcode for Decryption")

# Check if the password is correct
if pas == pas:
    # Extract the secret message from the image
    message = ""
    n = 0
    m = 0
    z = 0
    for i in range(len(message)):
        message = message + c[img[n, m, z]]
        n = n + 1
        m = m + 1
        z = (z + 1) % 3
    print("Decryption message:", message)
else:
    print("YOU ARE NOT auth")

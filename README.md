# **Image Steganography Using LSB Technique**  

A Python-based steganography project that securely hides a secret message and passcode within an image using Least-Significant-Bit (LSB) encoding, allowing for safe retrieval.  

## **Overview**  
This project leverages LSB steganography to embed a secret message and passcode into an image. It includes two Python scripts with user-friendly GUIs built using Tkinter for seamless encryption and decryption.  

## **Features**  

### **Encryption**  
- Hides a secret message and passcode in `mypic.jpg` and saves the encoded image as `encrypted.png`.  

### **Decryption**  
- Extracts the hidden message from `encrypted.png` when the correct passcode is provided.  

### **User-Friendly GUI**  
- Intuitive Tkinter-based interfaces for both encryption and decryption.  

### **Robust Data Storage**  
- Utilizes a header to store message and passcode lengths for accurate extraction.  

## **Requirements**  
- IDLE Python
- OpenCV  
- NumPy  
- Tkinter (typically included with Python)  

## **Installation**  
1. Clone the repository.  
2. Install the required dependencies:  
   ```sh
   pip install opencv-python numpy
   ```  
3. Place an image named `mypic.jpg` in the project directory.

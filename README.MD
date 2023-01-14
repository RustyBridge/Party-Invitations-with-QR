## **Party Invitations with QR**

A project where I aimed to generate in bulk, unique invitations for a party, combining an image template file with multiple QR code files, using Python

### **Description:**

1. Created the template image file using a Graphics Editor

2. Generated the QR codes using a website (Can be done with the Python qrcode library as well)

3. The following libraries and modules were used: The Python Imaging Library (PIL), Global (glob) and OS (os)

4. The script:\
a) Creates a listing of all the unique QR files in the specified directory\
b) For every QR file in the listing, the template image file and the QR file are loaded, converted appropriately and merged\
c) Finally the resulting image file is saved on the Invitations directory

# Automatic_certificate_generation
 

This is a Python program that generates certificates for participants of an event using data from a CSV file. The program reads the CSV file and retrieves the names of participants and the event name. It then uses a pre-designed certificate template and overlays the retrieved data onto the template to create personalized certificates.

 **Requirements**
 - Python >= 3.7 (I used 3.11)
 - cv2 Library (pip install cv2)
 - csv

**Usage**
Create a CSV file named names.csv containing the participant names and the event name in the following format:

Place the certificate template named certificate.jpg in the same directory as the program.

The program will generate a certificate for each participant in the CSV file and save them in the same directory as the program.

**Customization**
To use a different certificate template, replace the file named certificate_template.png with your own template. Ensure that the template has a transparent area where the participant name and event name will be added.

To change the font or size of the text, modify the values in the program where indicated.

**Limitations**
The program currently supports only one template and one font style and size.

The program does not support batch printing of certificates.

soon will be making the similar program using more advanced technologies

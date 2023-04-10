import cv2
import csv

with open('names.csv') as f:
    reader = csv.reader(f)
    names_list = [name for row in reader for name in row]

print(names_list)
for index, name in enumerate(names_list):
    template = cv2.imread('certificate.jpg')
    cv2.putText(template, 
                name, 
                (700, 800), 
                cv2.FONT_HERSHEY_SCRIPT_COMPLEX,
                4, 
                (0, 0, 0), 
                3,
                cv2.LINE_AA)
    cv2.imwrite("certificate_gen/"+name+".jpg", template)
    print('Proccessing Certificate ({})/({})'. format (index+1, len(names_list)))
# # import the necessary packages
# from PIL import Image
# import pytesseract
# import argparse
# import cv2
# import os
 
# # construct the argument parse and parse the arguments



import sys
import cv2
import pytesseract
from PIL import Image
import datefinder
from datetime import datetime
# print(int(sys.argv[1]) + int(sys.argv[2]))

CURRENT_DATE = datetime.date(datetime.now())
image = cv2.imread(sys.argv[1])
grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

filename = "output.png"
cv2.imwrite(filename, grayImage)

outputText = pytesseract.image_to_string(Image.open(filename))
matches = datefinder.find_dates(outputText, source=True)

months = {"January", "Jan", "February", "Feb", "March",
		  "Mar", "April", "Apr", "May", "June", "Jun", "July",
		  "Jul", "August", "Aug", "September", "Sep",
		  "October", "Oct", "November", "Nov",
		  "December", "Dec"}

for match in matches:
	print(match[1])


#for December 24, 2015 format
#matches are tuples with values of where it read the date(String) from and the date(String)
# for match in matches:
# 	for month in months: #checks all month words
# 		dateWordForm = month + " %d, %d"
# 		for x in range(1,32):
# 			for y in range(2010, int(str(CURRENT_DATE).split('-', 1)[0])):
# 				testDate = dateWordForm % (x,y)
# 				if(testDate == match[1]):
# 					print(match[0])



# cv2.imshow("Image", image)
# cv2.imshow("Output", grayImage)
# cv2.waitKey(0)




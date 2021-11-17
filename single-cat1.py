import cv2
import numpy as np
import csv
import glob
item_roi = []
item_backgr = []


for item in glob.glob("data/noleft/*.jpg"):
	item_roi=np.append(item_roi,item)
print(f"item in roi folder: {len(item_roi)}")
for item in glob.glob("notraffic/*.png"):
    item_backgr=np.append(item_backgr,item)
print(f"item in roi folder: {len(item_backgr)}")
with open('annotation1_unsigned.csv', 'w', newline='') as csvfile:
	csvfile = csv.writer(csvfile, delimiter=',',
                            quotechar=',', quoting=csv.QUOTE_MINIMAL)
	for ite in range(10):
		for i in range(len(item_roi)):
			img = cv2.imread(item_backgr[np.random.randint(0,916)]) #240x320
			img2=cv2.imread(item_roi[i])
			filename = f'aug{ite}_{i}.jpg'
			x_min=np.random.randint(0,320-img2.shape[1])
			y_min = np.random.randint(0,240-img2.shape[0])
			img[y_min:y_min+img2.shape[0], x_min:x_min+img2.shape[1]] = img2


			row= ['{}'.format(filename), '{}'.format(320), '{}'.format(240), 'unsigned', 
	            '{}'.format(x_min), '{}'.format(y_min), '{}'.format(x_min+img2.shape[1]), '{}'.format(y_min+img2.shape[0])]
			csvfile.writerow(row)
			cv2.imwrite("data_agument1_unsigned/"+"{}".format(filename), img)

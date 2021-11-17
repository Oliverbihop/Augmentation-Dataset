import xml.etree.ElementTree as ET
import glob
import numpy as np 
import csv
# annotation_file = f"Annotations/{image_id}.xml"
files =[]
for item in glob.glob("Annotations_signed/*.xml"):
    for img in glob.glob("data_agument1_signed/*.jpg"):
        files = np.append(item,files)
        annotation_file = files[0]
        tree = ET.parse(annotation_file)
        object1 = tree.find("object")
        xmin=object1[4][0].text
        ymin=object1[4][1].text
        xmax=object1[4][2].text
        ymax=object1[4][3].text

        print("vat1",xmin)
      
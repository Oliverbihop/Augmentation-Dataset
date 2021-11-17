import xml.etree.cElementTree as ET
import pandas as pd 
import re
data = pd.read_csv("annotation1_signed.csv", header = None)
y=0
for i in range(len(data)):
	name = data[0][i]
	temp = re.findall(r'\d+', name) 
	res = list(map(int, temp))
	print(f"name: {name}, iter: {res[0]}, i: {res[1]} ")

	x1 = data[4][i]
	y1 = data[5][i]
	x2 = data[6][i]
	y2 = data[7][i]

	annotation = ET.Element('annotation')
	ET.SubElement(annotation, 'folder').text = 'widerface'
	ET.SubElement(annotation, 'filename').text = f"{name}"
	# ET.SubElement(annotation, 'path').text = '/home/elliot/Documents/mmdetection_object_detection_demo/data/vedai/train_images/'
	source = ET.SubElement(annotation, 'source')
	ET.SubElement(source, 'database').text = 'Unknown'
	ET.SubElement(source, 'annotation').text = 'PASCAL VOC2007'
	ET.SubElement(source, 'image').text = 'flickr'
	ET.SubElement(source, 'flickr').text = '-1'
	ET.SubElement(annotation, 'segmented').text = '0'
	size = ET.SubElement(annotation, 'size')
	ET.SubElement(size, 'width').text = "320"
	ET.SubElement(size, 'height').text = "240"
	ET.SubElement(size, 'depth').text = "3"
	ob = ET.SubElement(annotation, 'object')
	ET.SubElement(ob, 'name').text = 'signed'
	ET.SubElement(ob, 'pose').text = 'Unspecified'
	ET.SubElement(ob, 'truncated').text = '1'
	ET.SubElement(ob, 'difficult').text = '0'
	bbox = ET.SubElement(ob, 'bndbox')
	ET.SubElement(bbox, 'xmin').text = str(x1)
	ET.SubElement(bbox, 'ymin').text = str(y1)
	ET.SubElement(bbox, 'xmax').text = str(x2)
	ET.SubElement(bbox, 'ymax').text = str(y2)

	tree = ET.ElementTree(annotation)
	tree.write(f"Annotations/au1{res[0]}_{res[1]}.xml")

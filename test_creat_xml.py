import xml.etree.cElementTree as ET


annotation = ET.Element('annotation')
ET.SubElement(annotation, 'folder').text = 'widerface'
ET.SubElement(annotation, 'filename').text = "img21.png"
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
ET.SubElement(ob, 'name').text = 'Vehicle'
ET.SubElement(ob, 'pose').text = 'Unspecified'
ET.SubElement(ob, 'truncated').text = '1'
ET.SubElement(ob, 'difficult').text = '0'
bbox = ET.SubElement(ob, 'bndbox')
ET.SubElement(bbox, 'xmin').text = "12"
ET.SubElement(bbox, 'ymin').text = "12"
ET.SubElement(bbox, 'xmax').text = "24"
ET.SubElement(bbox, 'ymax').text = "24"

fileName = "tenfile"
tree = ET.ElementTree(annotation)
tree.write("a.xml")
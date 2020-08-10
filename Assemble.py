# Converting annotations from xml to csv format.
%pylab inline

import settings
import os, sys, random
import xml.etree.ElementTree as ET
from glob import glob
from shutil import copyfile

annotations = glob('Dataset/Annotations/*.xml')
print(annotations)
df = []
cnt = 0
for file in  annotations:
  prev_filename = file.split('/')[-1].split('.')[0] + '.jpg'
  filename = str(cnt) + '.jpg'
  row = []
  parsedXML = ET.parse(file)
  for node in parsedXML.getroot().iter('object'):
    blood_cells = node.find('name').text
    xmin = int(node.find('bndbox/xmin').text)
    xmax = int(node.find('bndbox/xmax').text)
    ymin = int(node.find('bndbox/ymin').text)
    ymax = int(node.find('bndbox/ymax').text)

    row = [prev_filename, filename, blood_cells, xmin, xmax,ymin, ymax]
    df.append(row)
    cnt += 1

data = pd.DataFrame(df, columns=['prev_filename', 'filename', 'cell_type','xmin', 'xmax', 'ymin', 'ymax'])
data = data[['filename', 'cell_type', 'xmin', 'xmax', 'ymin', 'ymax']]

data.to_csv(os.path.join(settings.PROCESSED_DIR , 'blood_cells') , index = False)

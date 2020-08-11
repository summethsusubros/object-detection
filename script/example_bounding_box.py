import settings
import matplotlib.pyplot as plt
from matplotlib import patches
import os
import pandas as pd

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
image = plt.imread(os.path.join(settings.IMAGE_DIR , 'BloodImage_00292.jpg'))
plt.imshow(image)

data = pd.read_csv(os.path.join(settings.PROCESSED_DIR ,'blood_cells'))
data_for_one = data.loc[data['prev_filename'] == 'BloodImage_00292.jpg']

for i in range(len(data_for_one)):
  height = data_for_one['ymax'][i] - data_for_one['ymin'][i]
  width = data_for_one['xmax'][i] - data_for_one['xmin'][i]
  left_bottom_x = data_for_one['xmin'][i]
  left_bottom_y = data_for_one['ymin'][i]
  if data_for_one['cell_type'][i] == 'RBC':
    edgecolor = 'red'
    ax.annotate('RBC', xy=(data_for_one['xmax'][i]-40,data_for_one['ymin'][i]+20))
  elif data_for_one['cell_type'][i] == 'WBC':
    edgecolor = 'yellow'
    ax.annotate('WBC', xy=(data_for_one['xmax'][i]-40,data_for_one['ymin'][i]+20))
  elif data_for_one['cell_type'][i] == 'Platelets':
    edgecolor = 'green'
    ax.annotate('Platelets', xy=(data_for_one['xmax'][i]-40,data_for_one['ymin'][i]+20))  

  box = patches.Rectangle((left_bottom_x,left_bottom_y), width, height, edgecolor = edgecolor, facecolor = 'none',alpha = 1,linewidth = 2)
  ax.add_patch(box)

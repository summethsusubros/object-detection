import settings
import random
import numpy as np
import pandas as pd
import os

dataset =  pd.read_csv(os.path.join(settings.PROCESSED_DIR,'blood_cells'))

all_photos = dataset['filename'].unique()
random.shuffle(all_photos)

train_to_test_ratio = settings.TRAIN_TO_TEST_RATIO
train_size = int(len(all_photos) * (train_to_test_ratio/(train_to_test_ratio + 1)))

train = all_photos[:train_size]
test = all_photos[train_size:]

train = dataset[dataset['filename'].isin(train)] 
test = dataset[dataset['filename'].isin(test)]

train.to_csv(os.path.join(settings.PROCESSED_DIR , 'train') , index=False)
test.to_csv(os.path.join(settings.PROCESSED_DIR , 'test') , index=False)

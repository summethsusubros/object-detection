import settings
import os
import pandas

format_df = pd.read_csv(os.path.join(settings.PROCESSED_DIR,'train'))
format_df  = format_df[['prev_filename','xmin', 'ymin', 'xmax','ymax', 'cell_type']]
format_df['prev_filename'] = format_df['prev_filename'].apply(lambda s : 'Dataset/JPEGImages/' + str(s))
format_df = format_df.rename(columns={'prev_filename' : 'filepath' ,'cell_type' : 'class_name' })

format_df.to_csv(os.path.join(settings.PROCESSED_DIR , 'format_train.txt') , index=False)


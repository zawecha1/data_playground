import json
import os
import logging

def mkdirs(dir2make):
    if isinstance(dir2make,list):
        for i_dir in dir2make:
            if not os.path.exists(i_dir):
                os.makedirs(i_dir)
    elif isinstance(dir2make,str):
        if not os.path.exists(dir2make):
            os.makedirs(dir2make)
    else:
        raise ValueError("dir2make should be string or list type.")
        
def func_label_encoding(df,col,to_save=True,save_dir='./model_meta_data',file_marker=None,transform=True,overwrite=False):
    encoding_dict = {} 
    df[col] = df[col].apply(lambda x: '-999' if x == -999 else x)
    df[col] = df[col].astype('str')
    df[col] = df[col].fillna('-999')
    all_lst = list(df[col].unique())
    all_lst = list(map(str,all_lst))
    for i,iu in enumerate(all_lst):
        encoding_dict[iu] = i
    if to_save:
        mkdirs(save_dir)
        if file_marker is None:
            file_marker = col
        file_nm = f'encoding_{file_marker}.json'
        abs_file_path = os.path.join(save_dir, file_nm)
        if not os.path.exists(abs_file_path):
            with open(abs_file_path, 'w') as f:
                json.dump(encoding_dict, f)
        else:
            if overwrite:
                logging.warning(f"\nFile '{abs_file_path}' already exists and will be overwrited!")
                os.remove(abs_file_path)
                with open(abs_file_path, 'w') as f:
                    json.dump(encoding_dict, f)
            else:
                logging.warning(f"\nFile '{abs_file_path}' already exists and did not be overwrited!\
                \nIf you want to overwrite it, set argument overwrite as True")
    if '-999' in encoding_dict:
        encoding_dict['-999'] = -999
    if transform:
        df[col] = df[col].apply(lambda x: encoding_dict[x] if x in encoding_dict else -888)
    return encoding_dict

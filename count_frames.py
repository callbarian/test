import os
import numpy as np

def count():
    cur_dir = os.path.join(os.getcwd(),'test_frame_mask')
    files = sorted(os.listdir(cur_dir))
    list_shapes = []
    for file in files:
        numpy_files = np.load(os.path.join(cur_dir,file))
        list_shapes.append(numpy_files.shape)
        print(file,numpy_files)
    print(min(list_shapes))
if __name__ == "__main__":
    count()

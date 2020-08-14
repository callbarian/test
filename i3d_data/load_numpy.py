import os
import numpy as np

rgb_path = os.getcwd() +'/v_CricketShot_g04_c01_rgb.npy'
flow_path = os.getcwd() + '/v_CricketShot_g04_c01_flow.npy'

rgb_np = np.load(rgb_path)
flow_np = np.load(flow_path)

print("rgb: ",rgb_np)
print("optical flow: ",flow_np)
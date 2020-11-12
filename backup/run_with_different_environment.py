import os
import subprocess
def run():
    result = subprocess.Popen(['sh','/home/callbarian/C3D/C3D-v1.0/examples/c3d_feature_extraction/call_environment.sh','/home/callbarian/bin/miniconda3/envs/c3d_py36/bin/python','/home/callbarian/C3D/C3D-v1.0/examples/c3d_feature_extraction/extract_C3D_feature.py'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)

    result = subprocess.Popen(['sh','/home/callbarian/C3D/C3D-v1.0/examples/c3d_feature_extraction/call_environment.sh','/home/callbarian/bin/miniconda3/envs/Anomaly_py36/bin/python','/home/callbarian/AnomalyDetectionCVPR2018-master/Demo_GUI.py'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)

if __name__ =="__main__":
    run()
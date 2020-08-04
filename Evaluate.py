import os
import numpy as np
import scipy.io as sio
import sklearn.metrics as skmetr

def evaluate():
    gt_root = './gt_data'
    Fscore_root = './Model_Res'
    
    gt_data_list = []
    Fscore_data_list = []

    for gt_name,Fscore_name in zip(sorted(os.listdir(gt_root)),sorted(os.listdir(Fscore_root))):
        gt_data = np.load(os.path.join(gt_root,gt_name))
        #gt_data = sio.loadmat(os.path.join(gt_root,gt_name))['gt'][0]
        Fscore_data = sio.loadmat(os.path.join(Fscore_root,Fscore_name))['Score'][0]
        #gt_data = np.array(gt_data)
        Fscore_data = np.array(Fscore_data)
        
        #Fscore_norm = Fscore_data - Fscore_data.min()
        #Fscore_norm = Fscore_norm / Fscore_norm.max()
        #print(gt_data)
        #print(Fscore_data)
        #print(np.array(gt_data).shape,np.array(Fscore_norm).shape)
        gt_data_list.extend(gt_data[:-1])
        Fscore_data_list.extend(Fscore_data)
    #print(np.array(gt_data_list).shape,np.array(Fscore_data_list).shape)
    fpr,tpr,thresholds_roc = skmetr.roc_curve(gt_data_list,Fscore_data_list,pos_label=1)
    precision,recall,thresholds_prc = skmetr.precision_recall_curve(gt_data_list,Fscore_data_list,pos_label=1)
    print('fpr,tpr,thresholds: ',fpr,tpr,thresholds_roc)
    auc = skmetr.auc(fpr,tpr)
    print('auroc: ',auc)
    auc = skmetr.auc(recall,precision)
    print('auprc: ',auc)
    sio.savemat('./MIL_auroc.mat',{'tpr':tpr},{'fpr':fpr})
    sio.savemat('./MIL_auprc.mat',{'recall':recall},{'precision':precision})
if __name__ == "__main__":
    evaluate()


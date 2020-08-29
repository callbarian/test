import os
import sklearn.metrics as skmetr
import scipy.io as scio
import argparse
import numpy as np
import matplotlib.pyplot as plt

def parser_args():
    parser = argparse.ArgumentParser(description='Evaluating each model with AUROC and AUPRC')
    parser.add_argument('-t','--type',type=str, default='show_roc',help='ROC as default. \'show_roc\' for ROC, \'show_prc\' for PRC. ')
    parser.add_argument('-p','--path',type=str, default=os.getcwd(),help='path for matrix files. Default is current directory')

    return parser.parse_args()

def show_roc(mat_path):
    plt.figure()
    for mat in sorted(os.listdir(mat_path)):
        auroc = scio.loadmat(os.path.join(mat_path,mat))['auroc']
        fpr = np.squeeze(auroc['fpr'],axis=0)[0]
        tpr = np.squeeze(auroc['tpr'],axis=0)[0]
        fpr = fpr[0]
        tpr = tpr[0]
        auc = skmetr.auc(fpr,tpr)
        print(auc)
        plt.plot(fpr,tpr,label=(mat.split('.')[0]+':'+str(auc)[:5]))
    
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.legend()
    plt.show()
    plt.pause(3)
def show_prc(mat_path):
    for mat in sorted(os.listdir(mat_path)):
        auprc = scio.loadmat(os.path.join(mat_path,mat))['auprc']
        recall = auprc['recall'][0][0][0]
        precision = auprc['precision'][0][0][0]
        auc = skmetr.auc(recall,precision)
        print(auc)
        plt.plot(recall,precision,label=(mat.split('.')[0]+':'+str(auc)[:5]))
    plt.xlabel('Recall')
    plt.ylabel('Precision')
    plt.legend()
    plt.show()
    plt.pause(3)
evaluate_type_function = {
    'show_roc': show_roc,
    'show_prc': show_prc
}

def evaluate(eval_type,root_dir):
    assert eval_type in evaluate_type_function,'There is no type of evaluation{},please check{}' \
        .format(eval_type,eval_type_function.keys())
    eval_func = evaluate_type_function[eval_type]
    results = eval_func(os.path.join(root_dir,eval_type))

if __name__ =="__main__":
    args = parser_args()
    eval_type = args.type
    file_path = args.path

    print('Evaluation type : {}'.format(eval_type))
    print('File path : {}'.format(file_path))

    evaluate(eval_type,file_path)

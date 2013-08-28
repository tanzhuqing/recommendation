# -*- coding: cp936 -*-
#均方根误差RMSE 平均绝对误差MAE

def RMSE(records):
    return math.sqrt(sum([(rui-pui)*(rui-pui) for u,i,rui,pui in records])/float(len(records)))


def MAE(records):
    return sum([abs(rui-pui) for u,i,rui,pui in records])/float(len(records))


#准确率和召回率

def PrecisionRecall(test,N):
    hit = 0
    n_recall = 0
    n_precision = 0
    for user,items in test.items():
        rank = Recommend(user,N)
        hit += len(rank & item)
        n_precision += N
    return [hit / (1.0 * n_recall),hit /(1.0*n_precision)]

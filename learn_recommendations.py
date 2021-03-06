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


#尼基系数
def GiniIndex(p):
    j = 1
    n = len(p)
    G = 0
    for item,weight in sorted(p.items(),key=itemgetter(1)):
        G += (2*j -n -1)*weight
    return G / float(n-1)


#将数据集随机分成训练集合测试集
def SplitData(data,M,k,seed):
    test = []
    train = []
    random.seed(seed)
    for user,item in data:
        if random.randint(0,M) == k:
            test.append([user,item])
        else:
            train.append([user,item])
        return train,test

    

#召回率
def Recall(train,test,N):
    hit = 0
    all = 0
    for user in train.keys():
        tu = test[user]
        rank = GetRecommendation(user,N)
        for item,pui in rank
            if item in tu:
                hit += 1
        all += len(tu)
    return hit/(all*1.0)

#准确率

def Precision(train,test,N):
    hit = 0
    all = 0
    for user in train.keys():
        tu = test[user]
        rank = GetRecommendation(user,N)
        for item,pui in rank:
            if item in tu:
                hit += 1
        all += N
    return hit / (all * 1.0)

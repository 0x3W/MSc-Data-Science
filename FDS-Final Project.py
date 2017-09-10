import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn.cross_validation
from sklearn.linear_model import Lasso

#train = pd.read_csv("train.csv", index_col=0)
train = pd.read_csv(sys.argv[1], index_col=0)

train.columns[train.isnull().sum() > 1000] # ['Alley', 'PoolQC', 'Fence', 'MiscFeature']
train.drop(['Alley', 'PoolQC', 'Fence', 'MiscFeature'], axis=1, inplace=True)
train.columns[train.isnull().sum() > 500]
train.drop(['FireplaceQu'], axis=1, inplace=True)

train['yrSinceBuilt'] = 2017 - train['YearBuilt']
train['yrSinceRemod'] = 2017 - train['YearRemodAdd']
train['1stFlr_2ndFlr_Sf'] = np.log1p(train['1stFlrSF'] + train['2ndFlrSF'])
train['1stFlr_2ndFlr_Sf1'] = train['1stFlrSF'] + train['2ndFlrSF']
train['Bsmt'] = train['BsmtFinSF1'] + train['BsmtFinSF2']
train['All_Liv_SF'] = np.log1p(train['1stFlr_2ndFlr_Sf'] + train['LowQualFinSF'] + train['GrLivArea'])
train['All_Liv_SF1'] = train['1stFlr_2ndFlr_Sf'] + train['LowQualFinSF'] + train['GrLivArea']
train['LotArea1'] = np.log1p(train['LotArea'])
train['GrLivArea1'] = np.log1p(train['GrLivArea'])

train.drop(train[train['GrLivArea'] > 4000].index, inplace=True)
train.drop(train[train['1stFlr_2ndFlr_Sf'] < 6.3].index, inplace=True)
train.drop(train[train['SalePrice'] > 500000].index, inplace=True)
train.drop(train[train['LotFrontage'] > 300].index, inplace=True)
train.drop(train[train['LotArea'] > 200000].index, inplace=True)
train.drop(train[train['MasVnrArea'] > 1500].index, inplace=True)
train.drop(train[train['BsmtFinSF1'] > 2000].index, inplace=True)
train.drop(train[train['Bsmt'] > 2000].index, inplace=True)
train.drop(train[train['TotalBsmtSF'] > 3000].index, inplace=True)
train.drop(train[train['1stFlr_2ndFlr_Sf1'] > 4000].index, inplace=True)
train.drop(train[train['GarageArea'] > 1230].index, inplace=True)
train.drop(train[train['OpenPorchSF'] > 500].index, inplace=True)

df_with_dummies = pd.get_dummies(train)
df_with_dummies = df_with_dummies.fillna(df_with_dummies.median(axis=0), inplace=True)
df_with_dummies = df_with_dummies.fillna(0, inplace=False) # fill NaNs

train_num = df_with_dummies.select_dtypes([np.number])
#train_num.shape # 37 columns
#train_num.isnull().sum()
train_num = train_num.fillna(train_num.median(axis=0), inplace=True)
train_num = train_num.fillna(0, inplace=False) # fill NaNs

trainnum1 = train_num
trainnum1 = trainnum1.drop(['SalePrice'], axis=1, inplace=False)
trainnum1 = trainnum1.drop(['MSZoning_C (all)'], axis=1, inplace=False)
trainnum1 = trainnum1.drop(['SaleCondition_Abnorml'], axis=1, inplace=False)
trainnum1 = trainnum1.drop(['CentralAir_N'], axis=1, inplace=False)
trainnum1 = trainnum1.drop(['Neighborhood_MeadowV'], axis=1, inplace=False)
trainnum1 = trainnum1.drop(['Neighborhood_IDOTRR'], axis=1, inplace=False)
trainnum1 = trainnum1.drop(['KitchenAbvGr'], axis=1, inplace=False)
trainnum1 = trainnum1.drop(['Electrical_Mix'], axis=1, inplace=False)
trainnum1 = trainnum1.drop(['Heating_Floor'], axis=1, inplace=False)
trainnum1 = trainnum1.drop(['Heating_OthW'], axis=1, inplace=False)
trainnum1 = trainnum1.drop(['Exterior1st_ImStucc'], axis=1, inplace=False)
trainnum1 = trainnum1.drop(['Condition2_RRAn'], axis=1, inplace=False)
trainnum1 = trainnum1.drop(['Condition2_RRNn'], axis=1, inplace=False)
#trainnum1 = trainnum1.drop(['MSSubClass_160'], axis=1, inplace=False)

#test = pd.read_csv("test.csv", index_col=0) # Kaggle's test set
test = pd.read_csv(sys.argv[2], index_col=0)
test['yrSinceBuilt'] = 2017 - test['YearBuilt']
test['yrSinceRemod'] = 2017 - test['YearRemodAdd']
test['1stFlr_2ndFlr_Sf'] = np.log1p(test['1stFlrSF'] + test['2ndFlrSF'])
test['All_Liv_SF'] = np.log1p(test['1stFlr_2ndFlr_Sf'] + test['LowQualFinSF'] + test['GrLivArea'])
test['1stFlr_2ndFlr_Sf'] = np.log1p(test['1stFlrSF'] + test['2ndFlrSF'])
test['1stFlr_2ndFlr_Sf1'] = test['1stFlrSF'] + test['2ndFlrSF']
test['Bsmt'] = test['BsmtFinSF1'] + test['BsmtFinSF2']
test['All_Liv_SF'] = np.log1p(test['1stFlr_2ndFlr_Sf'] + test['LowQualFinSF'] + test['GrLivArea'])
test['All_Liv_SF1'] = test['1stFlr_2ndFlr_Sf'] + test['LowQualFinSF'] + test['GrLivArea']
test['LotArea1'] = np.log1p(test['LotArea'])
test['GrLivArea1'] = np.log1p(test['GrLivArea'])

df_with_dummies1 = pd.get_dummies(test)
df_with_dummies1 = df_with_dummies1.fillna(df_with_dummies1.median(axis=0), inplace=True)
df_with_dummies1 = df_with_dummies1.fillna(0, inplace=False) # fill NaNs
test = df_with_dummies1
test = test.loc[:, trainnum1.columns] # select the variables that are in our model
test = test.fillna(test.median(axis=0), inplace=True) # fill NaNs
test = test.fillna(0, inplace=False) # fill NaNs

#def mseCV(model):
#    mse= np.sqrt(-sklearn.cross_validation.cross_val_score(model, X, ylog, scoring="mean_squared_error", cv = 11))
#    return(mse)
#alphas = [0.01, 0.005, 0.001, 0.0005, 0.0001]
#bestAlpha = [mseCV(Lasso(alpha = alpha)).mean() for alpha in alphas]

X, y = trainnum1.values, train_num['SalePrice']
ylog = np.log1p(y)
model_lasso = Lasso(alpha=5e-4, max_iter=50000).fit(X, ylog)
p1 = np.expm1(model_lasso.predict(test))
solution1 = pd.DataFrame({"id":test.index, "SalePrice":p1}, columns=['id', 'SalePrice'])
solution1.to_csv("preds.csv", index = False)

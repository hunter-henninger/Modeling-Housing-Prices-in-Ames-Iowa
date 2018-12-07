import numpy as np 
import pandas as pd

class DataPreprocessing:
    
    def __init__(self):
        pass
   
    def get_missing_values(self , data):
        df = pd.DataFrame([], columns=['features','num_missing_values'])
        df['features'] = data.columns[data.isna().any()].tolist()
        df['num_missing_values'] = [data[col].isna().sum() \
                                for col in data.columns \
                                if data[col].isna().sum() > 0]
        return df
    
    def impute_missing_values(self, df , method):
        dp = DataPreprocessing()
        df_numeric = df._get_numeric_data()
        df_null = dp.get_missing_values(df)
        for feature in df_null['features']:
            if feature in df_numeric:
                if method == 'mean':
                    df[feature].fillna(df[feature].mean() , inplace = True)
                elif method == 'median':
                    df[feature].fillna(df[feature].median() , inplace = True)
                elif method == 'random':
                    num_bag = df[feature].dropna()
                    df[feature] = df[feature].apply(lambda x: np.random.choice(num_bag) if np.isnan(x) else x) 

    def create_ordinal_data(self, df_train , df_test):
        df_object = df_train.select_dtypes(include = ['object'])
        df_object_test = df_test.select_dtypes(include = ['object'])
        for col in df_object.columns:
            avg_prices = {}
            category_dict={}
            for i , x in enumerate(df_object[col].unique()):
                avg_prices[i] = x ,df_train['saleprice'][df_object[col]==x].mean()
            sorted_dict = pd.DataFrame(avg_prices).T.sort_values(by = 1)

            for i,x in enumerate(sorted_dict[0]):
                category_dict[x]=i

            df_train[col] = df_object[col].map(category_dict)
            df_test[col] = df_object_test[col].map(category_dict)

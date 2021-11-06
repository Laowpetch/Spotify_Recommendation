from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import pandas as pd
import numpy as np

df = pd.read_csv('D:\\Work\\Python\\Linear\\Datacsv.csv')
def clean_dataset(df):
    assert isinstance(df, pd.DataFrame), "df needs to be a pd.DataFrame"
    df.dropna(inplace=True)
    indices_to_keep = ~df.isin([np.nan, np.inf, -np.inf]).any(1)
    return df[indices_to_keep].astype(np.float64)

clean_dataset(df)
features = ['10','10.1','10.2','10.2','10.3','10.4','10.5']
x = df.loc[:, features].values
x = StandardScaler().fit_transform(x)
pca = PCA(n_components=3)
pca.fit(x)
y = pca.transform(x)
print(y)
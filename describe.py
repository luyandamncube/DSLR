
import sys
import pandas as pd
from helpers import readData

df = pd.DataFrame()
def describe(df):
    # find and select numeric types in dataframe
    numeric = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
    df = df.select_dtypes(include=numeric)

    # Perform Summary operations & concatenate to dataframe
    df = pd.concat([
        df.count(axis=0),
        df.mean(axis=0),
        df.std(axis=0),
        df.min(axis=0), 
        df.quantile(0.25),
        df.quantile(0.50),
        df.quantile(0.75),  
        df.max(axis=0)    
        ], axis=1)

    # Rename columns 
    df.columns = ['Count','Mean', 'Std', 'Min','25%','50%','75%','Max']
    
    df = df.transpose()
    print(df)
    return(df)

if __name__ == "__main__":
    df =  readData(sys.argv)
    # print('SUCCESS: Data read')
    describe(df)

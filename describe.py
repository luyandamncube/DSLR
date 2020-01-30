import pandas as pd
import sys
df = pd.DataFrame()

# csvData = sys.argv
def readData(csvData):
    if (len(csvData) != 2):
        print('USAGE: python <SCRIPTNAME>.py dataset.csv')
        exit()
    elif (not csvData[1].endswith('.csv')):
        print("ERROR: dataset not in csv format")
        exit()
    else:
        try:
            # Read csv and remove index column
            df = pd.read_csv(csvData[1])
            # df = df.drop(['Index'],axis=1)
            return (df)
        except Exception as e:
            print(f'ERROR: {e}')

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

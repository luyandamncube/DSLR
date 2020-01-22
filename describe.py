import sys 
import pandas as pd

df = pd.DataFrame()

def readData():
    global df
    if (len(sys.argv) != 2):
        print('USAGE: python describe.py dataset.csv')
        exit()
    elif (not sys.argv[1].endswith('.csv')):
        print("ERROR: dataset not in csv format")
        exit()
    else:
        try:
            # Read csv and remove index column
            df = pd.read_csv(sys.argv[1])
            df = df.drop(['Index'],axis=1)
            # df.set_index('Index', inplace=True)
            # print(df.head(5))
        except Exception as e:
            print(f'ERROR: {e}')

def describe():
    global df
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
    # rename columns 
    df.columns = ['Count','Mean', 'Std', 'Min','25%','50%','75%','Max']
    
    df = df.transpose()
    # rename column names
    count = 0
    for name, values in df.iteritems():
        count += 1
        df.rename({ name: 'Feature ' + str(count)}, axis=1, inplace=True)

    print(df)

if __name__ == "__main__":
    readData()
    print('SUCCESS: Data read')
    describe()

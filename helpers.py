import pandas as pd

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


def filterHouse(df, rowName, value):
    temp_df = df.loc[df[rowName] == value]
    return(temp_df)


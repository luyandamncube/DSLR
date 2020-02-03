import sys
from helpers import readData
from describe import describe
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from itertools import combinations

# Graph plotting
ROWS = 4
COLUMNS = 4
'''
Calculate how many graphs we need
==================================
nPr = chose r out of a group of n
nPr = chose 2 out of a group of 13
nPr = n!/(n-R)!
nPr = 13!/(13-2)! = 13!/11! = 13*12 = 156

nCr = chose c out of a group of n
nCr = chose 2 out of a group of 13
nCr = n!/((n-R)!R!)
nCr = 13!/((13-2)!*2!) = 78
therefore, there are 78 UNIQUE scatter plots we need to show
'''

def plotData(df, x_axis, y_axis, row, column):
    global fig
    fig.add_trace(go.Scatter(
            x = df[x_axis], 
            y = df[y_axis], 
            mode='markers',
            name=x_axis + ' vs ' + y_axis,
            marker_color='#636bfa'
        ), row=row, col=column)
    fig.update_layout(
        # xaxis_title='Scores',
        # yaxis_title= 'Frequency',
        showlegend=False,
        font=dict(
            family="Courier New, monospace",
            size=8,
            color="#7f7f7f"
        ))
    fig.update_xaxes(title_text=x_axis, row=row, col=column)
    fig.update_yaxes(title_text=y_axis, row=row, col=column)

if __name__ == "__main__":
    df =  readData(sys.argv)
    df_numerical = describe(df)
    del df_numerical['Index']
    titles = tuple(df_numerical.columns)
    fig = make_subplots(
        rows=ROWS, cols=COLUMNS,
        # subplot_titles=titles,
        #todo: automate creating this list object!
        specs=[
                # row 1 
                [{"secondary_y": True}, {"secondary_y": True}, {"secondary_y": True}, {"secondary_y": True}],
                [{"secondary_y": True}, {"secondary_y": True}, {"secondary_y": True}, {"secondary_y": True}],
                [{"secondary_y": True}, {"secondary_y": True}, {"secondary_y": True}, {"secondary_y": True}],
                [{"secondary_y": True}, {"secondary_y": True}, {"secondary_y": True}, {"secondary_y": True}],
                ])


    _list = []
    for index, combo in enumerate(combinations(titles, 2)):  # 2 for pairs, 3 for triplets, etc
        # print(f'{index} | {combo}')
        _list.append(combo)
    
    r = 1
    index = 0
    _len = len(_list)
    print(f'list length: {_len}')
    while (r <= ROWS):
        c = 1
        while (c <= COLUMNS and index < _len):
            plotData(df, _list[index][0], _list[index][1], r,c)
            print(f'{index} | {_list[index][0]} | {_list[index][1]}')
            c += 1 
            index += 1
        r += 1  
 
    fig.show()
    while (r <= ROWS):
        c = 1
        while (c <= COLUMNS and index < _len):
            plotData(df, _list[index][0], _list[index][1], r,c)
            print(f'{index} | {_list[index][0]} | {_list[index][1]}')
            c += 1 
            index += 1
        r += 1
    fig.show()
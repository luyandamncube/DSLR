import sys
from describe import describe
from helpers import readData, filterHouse
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Graph plotting
ROWS = 3
COLUMNS = 5

def plotData(df, courseName, row, column):
    global fig  
    df_Ravenclaw = filterHouse(df, 'Hogwarts House','Ravenclaw')
    df_Hufflepuff = filterHouse(df, 'Hogwarts House','Hufflepuff')
    df_Gryffindor = filterHouse(df, 'Hogwarts House','Gryffindor')
    df_Slytherin = filterHouse(df, 'Hogwarts House','Slytherin')
    fig.add_trace(go.Histogram(
            x = df_Ravenclaw[courseName], 
            name='Ravenclaw',
            marker_color='#636bfa'
        ), row=row, col=column)
    fig.add_trace(go.Histogram(
            x = df_Hufflepuff[courseName], 
            name='Hufflepuff',
            marker_color='#ef553b'
        ), row=row, col=column)

    fig.add_trace(go.Histogram(
            x = df_Gryffindor[courseName], 
            name='Gryffindor',
            marker_color='#00cc96'
        ), row=row, col=column)
    fig.add_trace(go.Histogram(
            x = df_Slytherin[courseName], 
            name='Slytherin',
            marker_color='#ac63fa'
        ), row=row, col=column)
    fig.update_layout(
        # subplot_title=courseName,
        # xaxis_title='Scores',
        # yaxis_title= 'Frequency',
        showlegend=False,
        font=dict(
            family="Courier New, monospace",
            size=8,
            color="#7f7f7f"
        )
    )
    fig.update_xaxes(title_text="Scores", row=row, col=column)
    fig.update_yaxes(title_text="Frequency", row=row, col=column)

    # Overlay both histograms
    fig.update_layout(barmode='overlay')
    # Reduce opacity to see both histograms
    fig.update_traces(opacity=0.75)
    
if __name__ == "__main__":
    df =  readData(sys.argv)
    df_numerical = describe(df)
    titles = tuple(df_numerical.columns)
    fig = make_subplots(
        rows=ROWS, cols=COLUMNS,
        subplot_titles=titles,
        specs=[
                # row 1 
                [{"secondary_y": True}, {"secondary_y": True}, {"secondary_y": True}, {"secondary_y": True},{"secondary_y": True} ],
                # row 2 
                [{"secondary_y": True}, {"secondary_y": True}, {"secondary_y": True}, {"secondary_y": True},{"secondary_y": True} ],
                # row 3 
                [{"secondary_y": True}, {"secondary_y": True}, {"secondary_y": True}, {"secondary_y": True},{"secondary_y": True} ]   
            ])
    r = 1
    index = 0
    _len = len(titles)
    while (r <= ROWS):
        c = 1
        while (c <= COLUMNS and index < _len):
            plotData(df, titles[index], r, c)
            c += 1 
            index += 1
        r += 1   
    fig.show()
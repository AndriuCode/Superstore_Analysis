import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots



def order_counting_over_timer_graph(data):
    fig = px.line(data, x='year-month of order', y='count', title="Order Counting Over Time")
    fig.update_traces(line=dict(color='#A054E8'))
    fig.show()




def top_customers_orders_graph(data):
    fig = go.Figure(data=[go.Table(
        header=dict(
            values=list(data.columns), 
            font=dict(color='white', size=12), 
            fill_color='#311C59', 
            align='center'),
        cells=dict(
            values=[data['Customer Name'], data['Count']], 
            fill_color='lavender', 
            align='left'))
    ])
    fig.update_layout(title="Top 10 Customers with the most Orders")
    fig.show()




def proportions_circle_graph(data_1, data_2, data_3):
    fig = make_subplots(
        rows=1, 
        cols=3, 
        specs=[[{'type':'domain'}, {'type':'domain'}, {'type':'domain'}]],
        subplot_titles=['Segment', 'Region', 'Category']    
    )
    fig.add_trace(go.Pie(
        labels=data_1['Segment'], 
        values=data_1['Proportion'], 
        name="Segment",
        marker = dict(
            colors=['#1F5C48', '#07A872', '#4DE1B0'],
            line=dict(color='white', width=2)
        )
    ), 1, 1)

    fig.add_trace(go.Pie(
        labels=data_2['Region'], 
        values=data_2['Proportion'], 
        name="Region",
        marker = dict(
            colors=['#3C2E5C', '#6F54A8', '#916EDB', '#C2B4E1'],
            line=dict(color='white', width=2)
        )
    ), 1, 2)

    fig.add_trace(go.Pie(
        labels=data_3['Category'], 
        values=data_3['Proportion'], 
        name="Category",
        marker = dict(
            colors=['#5C3F2B', '#A89282', '#DBBEA9'],
            line=dict(color='white', width=2)
        )
    ), 1, 3)
    fig.update_layout(title_text='Proportions Depending on the...')
    fig.show()




def violin_graph(data, title):
    fig = px.violin(x=data, title=title)
    fig.show()
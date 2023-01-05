import plotly.express as px
import plotly.graph_objects as go



def comparison_amount_salesprofit_graph(data):
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=data['year-month of order'], 
        y=data['Sales'],
        mode='lines',
        name='Sales'
    ))
    fig.add_trace(go.Scatter(
        x=data['year-month of order'], 
        y=data['Profit'],
        mode='lines',
        name='Profit'
    ))
    fig.update_layout(
        title="Comparison of the Amount of Sales and Profits Over Time", 
        xaxis_title="year-month of order", 
        yaxis_title="amount of sales and profits"
    )
    fig.show()




def average_discounts_monthly_graph(data):
    fig = px.line(data, x='year-month of order', y='Discount', title="Average Order Discounts per Month")
    fig.update_layout(yaxis_title="average of discounts")
    fig.update_traces(line=dict(color='#A054E8')) 
    fig.show()




def top_profitable_customers_graph(data):
    fig = go.Figure(data=[go.Table(
        header=dict(
            values=list(data.columns), 
            font=dict(color='white', size=12), 
            fill_color='#311C59', 
            align='center'),
        cells=dict(
            values=[data['Customer Name'], data['Profit'], data['Discount']], 
            fill_color='lavender', 
            align='left'))
    ])
    fig.update_layout(title="Top 10 most Profitable Customers")
    fig.show()




def profit_distribution_graph(data, cols, title, colors=None):
    fig = px.bar(data, x=cols[2], y=cols[0], color=cols[1], color_discrete_sequence=colors, title=title)
    fig.show()




def relationship_sales_profits_graph(data):
    fig = px.scatter(data, x="Sales", y="Profit", trendline="ols", title="Relationship Between Sales and Profits")
    fig.show()




def correlations_graph(data):
    fig = px.imshow(data, text_auto=True, title="Heatmap of Correlations in the Dataset")
    fig.show()
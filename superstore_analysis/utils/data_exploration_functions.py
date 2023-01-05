def create_grouped_dfdate(data, option):
    data['year-month of order'] = data['Order Date'].dt.strftime('%Y-%m')

    if option == 1:
        grouped_data = data.groupby('year-month of order').count()
        grouped_data = grouped_data.reset_index().rename(columns={'Order ID': 'count'})
    elif option == 2:
        grouped_data = data.groupby('year-month of order').agg({'Sales': 'sum', 'Discount': 'mean', 'Profit': 'sum'})
        grouped_data = grouped_data.reset_index()

    return grouped_data



def create_grouped_dfcustomer(data, option):

    if option == 1:
        grouped_data = data.groupby('Customer Name').count().sort_values('Customer ID', ascending=False)
        grouped_data = grouped_data.reset_index().head(10).rename(columns={'Customer ID': 'Count'})
    elif option == 2:
        grouped_data = data.groupby('Customer Name').agg({'Discount': 'mean', 'Profit': 'sum'}).round(2).reset_index()
        grouped_data= grouped_data[['Customer Name', 'Profit', 'Discount']].sort_values('Profit', ascending=False).head(10)

    return grouped_data



def create_grouped_proportions(data, columns):
    data = data[columns].copy()

    grouped_data = data.groupby(columns[0]).count().sort_values(columns[1], ascending=False).reset_index().rename(columns={columns[1]: 'Count'})
    grouped_data['Proportion'] = round((grouped_data['Count']/grouped_data['Count'].sum()) * 100, 2)

    return grouped_data



def create_grouped_proportions_bar(data, cols):
    data = data[cols].copy()
    grouped_data = data.groupby(cols[:2]).sum().reset_index()

    return grouped_data
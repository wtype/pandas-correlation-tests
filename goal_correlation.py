import pandas as pd

# import datasets
transactions18 = pd.read_csv('t2018.csv', delimiter = ',')
transactions19 = pd.read_csv('t2019.csv', delimiter = ',')

# group data by date
transactions_grouped_2018 = transactions18.groupby('Date').count()
transactions_grouped_2019 = transactions19.groupby('Date').count()

# isolate gross sales column - add .values for just data
gross_sales_2018 = transactions_grouped_2018.iloc[:, 3]
gross_sales_2019 = transactions_grouped_2019.iloc[:, 3]

# save new csv files with grouped data by day
transactions_grouped_2018.to_csv('transactions2018.csv')
transactions_grouped_2019.to_csv('transactions2019.csv')

# save isolated gross sales as csv
gross_sales_2018.to_csv('gross_sales_2018.csv')
gross_sales_2019.to_csv('gross_sales_2019.csv')


dataset = pd.read_csv('Main_Dataset.csv', delimiter = ',')

# correlation test gross sales and sessions
dataset['Sessions'].corr(dataset['Gross Sales (Square)'])
dataset['Sessions'].corr(dataset['Goal 1 Conversions'])
dataset['Gross Sales (Square)'].corr(dataset['Goal 1 Conversions'])

# correlate all set
correlation = dataset.corr()

pearson = dataset.corr(method='pearson') # mid
kendall = dataset.corr(method='kendall') # worst
spearman = dataset.corr(method='spearman') # best

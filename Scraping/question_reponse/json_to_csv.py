import pandas as pd

dataset=pd.read_csv('Scraping\question_reponse\data.csv')

# Rename the columns
dataset.columns = ['instruction', 'output']

# Add an empty 'input' column
dataset['input'] = ' '

# Reorder columns to match the desired order: instruction, input, output
dataset = dataset[['instruction', 'input', 'output']]
dataset.to_csv('dataset.csv',index=False)
import pandas as pd
import matplotlib.pyplot as plt
# Load the dataset
data = pd.read_csv('https://richardson.byu.edu/220/ds_salary.csv')
# Explore the variables
print(data.head())
print(data.info())

# Part 5- potential interactions between experience_level, company_size, and job_title

pivot_table = pd.pivot_table(data, values='salary_in_usd', index=['experience_level', 'company_size'], columns=['job_title'], aggfunc='mean')
print(pivot_table)

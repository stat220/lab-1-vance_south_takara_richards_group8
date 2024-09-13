import pandas as pd
import matplotlib.pyplot as plt
# Load the dataset
data = pd.read_csv('https://richardson.byu.edu/220/ds_salary.csv')
# Explore the variables
print(data.head())
print(data.info())

# Part 5- potential interactions between experience_level, company_size, and job_title

experience_size = pd.crosstab(data['experience_level'], data['company_size'], values=data['salary_in_usd'], aggfunc='mean')
title_experience = pd.crosstab(data['job_title'], data['experience_level'], values=data['salary_in_usd'], aggfunc='mean')
title_size = pd.crosstab(data['job_title'], data['company_size'], values=data['salary_in_usd'], aggfunc='mean')
print(experience_size)
print(title_experience)
print(title_size)

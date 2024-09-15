#imports
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


#data
data = pd.read_csv('ds_salary.csv')


"""
3. Impact of Company Size on Salary:

    Explore how company size affects data scientist salaries. Generate plots or tables to
    visualize this relationship.
"""


x = data['salary_in_usd'].values.reshape(-1, 1)
y = data['company_size'].values

plt.scatter(x, y, label="Scatterplot", )
plt.title("Company Size on Salary")
plt.ylabel("Company Size")
plt.xlabel("Salary (USD)")
plt.show()

#seems like larger company has higher max pay

grouped = data.groupby('company_size')['salary_in_usd'].apply(list)

small_arr = pd.Series(grouped.get('S', []))
medium_arr = pd.Series(grouped.get('M', []))
large_arr = pd.Series(grouped.get('L', []))

plt.hist(small_arr, bins=20)
plt.title("Salary Distribution for Small Companies")
plt.xlabel("Salary (USD)")
plt.xticks([0, 100000, 200000, 300000, 400000, 500000, 600000, 700000])
plt.ylabel("Frequency")
plt.show()

print("\nsmall company quartiles")
for i in range(5):
  print(f"{i/4} quantile: {small_arr.quantile(i/4)}")

plt.hist(medium_arr, bins=20)
plt.title("Salary Distribution for Medium Companies")
plt.xlabel("Salary (USD)")
plt.xticks([0, 100000, 200000, 300000, 400000, 500000, 600000, 700000])
plt.ylabel("Frequency")
plt.show()

print("\nmedium company quartiles")
for i in range(5):
  print(f"{i/4} quantile: {medium_arr.quantile(i/4)}")

plt.hist(large_arr, bins=20)
plt.title("Salary Distribution for Large Companies")
plt.xlabel("Salary (USD)")
plt.xticks([0, 100000, 200000, 300000, 400000, 500000, 600000, 700000])
plt.ylabel("Frequency")
plt.show()

print("\nlarge company quartiles")
for i in range(5):
  print(f"{i/4} quantile: {large_arr.quantile(i/4)}")


# The small company pays the least
# The medium company pays good
# The large company pays a little less than medium


"""
4. Job Title Analysis:

    Job titles can vary significantly. For this project, select a keyword or phrase to distinguish between different job titles. For instance, you can differentiate between job
    titles containing the word ”Analyst” and those that do not. To achieve this, you may
    find the str.contains function in Pandas helpful. Refer to this resource for examples:
    https://www.geeksforgeeks.org/python-pandas-series-str-contains. Explore
    various job titles to decide on the keyword or phrase you want to focus on.
"""

keyword = "Engineer"

contains_keyword = data['job_title'].str.contains(keyword)
with_keyword = data[contains_keyword]
without_keyword = data[~contains_keyword]

print(f"\ncontaining {keyword}: {len(with_keyword)}")
print(with_keyword['job_title'].head().to_list())

print(f"\nnot containing {keyword}: {len(without_keyword)}")
print(without_keyword['job_title'].head().to_list())

#seems like there are more non-engineers than engineers in general.
import pandas as pd
import matplotlib.pyplot as plt


# Top Ten Select and visualize 
df = pd.read_csv('NYC_Jobs.csv')
job_category_counts = df.groupby('Job Category')['Job ID'].count()
top_job_categories = job_category_counts.nlargest(10)
print(top_job_categories)
plt.barh(top_job_categories.index, top_job_categories.values)
plt.xlabel('Number of Listings')
plt.ylabel('Job Category')
plt.title('Top 10 NYC Job Categories by Number of Listings')
plt.yticks(fontsize=5)
plt.show()





# Top Ten Civil Service Titles based on Salary and visualize 
df = pd.read_csv('NYC_Jobs.csv')
df['Average Salary'] = (df['Salary Range From'] + df['Salary Range To']) / 2
job_salary_averages = df.groupby('Civil Service Title')['Average Salary'].mean().sort_values(ascending=False)
top_jobs = job_salary_averages.nlargest(10)
print(top_jobs)
plt.barh(top_jobs.index, top_jobs.values)
plt.xlabel('Average Salary')
plt.ylabel('Civil Service Title')
plt.yticks(fontsize=5)
plt.title('Top 10 NYC Jobs by Average Salary')
plt.show()

import pandas as pd
import matplotlib.pyplot as plt


# Top Job Categories by count of vaciences
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


# Engineering, Architecture, & Planning Details (EAP) & Career Level:
df = pd.read_csv('NYC_Jobs.csv')
eap = df[df['Job Category'] ==
         'Engineering, Architecture, & Planning']['Career Level'].value_counts()
print(eap)
eap.plot(kind='pie')
plt.title('Number of Career Levels in Engineering, Architecture, & Planning')
plt.xlabel('Career Level')
plt.ylabel('Count')
plt.show()


# Engineering, Architecture, & Planning Details (EAP) & Agency:
df = pd.read_csv('NYC_Jobs.csv')
eap_agency = df[df['Job Category'] ==
                'Engineering, Architecture, & Planning']['Agency'].value_counts()
print(eap_agency)
eap_agency.plot(kind='barh')
plt.title('Jobs per Agency in Engineering, Architecture, & Planning')
plt.xlabel('Count')
plt.xticks(fontsize=8)
plt.ylabel('Agency')
plt.show()


# Buiness Titles & under DEPT OF ENVIRONMENT PROTECTION
df = pd.read_csv('NYC_Jobs.csv')
eap_agency = df[df['Agency'] ==
                'DEPT OF ENVIRONMENT PROTECTION']['Business Title'].value_counts()
top = eap_agency.nlargest(10)
print(top)
top.plot(kind='barh')
plt.title('Business Titles in Dept Of Eviormental Protection')
plt.xlabel('Count')
plt.xticks(fontsize=8)
plt.ylabel('Business Title')
plt.show()

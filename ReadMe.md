# NYC Job Data Visualization

### Overview:

This project aims to achieve the follwing goals:

1. Determine the top job category in the NYC Jobs database. 

2. Filter the data by the top job category and gather information on the required level of experience.

3. Filter the data by the top job category and collect information on the agencies offering positions in that category.

4. Using the information from step 3, create a subset of the data by filtering for the top agency within the top job category, and extract information on the business titles within that agency.

5. Finally, determine the higest paying positions based on their business title

### The Data:
According to the City of New York's official jobs site, this dataset contains current job postings available on their website, including both internal postings available to city employees and external postings available to the general public. [1]

[1]: http://www.nyc.gov/html/careers/html/search/search.shtml
### Sample Output Goal 1:
| Job Category                                  | Count |
| --------------------------------------------- | ----- |
| Engineering, Architecture, & Planning         | 801   |
| Technology, Data & Innovation                 | 561   |
| Legal Affairs                                 | 432   |
| Building Operations & Maintenance             | 400   |
| Social Services                               | 345   |
| Administration & Human Resources              | 319   |
| Finance, Accounting, & Procurement            | 306   |
| Constituent Services & Community Programs     | 296   |
| Health                                        | 296   |
| Public Safety, Inspections, & Enforcement     | 270   |

![Figure 1](/assets/Top_10_By_Cat.png)

### Sample Output Goal 2:
#### For jobs under the 'job category' of 'Engineering, Architecture, & Planning'
| Experience Level        | Number of Listings |
|------------------------|--------------------|
| Experienced (non-manager) | 545               |
| Student                  | 84                 |
| Manager                  | 81                 |
| Entry-Level              | 81                 |
| Executive                | 10                 |

![Figure 2](/assets/Pie_EAP_Career_Level.png)


### Sample Output Goal 3:
#### For jobs under the 'job category' of 'Engineering, Architecture, & Planning'
| Agency                            | Count |
|----------------------------------|-------|
| DEPT OF ENVIRONMENT PROTECTION   | 337   |
| DEPARTMENT OF TRANSPORTATION     | 150   |
| DEPT OF DESIGN & CONSTRUCTION    | 139   |
| DEPT OF CITYWIDE ADMIN SVCS      | 42    |
| DEPARTMENT OF CITY PLANNING      | 37    |
| NYC HOUSING AUTHORITY            | 33    |
| DEPT OF PARKS & RECREATION       | 18    |
| DEPARTMENT OF BUILDINGS          | 14    |
| HOUSING PRESERVATION & DVLPMNT   | 10    |
| FIRE DEPARTMENT                  | 9     |
| OFFICE OF THE COMPTROLLER        | 4     |
| DEPT OF RECORDS & INFO SERVICE   | 2     |
| DEPT OF HEALTH/MENTAL HYGIENE    | 2     |
| POLICE DEPARTMENT                | 2     |
| PRESIDENT BOROUGH OF MANHATTAN   | 2     |

![Figure 3](/assets/EAP_Jobs_per_Agency.png)

### Sample Output Goal 4:
| Position                               | Count |
| -------------------------------------- | ------------------ |
| ACCOUNTABLE MANAGER                     | 82                 |
| Project Manager                         | 20                 |
| Assistant Counsel                       | 18                 |
| Assistant Civil Engineer                | 18                 |
| ASSISTANT PROJECT MANAGER               | 17                 |
| Assistant Process Engineer              | 12                 |
| Civil Engineering Intern                | 12                 |
| Emergency Management Specialist         | 10                 |
| Section Chief of Lifecycle Management   | 10                 |
| Assistant Mechanical Engineer           | 10                 |

![Figure 4](/assets/DEP_Biz_Titles.png)


### Sample Output Goal 5:

| Business Title                                            | Average Salary |
|-----------------------------------------------------------|----------------|
| Deputy Commissioner, Wastewater Treatment                 | $231,796       |
| Deputy Director of Management  Executive                  | $227,449       |
| Deputy Director  Executive                                | $227,449       |
| Deputy Commissioner, Energy Management                    | $213,783       |
| Senior Deputy Commissioner                                | $212,500       |
| Deputy Commissioner, Facilities & Fleet Administration    | $210,000       |
| Deputy Commissioner, Human Resources                      | $210,000       |
| Chief Technology Officer                                  | $210,000       |
| Deputy Comptroller, Public Finance                        | $205,000       |
| Assistant Commissioner, Facility Operations               | $201,587       |

![Figure 5](/assets/Top_10_vs_Salary.png)
--- 

### Conclusion 
#### Baed on [NYC Job Data ](https://data.cityofnewyork.us/City-Government/NYC-Jobs/kpav-sd4t/explore/query/SELECT%0A%20%20%60job_id%60%2C%0A%20%20%60agency%60%2C%0A%20%20%60posting_type%60%2C%0A%20%20%60number_of_positions%60%2C%0A%20%20%60business_title%60%2C%0A%20%20%60civil_service_title%60%2C%0A%20%20%60title_classification%60%2C%0A%20%20%60title_code_no%60%2C%0A%20%20%60level%60%2C%0A%20%20%60job_category%60%2C%0A%20%20%60full_time_part_time_indicator%60%2C%0A%20%20%60career_level%60%2C%0A%20%20%60salary_range_from%60%2C%0A%20%20%60salary_range_to%60%2C%0A%20%20%60salary_frequency%60%2C%0A%20%20%60work_location%60%2C%0A%20%20%60division_work_unit%60%2C%0A%20%20%60job_description%60%2C%0A%20%20%60minimum_qual_requirements%60%2C%0A%20%20%60preferred_skills%60%2C%0A%20%20%60additional_information%60%2C%0A%20%20%60to_apply%60%2C%0A%20%20%60hours_shift%60%2C%0A%20%20%60work_location_1%60%2C%0A%20%20%60recruitment_contact%60%2C%0A%20%20%60residency_requirement%60%2C%0A%20%20%60posting_date%60%2C%0A%20%20%60post_until%60%2C%0A%20%20%60posting_updated%60%2C%0A%20%20%60process_date%60/page/filter):

1. Engineering, Architecture, and Planning is the most in demand job category with 801 vacancies, followed by Technology, Data & Innovation with 561 vacancies, and Legal Affairs with 432 vacancies.
2.  Focusing on listings under the job category of 'Engineering, Architecture, and Planning' the most common experience level for these jobs is Experienced (non-manager) with 545 listings. This is followed by Student with 84 listings, Manager with 81 listings, and Entry-Level with 81 listings. Executive is the least common experience level with only 10 listings.

3. Continuing under the job category of 'Engineering, Architecture, and Planning', the Department of Environmental Protection (DEP) has the highest number of job listings with 337, followed by the Department of Transportation with 150 listings, and the Department of Design & Construction with 139 listings. The Department of Citywide Administrative Services and the Department of City Planning round out the top five agencies with 42 and 37 listings, respectively.  

4. The job title with the most vacancies under the 'Agency' of Department of Environmental Protection (DEP) is Accountable Manager with 82 employees, followed by Project Manager with 20 employees, Assistant Counsel, and Assistant Civil Engineer both with 18 employees. The fifth most common job title is Assistant Project Manager with 17 employees. 

5. The highest-paying business title listed on the City of New York's official jobs site is Deputy Commissioner of Wastewater Treatment, with an average salary of $231,796. The next highest-paying business titles are Deputy Director of Management Executive and Deputy Director Executive, both with an average salary of $227,449. Other high-paying titles include Deputy Commissioner of Energy Management, Senior Deputy Commissioner, and Deputy Commissioner of Facilities & Fleet Administration.

- This information can help job seekers in the engineering, architecture, and planning field to better understand the job market and identify the types of positions that are most in demand. The City of New York can also use this data to tailor their job postings and recruitment efforts. Overall, this analysis can help to inform human resources and talent management strategies for companies operating in this industry.

### Getting Started:
1. Downlaoad the [NYC Job Data ](https://data.cityofnewyork.us/City-Government/NYC-Jobs/kpav-sd4t/explore/query/SELECT%0A%20%20%60job_id%60%2C%0A%20%20%60agency%60%2C%0A%20%20%60posting_type%60%2C%0A%20%20%60number_of_positions%60%2C%0A%20%20%60business_title%60%2C%0A%20%20%60civil_service_title%60%2C%0A%20%20%60title_classification%60%2C%0A%20%20%60title_code_no%60%2C%0A%20%20%60level%60%2C%0A%20%20%60job_category%60%2C%0A%20%20%60full_time_part_time_indicator%60%2C%0A%20%20%60career_level%60%2C%0A%20%20%60salary_range_from%60%2C%0A%20%20%60salary_range_to%60%2C%0A%20%20%60salary_frequency%60%2C%0A%20%20%60work_location%60%2C%0A%20%20%60division_work_unit%60%2C%0A%20%20%60job_description%60%2C%0A%20%20%60minimum_qual_requirements%60%2C%0A%20%20%60preferred_skills%60%2C%0A%20%20%60additional_information%60%2C%0A%20%20%60to_apply%60%2C%0A%20%20%60hours_shift%60%2C%0A%20%20%60work_location_1%60%2C%0A%20%20%60recruitment_contact%60%2C%0A%20%20%60residency_requirement%60%2C%0A%20%20%60posting_date%60%2C%0A%20%20%60post_until%60%2C%0A%20%20%60posting_updated%60%2C%0A%20%20%60process_date%60/page/filter) and save it as 'NYC_Job.csv'
3. Navigate to this [Github repository](https://github.com/jozkan30/NYC_job_data-) and fork or clone.
4. Ensure you have Python installed from the offical website.
5. Install Pandas by running `` pip install pandas ``
6. Install Matplotlib by running  `pip install matplotlib`
7. Run:  `` python3 main.py ``

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def shorten_categories (categories, cutoff):
    categorical_map = {}
    for i in range(len(categories)):
        if categories.values[i] >= cutoff:
            categorical_map[categories.index[i]] = categories.index[i]
        else:
            categorical_map[categories.index[i]] ='other'
    return categorical_map
def shorten_categories (categories, cutoff):
    categorical_map = {}
    for i in range(len(categories)):
        if categories.values[i] >= cutoff:
            categorical_map[categories.index[i]] = categories.index[i]
        else:
            categorical_map[categories.index[i]] ='other'
    return categorical_map


# def clean_education (x):
#        if  "Bachelor's Degree" in x:
#         return  "Bachelor's Degree"
#        if "Master's Degree" in x:
#          return "Master's Degree"
#        if 'PhD'in x:
#             return 'PhD'
#        else:
#             return 'less than a Bachelors'

# @st.cache
# def  load_data(): 
#       df = pd.read_csv("Levels_Fyi_Salary_Data.csv")  
#       salary_df = df[['company','title','totalyearlycompensation','location','yearsofexperience','yearsatcompany','basesalary','Education']]
#       salary_df= salary_df['totalyearlycompensation'] +salary_df['basesalary']
#       salary_df1 = salary_df.copy()
#       salary_new1 = salary_df1.dropna(how = 'any')
#       df_salary =salary_new1.copy()
#       location_map = shorten_categories(df_salary.Location.value_counts(),400 )
#       df_salary['Location'] = df_salary['Location'].map(location_map)
#       df_salary = df_salary[df_salary["total_salary"] <= 1000000]
#       df_salary= df_salary[df_salary["total_salary"] >= 10000]
#       df_salary= df_salary[df_salary['Location'] != 'other']
#       company_map = shorten_categories(df_salary.company.value_counts(),400 )
#       df_salary['Company'] = df_salary['company'].map(company_map)
#       df_salary = df_salary[df_salary["total_salary"] <= 1000000]
#       df_salary= df_salary[df_salary["total_salary"] >= 40000]
#       df_salary = df_salary[df_salary['Company'] != 'other']
#       df_salary['Education'] =df_salary['Education'].apply(clean_education)


#       return df_salary

# df_salary = load_data()

def show_explore_page():
    st.title("Explore STEM Salaries in Top Tech Firm")

# data = df_salary["company"].value_counts()
# fig1, ax1 = plt.subplots()
# ax1.pie(data, label = data.index, autopct="%1.1f%%", shadow=True,startangle=90)
# ax1.axis("equal")
# st.write("""#### Number of Salary Data From Different Companies""")
# st.pyplot(fig1)






    
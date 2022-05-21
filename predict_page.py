import streamlit as st
import pickle
import numpy as np

def load_model():
    with open('saved_steps.pkl', "rb") as file:
        data = pickle.load(file)
    return data

data = load_model()

regressor = data["model"]
le_title = data["le_title"]
le_education = data["le_education"]
le_Location =data["le_Location"]
le_company = data["le_company"]

def show_predict_page():
    st.title("STEM SALARY PREDICTION  OF TOP TECH COMPANIES")

    st.write("""### We need some information to predict the salary""")

    Location = (
        "Seattle, WA",
        "San Francisco",
        "New York, NY",                
        "Redmond, WA",                   
        "San Jose, CA",                  
        "Mountain View, CA",               
        "Sunnyvale, CA",                   
        "Austin, TX",                     
        "Bangalore, KA, India",            
        "Menlo Park, CA",                  
        "Cupertino, CA",                  
        "Santa Clara, CA",                 
        "London, EN, United Kingdom",      
        "Boston, MA",                      
        "Palo Alto, CA",                   
        "Toronto, ON, Canada",             
        "Chicago, IL",              
    )

    company = (
       "Amazon",       
       "Microsoft",     
       "Google",        
       "Facebook",      
       "Apple",
    ) 

    title =(
        "Product Manager",
        "Software Engineer",
        "Software Engineering Manager",
        "Data Scientist",
        "Solution Architect",
        "Technical Program Manager",
        "Human Resources",
        "Product Designer",
        "Marketing",
        "Business Analyst",
        "Hardware Engineer",
        "Sales",
        "Recuriter",
        "Mechanical Engineer",
        "Management Consultant",

    ) 

    education = (
        "PhD",
        "Master's Degree",
        "Bachelor's Degree",
        "less than a Bachelors",
    )

    title = st.selectbox("Job Title",title)
    education = st.selectbox("Education", education)
    company = st.selectbox("Company",company)
    Location =st.selectbox("Region", Location)

    working_experience_years = st.slider("Experience",0,50,0)
    yearsatcompany = st.slider("CompanyExperience",0,100, 0)


    ok =st.button('Calculate Salary')
    if ok:
        Features= np.array([[title, education, company, Location, working_experience_years, yearsatcompany]])
        Features[:,0]=le_title.transform(Features[:,0])
        Features[:,1]=le_education.transform(Features[:,1])
        Features[:,2]=le_company.transform(Features[:,2])
        Features[:,3]=le_Location.transform(Features[:,3])
        Features = Features.astype(float)
        
       # Salary=regressor.predict(Features)
        #st.subheader(f'The estimated salary is ${Salary[0]:,.2f}')
        

        total_salary = regressor.predict(Features)
        st.subheader(f"Something hoooge in ${total_salary[0]:,.2f}!") # .2f means 2 decimal value and [0] means the first value in the numpy

    



       



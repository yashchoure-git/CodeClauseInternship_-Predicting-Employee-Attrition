import streamlit as st
import pickle
import numpy as np      


model_path="C:\\Users\\DELL\\Downloads\\Predicting Employee Attrition (1).pkl"
model=pickle.load(open(model_path,"rb"))

st.image("https://www.logomaker.com/api/main/images/1j_ojFVGOMkX9W_reBe4hGfc07bc814azQW8k3opM3QQqlF38GJ40qs4saJ5PEEC7EdX2kACcME9jy17VIESmlo8qzKNL9UWHHN...2G9aDqhCTn0odBDXH...aUr0g43eZowMAejk...GUiToTSCEPMIjItGX5K9iEtMKi2DeJyc8tE1...S7QDMMrQA4U1hZeheP9N4HCWSA--")

st.title(":green[Employee Attrition Predictor]")

st.header(":green[______________________________________]")


Age=st.slider("**Fix Age of Employee**",0,60)
Department=st.selectbox("Department of Employee",[' ','Sales','IT','Finance','Operations','HR'])

JobRole=st.selectbox("Job Role Of Employee",['','Manager', 'Sales Rep', 'Executive', 'Engineer', 'Analyst'])
MonthlyIncome=st.number_input('Monthly Income of Employee',0,1000000)

if st.button("Predict Attrition"):
    stuff=np.array([Age,Department,JobRole,MonthlyIncome]).reshape(1,-1)
    
    model.predict(stuff)[0]

import numpy as np
import pickle
import pandas as pd
#from flasgger import Swagger
import streamlit as st 



pickle_in = open("classifier.pkl","rb")
classifier=pickle.load(pickle_in)

def welcome():
    return "Welcome All"

#@app.route('/predict',methods=["Get"])
def predict_note_authentication(Total_Amt_Chng_Q4_Q1, Total_Trans_Amt, Total_Trans_Ct,Total_Ct_Chng_Q4_Q1, Avg_Utilization_Ratio):
    
    """Let's Authenticate the Banks Note 
    This is using docstrings for specifications.
    ---
    parameters:  
      - name: variance
        in: query
        type: number
        required: true
      - name: skewness
        in: query
        type: number
        required: true
      - name: curtosis
        in: query
        type: number
        required: true
      - name: entropy
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values
        
    """
   
    prediction=classifier.predict([[Total_Amt_Chng_Q4_Q1, Total_Trans_Amt, Total_Trans_Ct,Total_Ct_Chng_Q4_Q1, Avg_Utilization_Ratio]])
    print(prediction)
    return prediction



def main():
    st.title("Bank Customer Churn Prediction")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Bank Customer Churn Prediction ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    Total_Amt_Chng_Q4_Q1 = st.text_input("Total_Amt_Chng_Q4_Q1")
    Total_Trans_Amt = st.text_input("Total_Trans_Amt")
    Total_Trans_Ct = st.text_input("Total_Trans_Ct")
    Total_Ct_Chng_Q4_Q1 = st.text_input("Total_Ct_Chng_Q4_Q1")
    Avg_Utilization_Ratio = st.text_input("Avg_Utilization_Ratio")
    result=""
    if st.button("Predict"):
        result=predict_note_authentication(Total_Amt_Chng_Q4_Q1, Total_Trans_Amt, Total_Trans_Ct,Total_Ct_Chng_Q4_Q1, Avg_Utilization_Ratio)
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Project Guide :-   Dr.Ashwini Patil Mam")
        st.text("Project Members -:  1.Vaishnavi Rajput  2.Purva Rane  3.Rajesh Rampure  4.Venktesh Ranvirkar")

if __name__=='__main__':
    main()
    

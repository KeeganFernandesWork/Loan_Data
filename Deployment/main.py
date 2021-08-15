import streamlit as st
import pandas as pd
import pickle


st.markdown("""#Loan Qualification""")
progress = st.progress(0)
model = pickle.load(open("Model_For_Deployment.sav","rb"))
features = []

features.append(st.text_input(label = "Interest Rate" , value = 0.5))#
features.append(st.text_input(label = "Installment : The monthly installments owed by the borrower if the loan is funded" , value = 100))
features.append(st.text_input(label = "Log.Annual.Inc: The natural log of the self-reported annual income of the borrower." , value = 10))
features.append(st.text_input(label = "DTI: The debt-to-income ratio of the borrower (amount of debt divided by annual income)." , value = 0.5))
features.append(st.text_input(label = "FICO :" , value = 500))
features.append(st.text_input(label = "Days.with.cr.line : The number of days the borrower has had a credit line." , value = 1000))
features.append(st.text_input(label = "Revol.bal: The borrower's revolving balance (amount unpaid at the end of the credit card billing cycle)" , value = 5))
features.append(st.text_input(label = "Revol.util: The borrower's revolving line utilization rate (the amount of the credit line used relative to total credit available)" , value = 5))
features.append(st.text_input(label = " The borrower's number of inquiries by creditors in the last 6 months" , value = 5))
features.append(st.text_input(label = "The number of times the borrower had been 30+ days past due on a payment in the past 2 years." , value = 0))
features.append(st.text_input(label = "The borrower's number of derogatory public records (bankruptcy filings, tax liens, or judgments)" , value = 0))

X = pd.DataFrame({
    "1" : [features[0]],
    "2" : [features[1]],
    "3" : [features[2]],
    "4" : [features[3]],
    "5" : [features[4]],
    "6" : [features[5]],
    "7" : [features[6]],
    "8" : [features[7]],
    "9" : [features[8]],
    "10" : [features[9]],
    "11" : [features[10]],
})
progress.progress(100)
if st.button("Submit"):
    prediction = model.predict(X)[0]
    if prediction == 0:
        st.warning("Sorry you won't be able to acquire a loan")
    else:
        st.success("Congratulations!! You are eligible for a loan.")

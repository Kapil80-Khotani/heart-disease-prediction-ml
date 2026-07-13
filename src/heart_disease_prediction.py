import numpy as np
import streamlit as st
import pickle

loaded_model = pickle.load(open('models/trained_model.sav', 'rb'))

def heart_disease_prediction(input_data):
    input_data_as_numpy_array = np.asarray(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

    prediction = loaded_model.predict(input_data_reshaped)

    if(prediction[0] == 0):
        return 'The person has no heart disease'
    else:
        return 'The person has heart disease'
    

def main():

    st.title('Welcome to Heart Disease Diagnosis')

    age = st.number_input("Age")
    sex = st.selectbox("Sex (0->Female | 1->Male)",[0,1])

    trestbps = st.number_input("Resting Blood Pressure (mm Hg)")
    chol = st.number_input("Serum Cholesterol (mg/dl)")
    
    fbs = st.selectbox("Fasting Blood Sugar >120 mg/dl",[0,1])
    thalach = st.number_input("Maximum Heart Rate Achieved")

    exang = st.selectbox("Exercise Induced Angina",[0,1])
    oldpeak = st.number_input("Oldpeak",format="%.1f")

    

    slope = st.number_input("Slope",min_value=0,max_value=2)
    ca = st.number_input("Number of Major Vessels",min_value=0,max_value=4,value=0)

    cp_1 = st.selectbox("CP_1", [0, 1])
    cp_2 = st.selectbox("CP_2", [0, 1])
    cp_3 = st.selectbox("CP_3", [0, 1])

    restecg_1 = st.selectbox("Rest ECG_1", [0, 1])
    restecg_2 = st.selectbox("Rest ECG_2", [0, 1])

    thal_1 = st.selectbox("Thal_1", [0, 1])
    thal_2 = st.selectbox("Thal_2", [0, 1])
    thal_3 = st.selectbox("Thal_3", [0, 1])

    diagnosis = ''

    if st.button('Heart Test Result'):
        diagnosis = heart_disease_prediction([age,sex,trestbps,chol,fbs,thalach,exang,oldpeak,
                                              slope,ca,
                                              cp_1,cp_2,cp_3,
                                              restecg_1,restecg_2,
                                              thal_1,thal_2,thal_3])
        
        st.success(diagnosis)


if __name__ == '__main__':
    main()
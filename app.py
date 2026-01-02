# Mason Boyd - 4th period AP CSP
# Exam calculator

import streamlit as st

st.title("Semester Exam Grade Calculator")

# Function to calculate grade needed
def calc_grade(Q1_grade, Q2_grade, Q_weight, exam_weight, desired_s_grade):
    current_grade = (Q1_grade * Q_weight) + (Q2_grade * Q_weight)
    needed_exam_grade = (desired_s_grade - current_grade) / exam_weight
    return needed_exam_grade

# Get user inputs
Q1_grade = st.number_input("What is your first quarter grade?: ", min_value=0.0, max_value=100.0)
Q2_grade = st.number_input("What is your second quarter grade?: ", min_value=0.0, max_value=100.0)
Q_weight = st.number_input("How much are each of those worth? (i.e 0.20 = 20%): ", min_value=0.0, max_value=1.0, step=0.01)
exam_weight = st.number_input("How much is your exam worth? (i.e 0.20 = 20%): ", min_value=0.0, max_value=1.0, step=0.01)
desired_s_grade = st.number_input("What is your desired semester grade?: ", min_value=0.0, max_value=100.0)

# Button to calculate
if st.button("Calculate Needed Exam Grade"):
    exam_grade = calc_grade(Q1_grade, Q2_grade, Q_weight, exam_weight, desired_s_grade)
    st.write(f"Here is the grade you need on your exam to get a {desired_s_grade} in the class: **{round(exam_grade, 2)}**")

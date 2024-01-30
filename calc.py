import streamlit as st
import numpy as np

# Function to calculate the financials
def calculate_financials(start_year, monthly_income, monthly_expenses, salary_increment, expenses_increment, return_percentage):
    year = start_year
    total_savings = 0
    runway = 0

    while monthly_income > monthly_expenses:
        yearly_saving = (monthly_income - monthly_expenses) * 12
        total_savings += yearly_saving
        monthly_income *= (1 + salary_increment)
        monthly_expenses *= (1 + expenses_increment)
        runway += 1

    invested_savings = total_savings * ((1 + return_percentage) ** runway)
    extra_returns = invested_savings - total_savings

    return runway, invested_savings, extra_returns, total_savings

# Streamlit UI
st.title('Financial Projection Calculator')

start_year = st.number_input('Started Working Year', min_value=2000, max_value=2024, value=2018)
monthly_income = st.number_input('Monthly Income', value=21000)
monthly_expenses = st.number_input('Monthly Expenses', value=18000)
salary_increment = st.slider('Salary Increment (%)', 0, 100, 10) / 100
expenses_increment = st.slider('Expenses Increment (%)', 0, 100, 8) / 100
return_percentage = st.slider('Return Percentage (%)', 0, 100, 3) / 100

if st.button('Calculate'):
    runway, savings_after_investment, extra_returns, savings_without_investment = calculate_financials(
        start_year, monthly_income, monthly_expenses, salary_increment, expenses_increment, return_percentage
    )

    st.write(f'Total Runway: {runway} years')
    st.write(f'Total Saving after investment: ₹ {savings_after_investment:,.0f}')
    st.write(f'Extra returns, if investment is made: ₹ {extra_returns:,.0f}')
    st.write(f'Saving without investment: ₹ {savings_without_investment:,.0f}')


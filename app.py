import streamlit as st
import pandas as pd
import plotly.express as px

# Set page configuration
st.set_page_config(page_title="My Interactive Chart", layout="wide")

# Create sample data (you can replace this with your own data)
data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    'Sales': [1200, 1900, 1500, 2100, 1800, 2400],
    'Expenses': [1000, 1200, 900, 1400, 1100, 1800]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Create title
st.title("Monthly Sales and Expenses")

# Create interactive chart
fig = px.line(df, x='Month', y=['Sales', 'Expenses'],
              title='Sales vs Expenses Over Time',
              labels={'value': 'Amount ($)', 'variable': 'Category'},
              height=500)

# Add interactive features
fig.update_traces(mode='lines+markers')
fig.update_layout(hovermode='x unified')

# Display the chart
st.plotly_chart(fig, use_container_width=True)

# Add interactive filters
st.sidebar.header("Filters")
min_value = st.sidebar.number_input("Minimum Value", min_value=0, max_value=5000, value=0)
max_value = st.sidebar.number_input("Maximum Value", min_value=0, max_value=5000, value=3000)

# Update chart based on filters
fig.update_layout(yaxis_range=[min_value, max_value])
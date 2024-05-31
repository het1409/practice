import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import time

# Load the CSV data into a DataFrame
df = pd.read_csv('sample.csv')

# Create a bar plot using matplotlib
fig, ax = plt.subplots(figsize=(10, 5))
ax.bar(df['name'], df['sodium'], color='#3CA99F')

# Create a line plot using matplotlib
fig2, ax2 = plt.subplots(figsize=(10, 5))
ax2.plot(df['name'], df['calories'], color='#aa001f')


# Streamlit App
st.title('First App')

# Display the DataFrame
st.write(df)

# Highlight the maximum values in the DataFrame
st.write(df.style.highlight_max(axis=0, color = '#3CA99F').highlight_min(axis=0, color = '#ff4444'))

# add_selectbox = st.sidebar.selectbox(
#     'What tyoe of risk do you want to calculate?',
#     ('Health Risk', 'Insurance Quotation')
# )

# add_slider = st.sidebar.slider(
#     'Select a range of age',
#     15, 75, (25, 75)
# )
'Calculating the insurance...'
latest_iteartion = st.empty()
bar = st.progress(0)
for i in range(100):
    latest_iteartion.text(f'Iteration {i + 1}')
    bar.progress(i + 1)
    time.sleep(0.1)

'...And its calculated'
    
# Create a bar chart using Streamlit's built-in bar_chart method
st.bar_chart(df.set_index('name')['sodium'])


# Create a line chart using Streamlit's built-in line_chart method
st.line_chart(df.set_index('name')['calories'])


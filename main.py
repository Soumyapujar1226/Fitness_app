import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title and sidebar
st.title('Fitness Tracker App')

# Sidebar for user input
st.sidebar.header('User Input')
exercise_name = st.sidebar.text_input('Enter Exercise Name')
exercise_duration = st.sidebar.number_input('Exercise Duration (minutes)')
exercise_date = st.sidebar.date_input('Date')

# Store user input in a Pandas DataFrame
data = {'Exercise Name': [exercise_name],
        'Duration (min)': [exercise_duration],
        'Date': [exercise_date]}
df = pd.DataFrame(data)

# Display workout history
st.header('Workout History')
if 'workout_data' not in st.session_state:
    st.session_state.workout_data = pd.DataFrame()

if st.sidebar.button('Add Workout'):
    st.session_state.workout_data = pd.concat([st.session_state.workout_data, df], ignore_index=True)

st.write(st.session_state.workout_data)

# Fitness goals
st.header('Fitness Goals')
goal_duration = st.sidebar.number_input('Set Exercise Duration Goal (minutes)')
current_total_duration = st.session_state.workout_data['Duration (min)'].sum()
progress_percentage = (current_total_duration / goal_duration) * 100 if goal_duration != 0 else 0

st.write(f'Current Total Duration: {current_total_duration} minutes')
st.write(f'Goal Duration: {goal_duration} minutes')
st.write(f'Progress: {progress_percentage:.2f}%')

# Visualization
st.header('Fitness Statistics')
if st.sidebar.button('Visualize Data'):
    if not st.session_state.workout_data.empty:
        plt.figure(figsize=(8, 6))
        df['Date'] = pd.to_datetime(df['Date'])
        df.set_index('Date', inplace=True)
        df.resample('D').sum().plot(kind='bar', title='Workout Duration Over Time')
        st.pyplot()


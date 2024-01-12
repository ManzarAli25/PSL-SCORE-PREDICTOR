import streamlit as st
import pickle 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import base64


st.markdown(
    """
    <style>
    .reportview-container {
        background: url("background.jpeg")
    }
   .sidebar .sidebar-content {
        background: url("url_goes_here")
    }
    </style>
    """,
    unsafe_allow_html=True
)
# st.markdown("<h1 style='color:#ccff66; text-align: center; font-weight: bold;'>🏏 CricEx - PSL Score Predictor</h1>", unsafe_allow_html=True)
st.image("logo.jpeg")
# st.markdown("<h3 style='color:white; text-align: center;'>Turning Chai Conversations into Cricket Oracle Moments!</h3>", unsafe_allow_html=True)

matches = pickle.load(open('dataset_level1.pkl','rb'))
first_inning_batters = pickle.load(open('first_inning_batters.pkl','rb'))
second_inning_batters = pickle.load(open('second_inning_batters.pkl','rb'))
first_inning = pickle.load(open('first_innings.pkl','rb'))
second_inning = pickle.load(open('second_innings.pkl','rb'))
model = pickle.load(open('pipev2.pkl','rb'))
teams = ['Islamabad United',
'Karachi Kings',
'Lahore Qalandars'
,'Multan Sultans',
'Peshawar Zalmi',
'Quetta Gladiators']

cities = ['Lahore', 'Abu Dhabi', 'Karachi', 'Sharjah', 'Dubai', 'Rawalpindi',
       'Multan']

winner_counts = matches['info.outcome.winner'].value_counts()
number_of_wins = {}
for team in winner_counts.index:
    number_of_wins[team] = winner_counts[team]

st.sidebar.markdown("<h1>Pakistan Super League General Insights.</h1>", unsafe_allow_html=True)
opt = st.sidebar.radio("",options=("Tournament History","1st Innings Records","2nd Innings Records","Prediction Model"))

if opt =="Tournament History":
    # Plotting the number of wins for each team in Streamlit
    st.bar_chart(number_of_wins, color = "#66ff66")
    st.markdown("<p style='color:white; text-align: center;'><b>Number of Wins</b></p>", unsafe_allow_html=True)

    data = {
        'WINNER': ['Islamabad United', 'Lahore Qalandars', 'Peshawar Zalmi', 'Quetta Gladiators', 'Karachi Kings', 'Multan Sultans'],
        'VICTORIES': [2, 2, 1, 1, 1, 1],
        'WINNER YEAR': ['2016, 2018', '2022', '2017', '2019', '2020', '2021']
    }

    # Create a DataFrame
    df = pd.DataFrame(data)

    # Display the table
    st.table(df)
    st.markdown("<p style='color:white; text-align: center;'><b>Trophies Each Team has Won. </b></p>", unsafe_allow_html=True)

    data_summary = {
        'Teams': ['Multan Sultans', 'Islamabad United', 'Peshawar Zalmi', 'Quetta Gladiators', 'Lahore Qalandars', 'Karachi Kings'],
        'Span': ['2018–present', '2016–present', '2016–present', '2016–present', '2016–present', '2016–present'],
        'Mat': [67, 88, 93, 82, 85, 85],
        'Won': [37, 47, 49, 39, 39, 32],
        'Lost': [27, 40, 42, 42, 43, 49],
        'Tie&W': [0, 1, 1, 0, 1, 1],
        'Tie&L': [1, 0, 0, 0, 2, 1],
        'NR': [2, 0, 1, 1, 0, 2],
        'Win%': [57.69, 53.97, 53.8, 48.14, 47.64, 39.75],
    }

    # Create a DataFrame
    df_summary = pd.DataFrame(data_summary)

    # Display the table
    st.table(df_summary)
    st.markdown("<p style='color:white; text-align: center;'><b>Result Summary </b></p>", unsafe_allow_html=True)
    data_summary = {
    'Teams': ['Multan Sultans', 'Islamabad United', 'Peshawar Zalmi', 'Quetta Gladiators', 'Lahore Qalandars', 'Karachi Kings'],
    'Win%': [57.69, 53.97, 53.8, 48.14, 47.64, 39.75]}


if opt =="1st Innings Records":
    iu_df = first_inning[first_inning['batting_team'] == 'Islamabad United']
    kk_df = first_inning[first_inning['batting_team'] == 'Karachi Kings']
    lq_df = first_inning[first_inning['batting_team'] == 'Lahore Qalandars']
    qg_df = first_inning[first_inning['batting_team'] == 'Quetta Gladiators']
    pz_df = first_inning[first_inning['batting_team'] == 'Peshawar Zalmi']
    ms_df = first_inning[first_inning['batting_team'] == 'Multan Sultans']


    col1 , col2 = st.columns(2)
    with col1:
        st.line_chart(ms_df['total_score'],color = "#00cc99")
        st.write("Multan Sultan")
    with col2:
        st.line_chart(lq_df['total_score'],color = "#66ff33")
        st.write("Lahore Qalandars")

    col3 , col4 = st.columns(2)
    with col3:
        st.line_chart(iu_df['total_score'],color = "#e62e00")
        st.write("Islamabad United")
    with col4:
        st.line_chart(kk_df['total_score'],color = "#0033cc")
        st.write("Karachi Kings")
    col5 , col6 = st.columns(2)
    with col5:
        st.line_chart(pz_df['total_score'],color = "#ffcc00")
        st.write("Peshawar Zalmi")
    with col6:
        st.line_chart(qg_df['total_score'],color = "#1f1f7a")
        st.write("Quetta Gladiators")

    st.write("1st Innings Scores of Each Team.")





    top_n = 10  # You can adjust this based on your preference
    top_batsmen = first_inning_batters.nlargest(top_n, 'total_runs')

    st.bar_chart(first_inning_batters.set_index('batsman')['total_runs'])



if opt =="2nd Innings Records":
    iu_df = second_inning[second_inning['batting_team'] == 'Islamabad United']
    kk_df = second_inning[second_inning['batting_team'] == 'Karachi Kings']
    lq_df = second_inning[second_inning['batting_team'] == 'Lahore Qalandars']
    qg_df = second_inning[second_inning['batting_team'] == 'Quetta Gladiators']
    pz_df = second_inning[second_inning['batting_team'] == 'Peshawar Zalmi']
    ms_df = second_inning[second_inning['batting_team'] == 'Multan Sultans']


    col1 , col2 = st.columns(2)
    with col1:
        st.line_chart(ms_df['total_score'],color = "#00cc99")
        st.write("Multan Sultan")
    with col2:
        st.line_chart(lq_df['total_score'],color = "#66ff33")
        st.write("Lahore Qalandars")

    col3 , col4 = st.columns(2)
    with col3:
        st.line_chart(iu_df['total_score'],color = "#e62e00")
        st.write("Islamabad United")
    with col4:
        st.line_chart(kk_df['total_score'],color = "#0033cc")
        st.write("Karachi Kings")
    col5 , col6 = st.columns(2)
    with col5:
        st.line_chart(pz_df['total_score'],color = "#ffcc00")
        st.write("Peshawar Zalmi")
    with col6:
        st.line_chart(qg_df['total_score'],color = "#1f1f7a")
        st.write("Quetta Gladiators")

    st.write("2nd Innings Score trends of Each Team.")





    top_n = 10  # You can adjust this based on your preference
    top_batsmen = second_inning_batters.nlargest(top_n, 'total_runs')

    st.bar_chart(second_inning_batters.set_index('batsman')['total_runs'])




if opt =="Prediction Model":
    col1 , col2 = st.columns(2)
    with col1:
        bat = st.selectbox('SELECT BATTING TEAM',sorted(teams))
    with col2:
        bowl = st.selectbox('SELECT BOWLING TEAM',sorted(teams))
    city = st.selectbox('SELECT THE CITY', sorted(cities))
    col3,col4,col5, col6 = st.columns(4)
    with col3:
        current_score = st.number_input('CURRENT SCORE')
        
    with col4:
        overs =  st.number_input('OVERS DONE')
        

    with col5:
        wickets = st.number_input('WICKET OUT')
    with col6:
        innings = st.selectbox('CURRENT INNINGS',['1st','2nd'])
    last_five = st.number_input('RUNS IN LAST 5 OVERS')
    
    if st.button('PREDICT SCORE'):
        if current_score < last_five:
            st.error('Error: Current score should always be greater than or equal to thescore in last 5 overs.')
        elif overs < 5:
            st.error('Error: Overs must be 5 or more. Please enter a valid value.')
        else:
            balls_left = 120 - (overs*6)
            wicket_left = 10 - wickets
            crr = current_score/overs
            
            data = {
        'batting_team': [bat],
        'bowling_team': [bowl],
        'city': [city],
        'current_score': [current_score],
        'balls_left': [balls_left],
        'wickets_left': [wicket_left],
        'crr': [crr],
        'last_five': [last_five],
        'innings':[innings]
            }


            input_df = pd .DataFrame(data)
            result = model.predict(input_df)

            result_text = "I think the total Score of " + str(bat) + " will be somewhere around " + str(int(result[0]))

            # Use st.markdown with text-align CSS property to centerize the text
            st.markdown(f'<h3 style="text-align: center;">{result_text}</h3>', unsafe_allow_html=True)


            st.image("output.jpeg")

          
    
    


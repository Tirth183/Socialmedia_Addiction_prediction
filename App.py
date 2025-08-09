import streamlit as st
import pickle
import pandas as pd


def load_model(model_name):
    with open(f'{model_name}_model.pkl', 'rb') as file:
        model = pickle.load(file)
    return model


page_bg = '''
<style>
body {
    background: linear-gradient(135deg, #FFD700, #FFFFFF); /* Gold to White gradient */
    color: #333;
}
h1 {
    color: #d00000;
    text-align: center;
    font-family: 'Arial';
    font-size: 3em;
    padding: 20px;
}
.stButton>button {
    color: white;
    background-color: #d00000;
    border-radius: 12px;
    padding: 10px 24px;
    font-size: 16px;
}
.sidebar .sidebar-content {
    background-color: #FFD700; /* Gold for sidebar */
    color: white;
}
</style>
'''


st.markdown(page_bg, unsafe_allow_html=True)


st.markdown("<h1>🧠 Addiction Level Prediction App 🔮</h1>", unsafe_allow_html=True)


st.sidebar.markdown('<h2 style="color:white;text-align:center;">🔍 Choose a Model</h2>', unsafe_allow_html=True)
model_choice = st.sidebar.radio(
    "", 
    ("Logistic Regression", "Random Forest", "SVM")
)


model = load_model(model_choice.replace(" ", "_").lower())


def user_input_features():
    st.markdown("<h3 style='color:#d00000;'>📋 Enter your details below:</h3>", unsafe_allow_html=True)
    
    age = st.number_input("📅 Age", min_value=10, max_value=100, value=25)
    gender = st.selectbox('👤 Gender', ['Male', 'Female'])
    location = st.text_input('🌍 Location', 'United States')
    platform = st.selectbox('🖥️ Platform', ['Facebook', 'Instagram', 'YouTube', 'TikTok'])
    video_category = st.selectbox('🎥 Video Category', ['Pranks', 'Vlogs', 'Gaming'])
    engagement = st.selectbox('📊 Engagement', ['high', 'moderate', 'less'])
    frequency = st.selectbox('⏲️ Frequency', ['Morning', 'Afternoon', 'Evening', 'Night'])
    productivity_loss = st.slider('⚖️ Productivity Loss', 0, 10, 5)
    satisfaction = st.slider('😊 Satisfaction', 0, 10, 5)
    self_control = st.slider('🧘 Self Control', 0, 10, 5)
    watch_reason = st.selectbox('📺 Watch Reason', ['Procrastination', 'Habit', 'Entertainment', 'Boredom'])
    watch_time = st.text_input('🕒 Watch Time (e.g., 9:00 PM)', '9:00 PM')

    
    data = {
        'Age': age,
        'Gender': gender,
        'Location': location,
        'Platform': platform,
        'Video Category': video_category,
        'Engagement': engagement,
        'Frequency': frequency,
        'ProductivityLoss': productivity_loss,
        'Satisfaction': satisfaction,
        'Self Control': self_control,
        'Watch Reason': watch_reason,
        'Watch Time': watch_time
    }
    
    features = pd.DataFrame(data, index=[0])
    return features


input_df = user_input_features()


st.subheader('🔎 Your Input:')
st.write(input_df)


if st.button("🔮 Predict Addiction Level"):
    try:
        prediction = model.predict(input_df)
        st.markdown(f"<h2 style='color:green;text-align:center;'>🎯 Predicted Addiction Level: {prediction[0]}</h2>", unsafe_allow_html=True)
    except Exception as e:
        st.error(f"An error occurred: {e}")


st.markdown("<h6 style='text-align:center;color:#d00000;'>Designed by Tirth</h6>", unsafe_allow_html=True)

import streamlit as st
import random

# Page configuration
st.set_page_config(page_title="Growth Mindset Project", page_icon="🌱", layout="wide")

# Custom CSS for styling
st.markdown(
    """
    <style>
        /* Page styling */
        body {
            background-color: #f4f4f4;
        }
        
        /* Border for main content */
        .main-container {
            border: 3px solid #4CAF50;
            padding: 20px;
            border-radius: 15px;
            background-color: white;
        }

        /* Footer styling */
        .footer {
            position: fixed;
            bottom: 10px;
            right: 10px;
            font-size: 14px;
            font-weight: bold;
            color: #4CAF50;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Title and Introduction
st.title("🌱 Growth Mindset Challenge")
st.header("🚀 Welcome to Your Growth Journey!")
st.write("Welcome to the Growth Mindset Challenge! This app helps you develop a growth mindset through interactive content and quizzes.")

# Quotes section
st.header("💡 Today's Growth Mindset Quotes")
quotes = [
    "Mistakes are proof that you are trying!",
    "Failure is a stepping stone to success.",
    "Challenges help you grow!",
    "With effort, you can improve any skill!",
    "Success is not final, failure is not fatal. It is the courage to continue that counts."
]
st.write(random.choice(quotes))

# Quiz section
st.header("📖 Growth Mindset Quiz!")

questions = {
    "What is a growth mindset?": ["A belief that skills can improve", "A fixed intelligence level", "A talent you're born with"],
    "How should you view mistakes?": ["As learning opportunities", "As failures", "As reasons to quit"],
    "What is the key to improvement?": ["Effort and practice", "Natural talent", "Luck"],
}

score = 0
answers = {}

for question, options in questions.items():
    answers[question] = st.radio(question, options)

if st.button("Submit Quiz"):
    for question, options in questions.items():
        if answers[question] == options[0]:  # The correct answer is always the first option
            score += 1

    st.write(f"✅ You scored {score} out of {len(questions)}!")

    if score == len(questions):
        st.success("Amazing! You truly understand the growth mindset! 🌟")
        user_input = st.text_input("Describe a problem you are facing")
        if user_input:
            st.success(f"You're facing: {user_input}. Keep pushing forward to your goal! 💪")
    elif score > 0:
        st.info("Keep practicing! Every effort helps. 💪")
    else:
        st.warning("Don't worry! Learning is a journey. Try again! 🚀")

# Reflection section
st.header("📓 Growth Mindset Journal")

reflection = st.text_area("Write about a challenge you faced recently and how you overcame it.")
if st.button("Save Reflection"):
    st.success("Your reflection has been saved! Keep growing! 🌱")
else:
    st.info("Reflection on past experiences helps you grow! Share your difficulties.")

# Achievements section
st.header("🏆 Celebrate Your Wins!")
achievements = st.text_input("Share something you've recently accomplished:")

if achievements:
    st.success(f"🎉 Amazing! You achieved: {achievements}")
else:
    st.info("Big or small, every achievement counts! Share now! 🎉")

# Close main container
st.markdown("🚀 Keep believing in yourself" '</div>', unsafe_allow_html=True)

# Footer
st.markdown('<div class="footer"> **©️Sarah Survery**</div>', unsafe_allow_html=True)

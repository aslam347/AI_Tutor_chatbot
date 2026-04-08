import streamlit as st
from ai_engine import generate_learning_content, evaluate_answers

# Advanced Cinematic UI
st.markdown("""
<style>

/* Animated gradient background */
.stApp {
    background: linear-gradient(-45deg, #0f172a, #1e293b, #020617, #1e1b4b);
    background-size: 400% 400%;
    animation: gradientMove 10s ease infinite;
    color: white;
}

@keyframes gradientMove {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}

/* Glass card */
.card {
    padding: 25px;
    border-radius: 20px;
    background: rgba(255, 255, 255, 0.05);
    backdrop-filter: blur(15px);
    box-shadow: 
        0 8px 32px rgba(0, 0, 0, 0.37),
        inset 0 0 10px rgba(255,255,255,0.1);
    margin-top: 20px;
    transition: 0.3s;
}

.card:hover {
    transform: scale(1.02);
}

/* Inputs */
.stTextInput input, .stTextArea textarea, .stSelectbox div {
    border-radius: 12px;
    background-color: #1e293b;
    color: white;
}

/* Buttons */
.stButton>button {
    background: linear-gradient(135deg, #6366f1, #ec4899);
    color: white;
    border-radius: 12px;
    height: 3em;
    font-weight: bold;
    border: none;
    box-shadow: 0 0 15px rgba(99,102,241,0.6);
    transition: 0.3s;
}

.stButton>button:hover {
    transform: scale(1.05);
    box-shadow: 0 0 25px rgba(236,72,153,0.8);
}

/* Title */
h1 {
    text-align: center;
    font-size: 42px;
    background: linear-gradient(90deg, #6366f1, #ec4899);
    -webkit-background-clip: text;
    color: transparent;
}

</style>
""", unsafe_allow_html=True)

#  Header
st.markdown("<h1>🤖 AI Learning Tutor</h1>", unsafe_allow_html=True)
st.caption("🚀 Personalized AI Tutor • Smart Learning • Instant Feedback")

#  Main Card
st.markdown('<div class="card">', unsafe_allow_html=True)

# Inputs
class_level = st.selectbox("📘 Select Class", ["5", "8", "10"])
subject = st.selectbox("📚 Select Subject", ["Math", "Science"])
topic = st.text_input("✏️ Enter Topic")

# Generate
if st.button("🚀 Generate"):
    with st.spinner("🧠 AI is thinking..."):
        result = generate_learning_content(class_level, subject, topic)

    if "error" not in result:
        st.subheader("📖 Explanation")
        for point in result["explanation"]:
            st.write("• " + point)

        st.subheader("❓ Questions")
        for q in result["questions"]:
            st.write("👉 " + q)

        # Save questions
        st.session_state["questions"] = result["questions"]

    else:
        st.error("Something went wrong. Try again.")

#  Answers
answers = st.text_area("✍️ Enter your answers")

#  Evaluate
if st.button("🧠 Evaluate"):
    questions = st.session_state.get("questions", [])

    if not questions:
        st.warning("Please generate questions first.")
    else:
        with st.spinner("📊 Evaluating your answers..."):
            evaluation = evaluate_answers(questions, answers)

        if "error" not in evaluation:
            st.subheader("🏆 Score")
            st.write(evaluation["score"])

            st.subheader("💡 Feedback")
            st.write(evaluation["feedback"])

        else:
            st.error("Evaluation failed. Try again.")

st.markdown('</div>', unsafe_allow_html=True)
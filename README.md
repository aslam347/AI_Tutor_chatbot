# 🤖 AI Learning Tutor

🚀 **Live App:**  
https://ai-tutor-chatbot-mohamed-aslam.streamlit.app/

🎥 **Demo Video (Loom):**  
https://www.loom.com/share/abe2dd54705c4f008b8925ce48276f27

---

## 🎯 Overview

AI Learning Tutor is an AI-powered system that simulates a basic teacher by:

- Explaining concepts in simple bullet points  
- Asking questions  
- Evaluating student answers  
- Providing feedback and improvement suggestions  

---

## 🧠 Features

- ✅ Age-appropriate explanations  
- ✅ Bullet-point learning (easy to understand)  
- ✅ Auto-generated questions  
- ✅ AI-based evaluation  
- ✅ Score + feedback system  
- ✅ Clean UI with cinematic design  
- ✅ Structured JSON output  
- ✅ Prompt engineering focused system  

---

## 🏗️ System Flow

Input → Explanation → Questions → Answer → Evaluation → Feedback

---

## ⚙️ Tech Stack

- Python  
- Streamlit (UI)  
- OpenAI API (LLM)  
- Prompt Engineering  

---

## 📂 Project Structure

AI_Tutor_chatbot/

├── app.py          # Streamlit UI  
├── ai_engine.py    # AI logic (LLM + prompts)  
├── requirements.txt  
├── .gitignore  
└── README.md  

---

## 🔧 Setup Instructions

### 1. Clone Repository

git clone https://github.com/aslam347/AI_Tutor_chatbot.git  
cd AI_Tutor_chatbot  

---

### 2. Install Dependencies

pip install -r requirements.txt  

---

### 3. Add API Key (Local)

export OPENAI_API_KEY=your_api_key_here  

---

### 4. Run App

streamlit run app.py  

---

## 🔐 Deployment

Deployed using **Streamlit Cloud**

API keys are securely managed using **Streamlit Secrets**

---

## 💡 Prompt Engineering

The system uses structured prompts to:

- Ensure consistent JSON output  
- Generate bullet-point explanations  
- Control question generation  
- Provide reliable evaluation  

---

## ⚡ Scaling Considerations

If 10,000 users use this daily:

### Challenges:
- API rate limits  
- Latency issues  
- Increased cost  

### Solutions:
- Caching repeated queries  
- Async processing (Redis/Kafka queues)  
- Load balancing and auto-scaling  
- Using smaller models for cost optimization  

---

## 🚀 Future Improvements

- Adaptive difficulty levels  
- Student performance tracking  
- Chat-based conversational UI  
- Integration with real-time learning systems  

---

## 👤 Author

Mohamed Aslam  
AI/ML Engineer | Backend Developer  

---

## ⭐ Conclusion

This project demonstrates:

- Strong prompt engineering  
- Real AI system flow  
- Clean UI + user experience  
- Scalable architecture thinking  

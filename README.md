# 🤖 AI Learning Tutor  
### Personalized AI Tutor using OpenAI + Streamlit

An AI-powered educational assistant that helps school students learn concepts in a simple and interactive way using Generative AI.

This project simulates a smart AI tutor capable of:

- Explaining concepts in simple bullet points  
- Generating questions automatically  
- Evaluating student answers  
- Providing scores and improvement feedback  

Built using **OpenAI GPT models** and deployed with **Streamlit**.

---

# 🌐 Live Demo

🚀 Try the application here:

👉 https://ai-tutor-chatbot-mohamed-aslam.streamlit.app/

---

# 🎥 Demo Video

Watch the full project walkthrough:

👉 https://www.loom.com/share/abe2dd54705c4f008b8925ce48276f27

---

# 📌 Project Overview

AI Learning Tutor is designed as a beginner-friendly educational AI system for school students.

The application allows students to:

✅ Select class level  
✅ Select subject  
✅ Enter topic name  
✅ Receive simplified AI-generated explanations  
✅ Practice with generated questions  
✅ Get AI-based evaluation and feedback  

The system uses prompt engineering techniques to generate structured JSON outputs for reliable AI responses.

---

# 🚀 Key Features

✅ Personalized AI learning assistant  
✅ Child-friendly explanations  
✅ Automatic question generation  
✅ AI-powered answer evaluation  
✅ Score + improvement feedback  
✅ Structured JSON response handling  
✅ Beautiful cinematic Streamlit UI  
✅ Interactive educational experience  
✅ Prompt-engineering-based workflow  
✅ Lightweight and Dockerized deployment  

---

# 🧠 Example Workflow

### Student Input

- Class: 8  
- Subject: Science  
- Topic: Photosynthesis  

### AI Tutor Generates

✅ Simple explanation  
✅ Practice questions  
✅ Answer evaluation  
✅ Final score and feedback  

---

# 🛠️ Tech Stack

- Python  
- Streamlit  
- OpenAI API  
- Prompt Engineering  
- JSON Parsing  
- Python Dotenv  
- Docker  

---

# 🏗️ System Flow

```text
Student Input
      ↓
OpenAI Prompt Generation
      ↓
AI Explanation
      ↓
Question Generation
      ↓
Student Answers
      ↓
AI Evaluation
      ↓
Score + Feedback
```

---

# 📁 Project Structure

```text
AI_Tutor_chatbot/
│
├── app.py
├── ai_engine.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── .gitignore
├── .env
└── README.md
```

---

# ⚙️ Local Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/aslam347/AI_Tutor_chatbot.git
cd AI_Tutor_chatbot
```

---

## 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 3️⃣ Create Environment File

Create a `.env` file:

```env
OPENAI_API_KEY=your_openai_api_key
```

---

## 4️⃣ Run Application

```bash
streamlit run app.py
```

---

# 🐳 Run with Docker

## 1️⃣ Build Docker Image

```bash
docker build -t smart-tutor-ai .
```

---

## 2️⃣ Run Docker Container

```bash
docker run --env-file .env -p 8501:8501 smart-tutor-ai
```

---

## 3️⃣ Open in Browser

```text
http://localhost:8501
```

---

# 🐳 Docker Hub

If the image is pushed to Docker Hub, pull and run using:

```bash
docker pull mohamedaslam2001/smart-tutor-ai
docker run --env-file .env -p 8501:8501 mohamedaslam2001/smart-tutor-ai
```

---

# 📜 Requirements

```txt
streamlit
openai
python-dotenv
```

---

# 💡 Prompt Engineering Highlights

The system uses carefully designed prompts to:

✅ Generate structured JSON responses  
✅ Produce child-friendly explanations  
✅ Create educational questions  
✅ Evaluate student answers reliably  
✅ Maintain consistent AI outputs  

---

# ⚡ Scaling Considerations

If this system serves thousands of users daily:

### Potential Challenges

- API rate limits  
- Increased latency  
- Higher API costs  
- Concurrent request handling  

### Possible Solutions

✅ Response caching  
✅ Async task queues  
✅ Load balancing  
✅ Smaller model optimization  
✅ Cloud auto-scaling  

---

# 🚀 Future Enhancements

- Adaptive learning difficulty  
- Student progress tracking  
- Voice-based tutoring  
- Conversational AI tutor  
- Multi-language support  
- Real-time classroom integration  
- Learning analytics dashboard  

---

# 💡 Key Learnings

- Prompt Engineering  
- OpenAI API Integration  
- JSON Output Parsing  
- Streamlit UI Development  
- AI-based Evaluation Systems  
- Docker Containerization  
- Environment Variable Management  
- AI Product Deployment  

---

# 👨‍💻 Author

## Mohamed Aslam

AI/ML Engineer | Backend Developer | Generative AI Enthusiast

Passionate about:

- Generative AI  
- AI Agents  
- Real-world AI applications  
- Educational AI systems  
- End-to-end AI deployment  

---

# ⭐ Support

If you found this project useful, please give it a ⭐ on GitHub.

---

# 📜 License

This project is for educational and portfolio purposes.

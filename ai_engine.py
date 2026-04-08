import os
from openai import OpenAI
import json

#  Initialize client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


#  Utility: Clean JSON response (handles ```json issues)
def clean_json(content):
    content = content.strip()
    content = content.replace("```json", "").replace("```", "")
    return content


#  Step 1: Generate explanation + questions
def generate_learning_content(class_level, subject, topic):
    prompt = f"""
You are an AI tutor for Indian school students.

Class: {class_level}
Subject: {subject}
Topic: {topic}

Instructions:
- Explain in VERY SIMPLE bullet points (max 5 points)
- Each point should be 1 line only
- Use child-friendly language
- Ask exactly 2 short questions
- If unsure, say "I don't know"

Return ONLY JSON in this format:
{{
  "explanation": [
    "point 1",
    "point 2",
    "point 3"
  ],
  "questions": [
    "question 1",
    "question 2"
  ]
}}
"""

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.5
        )

        content = response.choices[0].message.content
        content = clean_json(content)

        return json.loads(content)

    except Exception as e:
        return {"error": str(e)}


#  Step 2: Evaluate answers
def evaluate_answers(questions, answers):
    prompt = f"""
You are an AI teacher.

Questions:
{questions}

Student Answers:
{answers}

Instructions:
- Be strict but fair
- Give score out of 10
- Provide correct answers
- Give improvement suggestions
- If answer is empty, give low score

Return ONLY JSON:
{{
  "score": "...",
  "feedback": "..."
}}
"""

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3
        )

        content = response.choices[0].message.content
        content = clean_json(content)

        return json.loads(content)

    except Exception as e:
        return {"error": str(e)}
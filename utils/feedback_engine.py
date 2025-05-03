from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

# Initialize OpenAI client using environment variable
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_feedback(resume_text: str) -> str:
    """
    Generate structured feedback for a resume using GPT-4.
    """
    system_prompt = (
        "You are a professional resume reviewer. Analyze the resume and give "
        "detailed, constructive feedback on formatting, grammar, structure, clarity, "
        "impact, and how it aligns with job market standards. Be objective and helpful."
    )

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": resume_text}
    ]

    response = client.chat.completions.create(
        model="gpt-4.1",
        messages=messages,
        temperature=0.7,
        max_tokens=800
    )

    return response.choices[0].message.content.strip()


def generate_interview_questions(resume_text: str) -> str:
    """
    Generate behavioral and technical interview questions based on a resume.
    """
    system_prompt = (
        "You are a senior technical recruiter. Based on the following resume, "
        "generate a list of behavioral and technical interview questions tailored "
        "to the candidate’s background. Include questions that test problem-solving, "
        "domain knowledge, and project involvement."
    )

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": resume_text}
    ]

    response = client.chat.completions.create(
        model="gpt-4.1",
        messages=messages,
        temperature=0.7,
        max_tokens=500
    )

    return response.choices[0].message.content.strip()

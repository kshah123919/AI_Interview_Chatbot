import google.generativeai as genai
from dotenv import load_dotenv 
import os
from memory_manager import get_recent_memory
from memory_manager import save_to_memory
load_dotenv()
API_KEY=os.getenv("GEMINI_API_KEY")
if not API_KEY:
    print("No API KEY found")
    exit()
genai.configure(api_key=API_KEY)
model=genai.GenerativeModel("models/gemini-2.5-flash")

def evaluate_ans(question,user_answer):
      past_memory=get_recent_memory()
      memory_text=""
      for item in past_memory:
            memory_text+=f"Question {item['Question']}\n Answer:{item['Answer']}\n Feedback :{item['Feedback']}"
 #  final prompt
      final_prompt=f"""
You are an AI Interview Coach.

Your task is to evaluate a candidate's interview answer.

Past interview context (if any):
{memory_text}

Current interview question:
{question}

Candidate's answer:
{user_answer}

Give:
1. Short and clear feedback on the answer
2. One specific improvement suggestion
Give feedback considering the past answers.
Keep the response concise and interview-focused.
You MUST include a line exactly in this format:
Score: X/10

Do not skip the score.
"""
      response=model.generate_content(final_prompt)
      ans=response.text
      save_to_memory(question,user_answer,ans)
      return ans 


from interview_agent import evaluate_ans
roles = {
    1: "Software Engineer",
    2: "Frontend Developer",
    3: "Backend Developer",
    4: "Python Developer",
    5:"Data Analyst",
    6:"Machine Learning Engineer",
    7:"DevOps Enginner",
    8:"Cyber Security Analyst"
}

print("Welcome to AI Interview Coach")

for key,value in roles.items():
    print(f"{key}. {value}")
print("Choose a role to begin your interview : ")
choice=int(input("Enter your choice : "))
print("You Selected :",roles[choice])
print("Starting Interview...")
selected_role=roles[choice]
questions = {
    "Software Engineer": [
        "What is Object-Oriented Programming (OOP)?",
        "Explain the difference between REST and SOAP APIs.",
        "What is time complexity and why is it important?",
        "Explain the concept of multithreading."
    ],

    "Frontend Developer": [
        "What is the difference between HTML, CSS, and JavaScript?",
        "Explain the CSS box model.",
        "What is the difference between var, let, and const?",
        "What is the DOM and how do you manipulate it?"
    ],

    "Backend Developer": [
        "What is the difference between GET and POST requests?",
        "Explain what an API is.",
        "What is authentication vs authorization?",
        "How do you handle errors in backend applications?"
    ],

    "Python Developer": [
        "What is the difference between list and tuple in Python?",
        "Explain Python decorators.",
        "What is exception handling?",
        "What are virtual environments and why are they used?"
    ],

    "Data Analyst": [
        "What is the difference between mean and median?",
        "Explain different types of SQL joins.",
        "What is data cleaning and why is it important?",
        "How do you handle missing values in a dataset?"
    ],

    "Machine Learning Engineer": [
        "What is the difference between supervised and unsupervised learning?",
        "What is overfitting and how can you prevent it?",
        "Explain the bias-variance tradeoff.",
        "Why do we split data into training and testing sets?"
    ],

    "DevOps Engineer": [
        "What is CI/CD?",
        "What is Docker and why is it used?",
        "Explain the difference between containers and virtual machines.",
        "What is monitoring and logging?"
    ],

    "Cyber Security Analyst": [
        "What is phishing?",
        "Explain the concept of encryption.",
        "What is the difference between HTTP and HTTPS?",
        "What is a firewall?"
    ]
}

role_questions=questions[selected_role]
score=[]
for q in role_questions:
    print(q)
    user_input=input("Your Answer :")
    feedback=evaluate_ans(q,user_input)
    print(feedback)
    
    if "Score:" in feedback:
        score_line=feedback.split("Score:")[1]
        score_num=score_line.split("/")[0].strip()
        score_num=int(score_num)
        
        score.append(score_num)
    else:
        print("score not found")

if len(score)>0:
    avg=sum(score)/len(score)
    print("Final_Interview_Score (out of 10) :",avg)
full_history_text="interview_memory.json"
summary_prompt = f"""
You are a professional AI Interview Coach.

Interview Role:
{selected_role}

Below is the complete interview history of the candidate.

Interview History:
{full_history_text}

Your task:
Based on the entire interview, generate a concise interview summary.

Provide the summary in the following format:

1. Overall Performance (2–3 lines)
2. Key Strengths (bullet points)
3. Weak Areas (bullet points)
4. Final Improvement Advice (1–2 lines)

Guidelines:
- Base your analysis ONLY on the interview history provided.
- Be honest, professional, and interview-focused.
- Do NOT repeat the questions verbatim.
- Keep the response concise and clear.

Also Provide a score from 1 to 10.And explain briefly why this score was given 


"""

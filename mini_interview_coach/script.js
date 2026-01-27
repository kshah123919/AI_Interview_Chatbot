console.log("JS loaded");


document.addEventListener("submit", function (e) {
    e.preventDefault();
});

// DOM elements
const chatContainer = document.getElementById("chat-container");
const sendBtn = document.getElementById("send-btn");
const input = document.getElementById("user-input");
const roleText = document.getElementById("role-text");

// App state
let state = "ROLE_SELECTION";
let selectedRole = null;
let currentQuestionIndex = 0;
let roleQuestions = [];

// Roles
const roles = {
    "1": "Software Engineer",
    "2": "Frontend Developer",
    "3": "Backend Developer",
    "4": "Python Developer",
    "5": "Data Analyst",
    "6": "Machine Learning Engineer",
    "7": "DevOps Engineer",
    "8": "Cyber Security Analyst"
};

// Questions per role
const questions = {
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
        "What is an API?",
        "Explain authentication vs authorization.",
        "How do you handle errors in backend applications?"
    ],
    "Python Developer": [
        "What is the difference between list and tuple in Python?",
        "Explain Python decorators.",
        "What is exception handling?",
        "What are virtual environments?"
    ],
    "Data Analyst": [
        "What is the difference between mean and median?",
        "Explain different types of SQL joins.",
        "What is data cleaning?",
        "How do you handle missing values?"
    ],
    "Machine Learning Engineer": [
        "What is supervised vs unsupervised learning?",
        "What is overfitting?",
        "Explain bias-variance tradeoff.",
        "Why do we split data into train/test?"
    ],
    "DevOps Engineer": [
        "What is CI/CD?",
        "What is Docker?",
        "Containers vs virtual machines?",
        "What is monitoring and logging?"
    ],
    "Cyber Security Analyst": [
        "What is phishing?",
        "What is encryption?",
        "Difference between HTTP and HTTPS?",
        "What is a firewall?"
    ]
};

// -------- Helpers --------
function addUserMessage(text) {
    const div = document.createElement("div");
    div.className = "message user-message";
    div.innerText = "You: " + text;
    chatContainer.appendChild(div);
    chatContainer.scrollTop = chatContainer.scrollHeight;
}

function addAIMessage(text) {
    const div = document.createElement("div");
    div.className = "message ai-message";
    div.innerText = "AI: " + text;
    chatContainer.appendChild(div);
    chatContainer.scrollTop = chatContainer.scrollHeight;
}

// -------- Prevent ENTER reload --------
input.addEventListener("keydown", function (e) {
    if (e.key === "Enter") {
        e.preventDefault();
        sendBtn.click();
    }
});

// -------- Initial welcome --------
window.onload = function () {
    addAIMessage("Welcome to AI Interview Coach 👋");
    addAIMessage("Please select a role to begin:");
    Object.entries(roles).forEach(([key, value]) => {
        addAIMessage(`${key}. ${value}`);
    });
};

// -------- Send button logic --------
sendBtn.addEventListener("click", async function (e) {
    e.preventDefault(); // 🚫 STOP reload

    const userText = input.value.trim();
    if (!userText) return;

    addUserMessage(userText);
    input.value = "";

    /* ROLE SELECTION */
    if (state === "ROLE_SELECTION") {
        if (!roles[userText]) {
            addAIMessage("Invalid choice ❌ Please enter 1 to 8.");
            return;
        }

        selectedRole = roles[userText];
        roleText.innerText = "Role: " + selectedRole;

        roleQuestions = questions[selectedRole];
        currentQuestionIndex = 0;
        state = "INTERVIEW";

        addAIMessage(`Great! You selected ${selectedRole}.`);
        addAIMessage("First question:");
        addAIMessage(roleQuestions[currentQuestionIndex]);
        return;
    }

    /* INTERVIEW STATE */
    if (state === "INTERVIEW") {
        const currentQuestion = roleQuestions[currentQuestionIndex];

        try {
            const response = await fetch("http://localhost:5000/interview", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({
                    question: currentQuestion,
                    answer: userText,
                    role: selectedRole
                })
            });

            const data = await response.json();
            addAIMessage(data.ai_reply);
        } catch (err) {
            addAIMessage("Server error ❌ Backend not reachable.");
            return;
        }

        currentQuestionIndex++;

        if (currentQuestionIndex < roleQuestions.length) {
            addAIMessage("Next question:");
            addAIMessage(roleQuestions[currentQuestionIndex]);
        } else {
            addAIMessage("Interview completed ✅ Thank you!");
            state = "DONE";
        }
    }
});

# 🩺 MediBot

![React](https://img.shields.io/badge/React-19-blue?logo=react)
![Node.js](https://img.shields.io/badge/Node.js-Express-green?logo=node.js)
![Python](https://img.shields.io/badge/Python-3.11-yellow?logo=python)
![TypeScript](https://img.shields.io/badge/TypeScript-5-blue?logo=typescript)

An AI-powered medical chatbot that assists users in understanding their symptoms through intelligent, context-aware conversations. The system collects relevant medical information using dynamic follow-up questions and generates informative responses using a locally hosted Large Language Model (LLM) powered by Ollama.

---

## ✨ Highlights

- AI-powered medical conversations
- Context-aware multi-turn dialogue
- Intelligent symptom assessment through follow-up questions
- Dynamic conversation routing
- Structured medical information collection
- Modular full-stack architecture
- Privacy-friendly local AI inference using Ollama
- Responsive React-based user interface

---

## 🚀 Features

- AI-powered medical conversations
- Multi-turn contextual conversations
- Symptom assessment through intelligent follow-up questions
- Conversation memory and context management
- Intelligent query routing
- Medical information collection (age, symptom duration, pain severity, etc.)
- Structured and easy-to-read AI-generated responses
- RESTful API communication
- Local LLM inference using Ollama
- Modular frontend, backend, and AI microservice architecture

---

## 🏗️ System Architecture

```text
                     +----------------------+
                     |   React Frontend     |
                     +----------+-----------+
                                |
                                | REST API
                                |
                     +----------v-----------+
                     |   Express Backend    |
                     +----------+-----------+
                                |
              +-----------------+-----------------+
              |                                   |
              |                                   |
     Session Management                  AI Microservice
                                                  |
                                                  |
                                          +-------v-------+
                                          |   Python API  |
                                          +-------+-------+
                                                  |
                                          Prompt Engineering
                                                  |
                                          +-------v-------+
                                          |    Ollama     |
                                          |  Local LLM    |
                                          +---------------+
```

---

## 🧠 AI Workflow

1. The user submits a medical question or describes their symptoms.
2. The backend receives the request.
3. Previous conversation history is retrieved.
4. The routing engine determines the appropriate processing pipeline.
5. If required, the chatbot asks follow-up questions to collect missing medical information.
6. A structured prompt is generated using the conversation context.
7. The prompt is sent to the locally hosted LLM through Ollama.
8. The AI generates a context-aware medical response.
9. The response is returned to the frontend and displayed to the user.

---

## 📂 Project Structure

```text
medical_chatbot/
│
├── frontend/
│   ├── public/
│   │   ├── favicon.ico
│   │   ├── index.html
│   │   ├── logo192.png
│   │   ├── logo512.png
│   │   ├── manifest.json
│   │   └── robots.txt
│   │
│   ├── src/
│   │   ├── pages/
│   │   │   ├── ChatPage.jsx
│   │   │   ├── LoginPage.jsx
│   │   │   └── RegisterPage.jsx
│   │   │
│   │   ├── App.js
│   │   ├── App.css
│   │   ├── index.js
│   │   ├── index.css
│   │   ├── App.test.js
│   │   ├── reportWebVitals.js
│   │   ├── setupTests.js
│   │   └── logo.svg
│   │
│   ├── .gitignore
│   ├── package.json
│   ├── package-lock.json
│   └── README.md
│
├── ai/
│   ├── .env
│   ├── app.py
│   ├── config.py
│   ├── db.py
│   ├── grad_runner.py
│   ├── mistral_runner.py
│   ├── nhs_conditions.json
│   └── requirements.txt
│
├── README.md
└── .gitignore
```

> *The internal structure of each module may vary depending on future development.*

---

## 🛠️ Tech Stack

### Frontend

- React.js
- TypeScript
- Vite
- CSS

### Backend

- Node.js
- Express.js
- REST APIs

## AI

- Python
- Ollama
- Large Language Models (LLMs)
- Prompt Engineering
- Natural Language Processing (NLP)

### Development Tools

- Git
- GitHub
- npm
- Postman

---

## ⚙️ Prerequisites

Before running the project, ensure you have installed:

- Node.js
- npm
- Python 3.10+
- Ollama
- Git

---

## 📦 Installation

### Clone the repository

```bash
git clone https://github.com/RanimMoharebb/Medical-Chatbot.git
cd Medical-Chatbot
```

---

### Install Backend Dependencies

```bash
cd backend
npm install
```

---

### Install Frontend Dependencies

```bash
cd frontend
npm install
```

---

### Install AI Service Dependencies

```bash
cd ai
pip install -r requirements.txt
```

---

## 🔧 Environment Variables

Create a `.env` file inside the backend (or AI service if applicable) and configure the required environment variables.

```env
PORT=5000

OLLAMA_HOST=http://localhost:11434
OLLAMA_MODEL=elixpo/llamamedicine
```

> **Note:** Ensure the specified Ollama model is installed locally. You may replace it with any compatible model available on your machine.

---

## ▶️ Running the Project

Start each service in the following order.

### 1. Start Ollama

```bash
ollama serve
```

### 2. Start the AI Service

```bash
cd ai
python app.py
```

### 3. Start the Backend

```bash
cd backend
npm run dev
```

### 4. Start the Frontend

```bash
cd frontend
npm run dev
```

---

## 📌 Core Functionalities

### Intelligent Medical Conversations

Collects symptoms through natural conversations and asks medically relevant follow-up questions before generating a response.

### Context Management

Maintains conversation history to produce coherent multi-turn interactions.

### Prompt Engineering

Constructs structured prompts to improve the quality, consistency, and relevance of AI-generated responses.

### Intelligent Query Routing

Determines whether additional medical information is required before generating a response.

### Local AI Inference

Runs the language model locally through Ollama, providing enhanced privacy and eliminating dependence on external AI APIs.

---


## 🔮 Future Improvements

- Doctor appointment booking integration
- Doctor recommendation system
- Voice-based conversations
- Medical report summarization
- Image-based symptom analysis
- Electronic Health Record (EHR) integration
- Multi-language support
- User authentication and profiles
- Docker deployment

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Push your branch.
5. Open a Pull Request.

---


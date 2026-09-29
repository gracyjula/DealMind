DealMind 🧠

AI Sales Intelligence Agent with Persistent Memory

DealMind is an AI-powered sales intelligence platform built by Team INVENTA for the HackWithHyderabad Hackathon.

The goal of DealMind is to help sales teams prepare for customer conversations by remembering important information from previous interactions and using that context to generate an AI-powered call brief.

Instead of treating every sales conversation as a completely new interaction, DealMind uses Hindsight as its persistent memory layer so relevant customer information can be recalled when preparing for the next call.

🚀 Key Features

🧠 Persistent Customer Memory using Hindsight

🔎 Memory Recall for previous customer information

📋 AI Call Brief generation

🎯 Next Call Preparation with one click

💬 Customer concerns and requirements

📅 Important deadlines and deal context

💡 Suggested talking points for the next conversation

🌙 Professional dark dashboard UI

💡 Problem

Sales teams often have to keep track of information across multiple conversations with the same customer.

Important details such as:

Customer concerns

Requirements

Deadlines

Previous discussions

Deal context

can become difficult to manage manually.

A normal AI assistant that only sees the current prompt may not have access to this previous context.

DealMind addresses this by making persistent memory a central part of the sales workflow.

🧠 Why Hindsight?

Hindsight is the memory layer used by DealMind.

It allows the application to store and recall relevant customer information so that previous interactions can contribute to future AI-generated sales briefs.

The workflow is:

Previous Customer Information
          ↓
      Hindsight
          ↓
     Memory Recall
          ↓
   Relevant Context
          ↓
        Groq
          ↓
    AI Call Brief
          ↓
   Prepare Next Call

⚙️ How DealMind Works

The application contains customer-related information and memories.

When the user selects Prepare for Next Call, DealMind requests relevant information from the memory layer.

Hindsight recalls the stored customer context.

The recalled information is provided to the AI workflow.

Groq generates an AI call brief.

The dashboard displays useful information such as customer concerns, requirements, deadlines, and suggested talking points.

🏗️ Architecture

                    ┌─────────────────────┐
                    │      User           │
                    │  Sales Team Member  │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │  React + Vite UI    │
                    │   DealMind Dashboard │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │    FastAPI Backend  │
                    └──────────┬──────────┘
                               │
                 ┌─────────────┴─────────────┐
                 ▼                           ▼
        ┌─────────────────┐         ┌─────────────────┐
        │    Hindsight    │         │      Groq       │
        │ Persistent      │         │ AI / LLM        │
        │ Memory          │         │ Generation      │
        └─────────────────┘         └─────────────────┘
                 │                           │
                 └─────────────┬─────────────┘
                               ▼
                    ┌─────────────────────┐
                    │    AI Call Brief    │
                    │  for Next Meeting   │
                    └─────────────────────┘

🛠️ Tech Stack

Frontend

React

Vite

CSS

Professional dark dashboard interface

Backend

Python

FastAPI

Uvicorn

AI & Memory

Hindsight — persistent memory

Groq — LLM generation

🖥️ User Interface

The DealMind dashboard includes:

DealMind branding

Powered by Hindsight memory indicator

Customer intelligence section

Prepare for Next Call action

Customer information

Customer memory

AI-generated call brief

The interface is designed as a professional sales intelligence dashboard rather than a basic chatbot.

🔌 Backend API

The project includes FastAPI endpoints for the DealMind backend.

Root

GET /

Used to check whether the DealMind backend is running.

Recall

GET /recall

Used to retrieve relevant customer memories.

Brief

GET /brief

Used to obtain the AI-generated sales brief.

▶️ Running the Project Locally

1. Clone the repository

git clone https://github.com/gracyjula/DealMind.git
cd DealMind

2. Start the Backend

Open a terminal and move into the backend directory.

Windows Command Prompt

cd /d D:\Desktop\DealMind\DealMind\backend

Activate the virtual environment:

venv\Scripts\activate

Start FastAPI:

uvicorn main:app --reload

The backend should run at:

http://127.0.0.1:8000

3. Start the Frontend

Open a second terminal.

cd /d D:\Desktop\DealMind\DealMind\frontend

Run:

npm install
npm run dev

The frontend should be available at:

http://localhost:5173

🔍 Testing the Backend

After starting the backend, you can check:

http://localhost:8000/

http://localhost:8000/recall

http://localhost:8000/brief

The root endpoint can be used to verify that the backend is running, while the other endpoints expose memory recall and the generated brief.

🎬 Demo Flow

A simple demonstration of DealMind can follow this flow:

Open the DealMind dashboard.

Introduce DealMind as an AI Sales Intelligence platform.

Explain that Hindsight provides persistent customer memory.

Explain that Groq is used to generate meeting briefs.

Click Prepare for Next Call.

Show the recalled customer memories.

Show customer concerns and requirements.

Show deadlines and other deal context.

Show the generated AI call brief and suggested talking points.

Explain how persistent memory helps sales teams prepare for customer meetings.

🎯 Example Use Case

Imagine a sales team has already had multiple conversations with a customer.

During previous interactions, the customer mentioned:

A pricing concern

A specific implementation requirement

A deadline

Existing tools such as Salesforce

When the sales representative prepares for the next call, DealMind can recall the relevant information and use it to generate a focused call brief.

This allows the representative to start with the context of the relationship instead of starting from zero.

🧩 Challenges

Some of the main development challenges included:

Integrating persistent memory into the sales workflow

Connecting the frontend and FastAPI backend

Making recalled information useful for AI-generated briefs

Creating a professional dashboard experience

Ensuring the project workflow clearly demonstrates the value of memory

📚 What We Learned

Building DealMind helped us explore how persistent memory can change an AI application.

A conventional AI interaction is often based mainly on the current prompt.

With persistent memory, an AI application can instead:

Remember
   ↓
Recall
   ↓
Understand Context
   ↓
Generate a More Contextual Response

For DealMind, this concept is applied to sales conversations and meeting preparation.

🔮 Future Improvements

Potential future improvements include:

More customer profiles and deal histories

Richer sales conversation history

CRM integrations

More advanced deal-stage tracking

Additional memory-based insights

More personalized sales recommendations

Improved analytics and reporting

Production deployment

👥 Team

Team INVENTA

Nandini Daggu

Gracy Prasanna Jula

Shivani Edigi

🏆 Hackathon

Built for the HackWithHyderabad Hackathon using Hindsight as the persistent memory layer.

🙌 Acknowledgements

Thanks to the HackWithHyderabad Hackathon organizers and the Hindsight/Vectorize ecosystem for providing the opportunity to explore memory-powered AI applications.

📄 License

Add the project's license here if a license has been added to the repository.

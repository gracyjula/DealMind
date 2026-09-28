import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from hindsight_client import Hindsight
from groq import Groq


# Load environment variables
load_dotenv()


# Create FastAPI app
app = FastAPI(title="DealMind")


# ============================================================
# CORS CONFIGURATION
# ============================================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ============================================================
# HINDSIGHT
# ============================================================

hindsight = Hindsight(
    "https://api.hindsight.vectorize.io",
    api_key=os.getenv("HINDSIGHT_API_KEY")
)


# ============================================================
# GROQ
# ============================================================

groq = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


# Hindsight memory bank
BANK_ID = os.getenv("HINDSIGHT_BANK_ID")


# ============================================================
# HOME
# ============================================================

@app.get("/")
def home():
    return {
        "message": "DealMind backend is running"
    }


# ============================================================
# ADD CUSTOMER MEMORY
# ============================================================

@app.post("/add-memory")
def add_memory():

    content = """
    Customer: Acme Corp
    Date: September 25, 2026

    Sales Meeting:

    Acme still considers our pricing higher than expected.

    The CTO confirmed that Salesforce integration is mandatory.

    Implementation time is now the biggest concern.

    The customer needs implementation completed within two weeks.

    The customer asked for a detailed implementation plan before the next meeting.
    """

    result = hindsight.retain(
        bank_id=BANK_ID,
        content=content
    )

    return {
        "message": "Customer memory stored successfully",
        "result": str(result)
    }


# ============================================================
# RECALL CUSTOMER MEMORIES
# ============================================================

@app.get("/recall")
def recall():

    result = hindsight.recall(
        bank_id=BANK_ID,
        query=(
            "What are Acme Corp's main concerns, "
            "requirements, deadlines, stakeholders "
            "and commitments?"
        )
    )

    memories = [
        {
            "text": memory.text,
            "type": memory.type
        }
        for memory in result.results
    ]

    return {
        "customer": "Acme Corp",
        "memories": memories
    }


# ============================================================
# GENERATE AI SALES BRIEF
# ============================================================

@app.get("/brief")
def generate_brief():

    result = hindsight.recall(
        bank_id=BANK_ID,
        query=(
            "Prepare me for the next Acme Corp sales meeting. "
            "What are their concerns, requirements, deadlines, "
            "stakeholders and previous commitments?"
        ),
        max_tokens=4096
    )

    memory_text = "\n".join(
        f"- {memory.text}"
        for memory in result.results
    )


    # ========================================================
    # GROQ PROMPT
    # ========================================================

    prompt = f"""
You are DealMind, an AI sales intelligence assistant.

Your job is to prepare a salesperson for their next customer meeting.

Customer:
Acme Corp

Customer history retrieved from Hindsight:
{memory_text}

Create a concise professional sales call preparation brief.

Use exactly these sections:

1. Customer Situation
2. Key Concerns
3. Critical Requirements
4. Stakeholders
5. Commitments / Deadlines
6. What To Prepare
7. Suggested Talking Points

IMPORTANT RULES:

- Use ONLY information supported by the customer history.
- Do NOT invent facts.
- Do NOT assume a person is a decision-maker unless explicitly stated.
- Do NOT invent dates.
- For stakeholders, mention only roles or people explicitly supported by the memory.
- Clearly distinguish requirements from concerns.
- Keep the response practical for a salesperson.
"""


    # ========================================================
    # GROQ REQUEST
    # ========================================================

    response = groq.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a professional B2B sales intelligence "
                    "assistant. Ground every statement in the "
                    "customer history provided."
                )
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2
    )


    answer = response.choices[0].message.content


    # ========================================================
    # RESPONSE
    # ========================================================

    return {
        "customer": "Acme Corp",
        "memory_count": len(result.results),
        "brief": answer
    }
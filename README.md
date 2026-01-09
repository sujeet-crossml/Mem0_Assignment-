# Mem0_Assignment-
Upgrading langchain assignment using mem0 for the memory of agent working response

## 🧠 LangChain Agents with Google Gemini & Mem0 Memory

### 📌 Project Objective

The goal of this assignment is to:

  - Understand LangChain Agents
  - Implement custom tools
  - Explore single-tool vs multi-tool agents
  - Integrate external APIs with LLMs
  - Learn practical agent orchestration using Google Gemini
  - Introduce Mem0 as a persistent memory layer for intelligent agents

### 🧠 Agents Implemented

  1️⃣ Multi Tool Agent
  
  - Uses multiple tools
  - The LLM dynamically decides:
    - Which tool to call
    - When to call it
  - Handles mixed queries such as:
    - “Analyze this text and tell me the sentiment”
    - “What is the date 30 days from now?”

  2️⃣ API
  - Integrates external APIs
    - Example:
      - 🌦️ Weather data using OpenWeatherMap
    - Demonstrates real-world LLM + API orchestration
   
  
  3️⃣ Memory-Enabled Agent (Mem0 Integration)
  
  - Uses Mem0 as a long-term memory store
  - Enables the agent to
    - Remember user preferences
    - Recall past interactions
    - Fetch relevant memories during reasoning
  - Adds statefulness to otherwise stateless LLM calls

## 🧠 What is Mem0?

Mem0 is a lightweight memory layer for LLM agents that allows:
- Semantic memory search
- User-specific memory filtering
- Persistent context across conversations

### Why Mem0?

Without memory:
- LLMs forget everything after each request ❌

With Mem0:
- Agents can remember, retrieve, and reason using past data ✅

## 🔁 How Memory Works in This Project

1. User interaction occurs
2. Important information is stored in Mem0
3. On new queries:
  - Relevant memories are retrieved using semantic search
  - Memory is injected into the agent prompt
4. The agent produces context-aware responses

## 🛠️ Tech Stack

- Language: Python 3.10+
- Framework: LangChain
- LLM: Google Gemini
    - gemini-2.5-flash
    - gemini-2.5-flash-lite
- Memory Layer: Mem0
- Environment: Virtual Environment (venv)
- API: OpenWeatherMap

## ⚙️ Installation & Setup

1️⃣ Clone the Repository

      git clone https://github.com/sujeet-crossml/Mem0_Assignment.git
      cd Mem0_Assignment

2️⃣ Create & Activate Virtual Environment

    python -m venv myenv
    source myenv/bin/activate     # Linux / macOS
    myenv\Scripts\activate        # Windows

## 🔐 API Key Configuration

Add your Gemini API Key in cred.py:

    gemini_api_key = "YOUR_GEMINI_API_KEY"


(Optional but recommended)

Use .env for production:

    GEMINI_API_KEY=your_key_here
    MEM0_API_KEY=your_mem0_key_here

## ⚠️ Important Notes

- ❌ Do NOT commit real API keys to GitHub

- ✅ Use environment variables for secure deployments

## ▶️ How to Run

Run the main application:

    python main.py


The agent will:
  1. Understand the user query
  2. Retrieve relevant memory (via Mem0)
  3. Select the appropriate tool
  4. Execute the tool or API
  5. Return a final, context-aware response

## 📌 Example Use Cases

- Solve mathematical calculations
- Find future dates
- Analyze text sentiment and statistics
- Fetch live weather information
- Dynamically choose tools based on user intent
- Remember user preferences using memory
- Answer queries using historical context

## 🧪 Learning Outcomes

- By completing this project, you will gain:
- Practical understanding of LangChain Agents
- Hands-on experience with custom tools
- Clear distinction between single-tool and multi-tool agents
- Real-world API integration with LLMs
- Introduction to agent memory using Mem0
- Best practices for scalable AI application design

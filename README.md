# QA-ChatBot 🤖
A Question-Answering Chatbot Powered by Gemma3 (Ollama) and DeepSeek-R1 (Groq) via LangChain

## 🧠 Overview
QA-ChatBot is an intelligent question-answering chatbot built using two cutting-edge language models:

- gemma3:1b served locally via Ollama

- deepseek-r1 accessed via the Groq API

These models are orchestrated through LangChain to manage multi-model routing, prompt chaining, and contextual memory.

## ⚙️ Features
- 🔀 Hybrid Model Routing – Automatically routes questions between Gemma and DeepSeek depending on complexity or topic.

- 🧩 LangChain Integration – Manages prompts, history, tools, and chains.

- 🖥️ Local + API Setup – Combines the speed of local inference (Ollama) with the power of cloud inference (Groq).

- 📚 Contextual QA – Provides accurate answers with memory and tool-enhanced capabilities

## 📦 Requirements
- Python 3.9+

- Ollama installed locally with gemma3:1b model

- Groq API key

- LangChain and required packages

## 🚀 Installation

```bash
git clone https://github.com/your-username/qa-chatbot.git
cd qa-chatbot
pip install -r requirements.txt
```

##🧠 Model Setup
🔹 1. Start the Gemma3 model with Ollama:
```bash
ollama run gemma3:1b
```
🔹 2. Add your Groq API key:
Create a .env file:

```ini
GROQ_API_KEY=your_groq_api_key_here
```

## 📜 Example Usage

```python
from langchain.chains import ConversationChain
from langchain_community.llms import Ollama, GroqLLM
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate

# Load models
gemma_llm = Ollama(model="gemma3:1b")
deepseek_llm = GroqLLM(model="deepseek-r1", api_key=os.getenv("GROQ_API_KEY"))

# Example routing logic (simplified)
def choose_model(prompt):
    if "code" in prompt or "technical" in prompt:
        return deepseek_llm
    return gemma_llm

# Chain execution
user_input = "Explain how LangChain works with multiple models"
selected_llm = choose_model(user_input)
response = selected_llm(user_input)
print(response)
```
## 🛠 Architecture

```mermaid
graph TD
    A[User Input] --> B[LangChain Router]
    B --> C[Gemma3:1b (Ollama)]
    B --> D[DeepSeek-R1 (Groq API)]
    C --> E[Response]
    D --> E[Response]
```

## 🧪 Testing
You can test the system with sample inputs via CLI or build a Streamlit/Gradio frontend for user interaction.

## 📝 License
MIT License




# 🤖 Day 13: Multi-Agent AI Debate System

A sophisticated multi-agent system where two competing AI agents debate a given topic, moderated and scored by a third AI judge. Built using **Groq** and the **Llama 3.3 70B** model for high-speed, intelligent reasoning.

![Debate System Preview](https://img.shields.io/badge/Day-13-blue)
![Python](https://img.shields.io/badge/Python-3.8%2B-green)
![Groq](https://img.shields.io/badge/Powered%20By-Groq-orange)

## 🌟 Features

- **Trio of Specialized Agents**:
  - **Agent PRO**: Argues strongly in favor of the topic.
  - **Agent CON**: Argues strongly against the topic.
  - **Agent JUDGE**: Evaluates both sides based on logic, evidence, and persuasion.
- **Dynamic 3-Round Debate**:
  - **Round 1**: Opening arguments.
  - **Round 2**: Direct rebuttals (agents respond specifically to their opponent's previous points).
  - **Round 3**: Powerful closing statements.
- **Scoring System**: The Judge provides a scorecard (out of 30) and a final verdict explaining why the winner was chosen.
- **Interactive CLI**: Choose from sample topics or enter your own custom debate prompt.

## 🛠️ Technology Stack

- **Large Language Model**: Llama 3.3 70B (via Groq Cloud)
- **Framework**: Python 3.x
- **Environment Management**: `python-dotenv`
- **API Client**: `groq`

## 🚀 Getting Started

### 1. Prerequisites
- A Groq API Key (Get one at [console.groq.com](https://console.groq.com))
- Python installed on your system.

### 2. Installation
Clone the repository and install dependencies:

```bash
pip install groq python-dotenv
```

### 3. Configuration
Create a `.env` file in the root directory and add your API key:

```env
GROQ_API_KEY=your_groq_api_key_here
```

### 4. Running the App
Start the debate system:

```bash
python app.py
```

## 📂 Project Structure

- `app.py`: Entry point and interactive CLI.
- `debate.py`: Logic for the 3-round debate loop.
- `agents.py`: Agent configurations and LLM calls.
- `.env`: (Ignored) Storage for API keys.
- `requirements.txt`: List of dependencies.

## 📝 Example Topics
- "AI will replace software engineers within 10 years"
- "Remote work is better than office work"
- "Social media does more harm than good"

---
*Developed as part of the 25 Days of ML Projects challenge.*

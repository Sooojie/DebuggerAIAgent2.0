
# Debugger AI Agent

An AI-powered code debugging and development assistant

The application allows developers to submit source code and receive AI-generated bug diagnoses, explanations, corrected code, improvement suggestions, and recommended test cases.

Deployed on https://debuggeraiagent2-0.onrender.com/

## Features

- Bug Detection: Identifies potential syntax, runtime, and logical errors.
- Error Explanation: Explains why a problem occurs.
- Code Correction: Generates a proposed corrected version of the submitted code.
- Code Explanation: Describes important corrections and changes.
- Code Improvement: Provides recommendations for readability, efficiency, and structure.
- Test Suggestions: Recommends test cases to verify expected behavior.
- Code Download: Allows users to download the proposed corrected code.

## Technologies

- Python
- Streamlit
- Ollama
- Llama 3.2
- Render

## Prompt Engineering

The project incorporates multiple prompt-engineering techniques:

1. **Role Prompting:** Assigns the LLM the role of an experienced code debugging and development assistant.
2. **Few-Shot Prompting:** Provides examples of code errors and expected debugging responses to guide the model's output.
3. **Structured Output:** Uses JSON formatting to organize the model's response into predictable fields.

## Requirements

- Python 3
- An OpenAI API key
- API access and any required billing configuration

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/Sooojie/DebuggerAIAgent2.0
cd DebuggerAIAgent2.0
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate the environment on Windows:

```powershell
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Install Ollama

Download and install Ollama:

https://ollama.com/

Download the Llama 3.2 model:

```bash
ollama pull llama3.2
```

Make sure Ollama is running before using the application locally.

### 5. Run the application

Start the Streamlit interface:

```bash
streamlit run app.py
```

Alternatively, run the terminal interface:

```bash
python main.py
```

## Usage

1. Open the application.
2. Select the programming language.
3. Enter or paste source code.
4. Optionally provide an error message or describe the problem.
5. Click **Debug My Code**.
6. Review the AI-generated diagnosis and proposed correction.
7. Explore the suggestions and recommended test cases.
8. Download the corrected code if desired.


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
- Google gemini-3.8-flash
- Render

## Prompt Engineering

The project incorporates multiple prompt-engineering techniques:

1. **Role Prompting:** Assigns the LLM the role of an experienced code debugging and development assistant.
2. **Few-Shot Prompting:** Provides examples of code errors and expected debugging responses to guide the model's output.
3. **Structured Output:** Uses JSON formatting to organize the model's response into predictable fields.

## Usage

Deployment Link: https://debuggeraiagent2-0.onrender.com/
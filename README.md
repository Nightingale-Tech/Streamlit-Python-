# Streamlit-Python-
Building a Beginner’s Toolkit for Streamlit (Python)
# Prompt-Powered Kickstart: Beginner’s Toolkit for Streamlit (Python)

## Overview

This project is a beginner-friendly toolkit designed to help users quickly get started with **Streamlit**, a Python framework for building interactive web applications.

Using **Generative AI prompts**, this project demonstrates how to:

- Learn a new technology efficiently
- Build a simple working application
- Document the process for easy replication

---
##  What is Streamlit?
Streamlit is a Python framework that allows you to create web apps easily without needing HTML, CSS, or JavaScript.

###  Where it is used:
- Data dashboards  
- Machine learning apps  
- Simple tools and interfaces  

###  Example:
A data analyst can use Streamlit to create a dashboard that shows sales data.

--- 

##  Project Objective

The goal of this project is to:

- Introduce Streamlit to beginners
- Build a minimal interactive web app
- Showcase how AI-assisted learning improves productivity and understanding

---

##  Tech Stack

| Tool | Version |
|------|---------|
| Python | 3.7+ |
| Streamlit | Latest |
| VS Code | Recommended Editor |

---

##  Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/streamlit-toolkit.git
cd streamlit-toolkit
```

### 2. Create a Virtual Environment *(Optional but Recommended)*

```bash
python -m venv venv

# On Linux/Mac
source venv/bin/activate

# On Windows
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` is not available:

```bash
pip install streamlit
```

---

##  Running the Application

```bash
streamlit run app.py
```

After running, open your browser and go to:

```
http://localhost:8501
```

---

##  Application Features

-  Simple and interactive UI
-  User input field
-  Dynamic output display
-  Beginner-friendly structure

---

##  Minimal Working Example

```python
import streamlit as st

st.title("My First Streamlit App")

name = st.text_input("Enter your name:")

if name:
    st.write(f"Hello, {name}!  Welcome to Streamlit.")

 if city:
    st.write(f"Nightingale lives in {city}.")   
```

---
## screenshots of the app
C:\Users\KEN16877\Documents\GENAI\Project\Streamlit-Python-\Screenshot .jpg

##  AI Prompt Documentation (Learning Process)

### 🔹 Prompt 1

> **Prompt:** "How do I install and run Streamlit for beginners?"

- **Outcome:** Provided installation steps and initial setup guidance.
- **Reflection:** Saved time and simplified onboarding.

### 🔹 Prompt 2

> **Prompt:** "Generate a simple Streamlit app with user input and output"

- **Outcome:** Produced a working example with explanations.
- **Reflection:** Helped understand Streamlit structure quickly.

### 🔹 Prompt 3

> **Prompt:** "Why is my Streamlit app not opening in browser?"

- **Outcome:** Identified common issues like port conflicts and environment errors.
- **Reflection:** Improved debugging skills.

---

##  Common Issues & Fixes

| Issue | Cause | Solution |
|-------|-------|----------|
| `streamlit: command not found` | Not installed | Run `pip install streamlit` |
| App not loading | Port issue | Visit `localhost:8501` |
| Module errors | Wrong environment | Activate virtual environment |

---

##  Project Structure

```
streamlit-toolkit/
│── app.py
│── requirements.txt
│── README.md
```

--


---

##  References

- ChatGpt
- Claude AI
- Gemini
- 

---

##  Acknowledgements

This project was developed as part of the **Moringa AI Capstone Project**, demonstrating the use of AI tools to accelerate learning and development.

---

##  Author

**[Nightingale Jeptoo]**
- GitHub: [git@github.com:Nightingale-Tech/Streamlit-Python-.git]

---

##  Final Note

> This project highlights how **AI-powered learning** can help beginners quickly understand new technologies and build functional applications with confidence.




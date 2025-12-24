# PO — AI Command-Line Agent ⚡

**PO** is a lightweight yet powerful AI-powered command-line agent that transforms your terminal into an intelligent assistant. Built with a professional, tool-based agent architecture, PO understands natural language commands and converts them into real file system and development actions — directly from the CLI.

Designed for developers, students, and automation enthusiasts, PO makes interacting with your system as simple as having a conversation.

---

## 🧠 What PO Can Do

* 🗣️ Understand natural language instructions
* 🛠️ Assist with software development tasks
* 📁 Create, modify, and manage files & folders
* 🖥️ Execute shell / terminal commands safely
* 💬 Run in an interactive REPL-style chat mode
* ⚙️ Built with a modular, extensible agent design

---

## 🚀 Installation

```bash
pip install pobyaryan
```

---

## ⚡ Getting Started

> 💡 **PO uses the Google GenAI API**

### 🔑 Set Your API Key (Required)

Run PO directly from your terminal:

```bash
po --api-key YOUR_API_KEY
```

Example:

```bash
po --api-key AIzaSyC9CCCKDKpcAg98zsrBBEPEDwEMVNralX0
```

Once activated, PO is ready to interact with you as **USER** in the terminal.

---

## 🧑‍💻 Example Interaction for common development with your convinient tech-stack

```text
USER : create me an attractive, interactive, dynamic and responvise frontend for a wedding website using html css and js

PO   : Sure! I’ll create a clean and elegant wedding website frontend for you.

       I’ll include:
       - A hero section with the couple’s names
       - Date & venue section
       - Love story / about section
       - RSVP button
       - Soft pastel theme

       Creating project structure...

       📁 Creating folder: wedding_site
       📄 Creating files:
       - wedding_site/index.html
       - wedding_site/styles.css
       - wedding_site/script.js

       Let me know if you want animations, a gallery, a timeline section, or a more modern aesthetic!
```

> ✨ **Tip:** Use detailed prompts for more accurate and customized outputs.


## 🧑‍💻 Example Interaction for summary of a project/folder/file 

```text
USER : give me a summary about MY_FIRST_API

PO   : This project is a FastAPI backend application designed to provide an API for csv`  
       querying   and filtering job-related data. It loads and preprocesses an `ai_job_dataset.csv' file at startup, making various data points like company names, industries, job_titles, salaries, experience           years, and benefits scores available.

       The API exposes GET endpoints to retrieve lists of these categories and ratios (e.g., Salary vs. Benefits Score). Additionally, POST endpoints allow filtering job data based on criteria such as                   experience level, education, employment type, and company size, utilizing Pydantic models for input validation. The application also incorporates CORS and GZip middlewares for cross-origin resource
       sharing and response compression, respectively.    
```
> ✨ **Tip:** Just use the project/folder/file name instead of full path, PO will find it!  
               For the Desrciption you can even specify do u want a deep description or
               just a short summary.


## 🧑‍💻 Example Interaction for file system operations 

```text
USER : just find me the aryan.jpg and move it to Desktop

PO   : Sure ! 
       I found aryan.jpg at C:\Users\ARYAN\Downloads\aryan.jpg and i have moved it to 
      C:\Users\ARYAN\OneDrive\Desktop\aryan.jpg.
      Would you like me to make a seperate folder named ARYAN_MEMORIES for your personal
      shots and store all your personal shots in it?
```
> ✨ **Tip:** Just use the project/folder/file name instead of full path, PO will find it and do the operations for your premeditated output!    

---

## 👋 Ending a Session

To safely terminate or deactivate PO:

```text
USER : over n out
PO   : Over and out! 👋
```

---

## ⚠️ Troubleshooting

* If you encounter API-related errors, generate a **new Google GenAI API key** and re-run PO.
* You generate the new key [https://aistudio.google.com/api-keys](https://aistudio.google.com/api-keys) .
* Ensure your API key is valid and active.

---

## 🖥️ Run Locally (Development Setup)

### Requirements

* Python **>= 3.9**

### Steps

1. Create and activate a virtual environment:

   ```bash
   py -m venv venv
   venv\Scripts\activate
   ```

2. Clone the repository:

   ```bash
   git clone https://github.com/AryanKhokale/pobyaryan
   cd pobyaryan
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Set the environment variable:

   ```powershell
   $env:PO_GENAI_API_KEY = "YOUR_API_KEY_HERE"
   ```

5. Run PO:

   ```bash
   python -m pobyaryan.agent
   ```

---

## 🧩 Philosophy

PO follows a **tool-based agent architecture**, making it easy to extend with new capabilities without modifying the core logic. This makes it ideal for experimentation, learning agentic AI systems, and building real-world automation tools.

---

## 👨‍💻 Author

Built with ❤️ by **Aryan Khokale**

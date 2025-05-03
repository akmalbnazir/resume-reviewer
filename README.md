# 🧠 Resume Reviewer & AI Interview Coach

This is a smart web-based application that uses **GPT-4.1** to analyze resumes and generate:
- 📋 **Detailed Feedback** (formatting, grammar, impact, structure, clarity, and job alignment)
- 🎯 **Tailored Interview Questions** (behavioral and technical)

The project leverages **Flask**, **OpenAI API**, and **TailwindCSS** to provide an interactive, clean, and responsive experience.

---

## ✨ Features

- Upload `.pdf` or `.docx` resume files
- Receive structured, actionable AI feedback
- Get AI-generated mock interview questions
- Clean, minimal UI with zero distractions
- Built-in .env support for secure API keys

---

## 🚀 Tech Stack

- **Backend**: Python, Flask, OpenAI SDK
- **Frontend**: HTML, TailwindCSS
- **AI**: GPT-4.1 (chat completions API)
- **Deployment Ready**: Easily deploy on Replit, Render, or any Flask-compatible host

---

## 📂 Project Structure

```
resume-reviewer/
│
├── app.py                      # Main Flask app
├── .env                        # Store your OpenAI API key
├── requirements.txt            # All dependencies
├── templates/
│   ├── index.html              # Upload page
│   └── result.html             # Feedback page
├── utils/
│   ├── resume_parser.py        # Resume text extraction (PDF/DOCX)
│   └── feedback_engine.py      # GPT-4.1 prompt + completion logic
└── static/                     # (Optional) static assets
```

---

## 🧪 Local Setup

1. **Clone the repository**  
```bash
git clone https://github.com/your-username/resume-reviewer.git
cd resume-reviewer
```

2. **Create a virtual environment**  
```bash
python -m venv venv
source venv/bin/activate     # On Windows: venv\Scripts\activate
```

3. **Install dependencies**  
```bash
pip install -r requirements.txt
```

4. **Create a `.env` file**  
```env
OPENAI_API_KEY=your-openai-api-key
```

5. **Run the app**  
```bash
python app.py
```

Then open `http://127.0.0.1:5000` in your browser.

---

## 🌐 Deployment Notes

- ✅ Works on Replit with a few adjustments to file paths and environment variables
- 🐳 Docker support can be added in future versions
- 🔐 Always keep `.env` files out of your Git commits (already excluded via `.gitignore`)

---

## 🛠 Future Improvements

- Multi-language resume support
- Resume scoring and keyword matching for ATS
- Exportable PDF reports
- LinkedIn integration (upload profile → review)

---

## 🤝 Contributions

Contributions are welcome!  
Please open a pull request or create an issue with ideas or bugs.

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

> Built by Akmal Nazir — designed to help candidates prepare smarter, not harder.

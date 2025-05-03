from flask import Flask, render_template, request
from utils.resume_parser import extract_resume_text
from utils.feedback_engine import generate_feedback, generate_interview_questions
from werkzeug.utils import secure_filename
import markdown
import os
import tempfile

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        uploaded_file = request.files.get("resume")
        if not uploaded_file or uploaded_file.filename == "":
            return render_template("index.html", error="No file selected.")

        # Save resume to a temporary file with correct suffix
        suffix = os.path.splitext(uploaded_file.filename)[1]
        with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
            uploaded_file.save(tmp.name)
            resume_text = extract_resume_text(tmp.name)

        # Generate feedback and interview questions
        feedback_md = generate_feedback(resume_text)
        questions_md = generate_interview_questions(resume_text)

        # Convert markdown to HTML
        feedback_html = markdown.markdown(feedback_md, extensions=["extra"])
        questions_html = markdown.markdown(questions_md, extensions=["extra"])

        # Clean up temp file
        os.remove(tmp.name)

        # Render result template with cleaned HTML
        return render_template("result.html", feedback=feedback_html, questions=questions_html)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

import json
import pdfkit
from jinja2 import Environment, FileSystemLoader

# Load resume JSON
with open("ResumeOutput.json", "r", encoding="utf-8") as f:
    resume_data = json.load(f)

# Load HTML template
env = Environment(
    loader=FileSystemLoader("."),
    autoescape=True
)
template = env.get_template("ResumeTemplate.html")

# Render HTML
rendered_html = template.render(**resume_data)

# Save HTML (debug-friendly)
with open("resume_rendered.html", "w", encoding="utf-8") as f:
    f.write(rendered_html)

# PDF configuration
options = {
    "encoding": "UTF-8",
    "page-size": "A4",
    "margin-top": "10mm",
    "margin-bottom": "10mm",
    "margin-left": "10mm",
    "margin-right": "10mm",
}

# Generate PDF
pdfkit.from_file(
    "resume_rendered.html",
    "Resume.pdf",
    options=options
)

print("✅ Resume PDF generated successfully")

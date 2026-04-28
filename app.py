from pathlib import Path

from flask import Flask, abort, render_template
from jinja2 import ChoiceLoader, FileSystemLoader


BASE_DIR = Path(__file__).resolve().parent
PAGES_DIR = BASE_DIR / "wiki" / "pages"
WIKI_DIR = BASE_DIR / "wiki"

RENDERABLE_PAGES = [
    "attributions",
    "contribution",
    "critical_mineral_conference",
    "description",
    "education",
    "engineering",
    "entrepreneurship",
    "hardware",
    "human-practices",
    "inclusivity",
    "industry-connection",
    "lab-notebook",
    "measurement",
    "members",
    "mining-integration",
    "model",
    "module-1",
    "module-2",
    "module-3",
    "notebook",
    "nsf-poster",
    "plant",
    "pulse-check",
    "results",
    "safety-and-security",
    "software",
    "sustainability",
]


app = Flask(__name__, static_folder="Static")
app.config.update(
    FREEZER_DESTINATION=str(BASE_DIR / "dist"),
    FREEZER_REMOVE_EXTRA_FILES=False,
    FREEZER_RELATIVE_URLS=True,
)
app.jinja_loader = ChoiceLoader(
    [
        FileSystemLoader(str(PAGES_DIR)),
        FileSystemLoader(str(WIKI_DIR)),
    ]
)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/page/<page>")
def pages(page: str):
    if page not in RENDERABLE_PAGES:
        abort(404)
    return render_template(f"{page}.html")


if __name__ == "__main__":
    app.run(debug=True, port=5000)

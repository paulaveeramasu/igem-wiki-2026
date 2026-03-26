from pathlib import Path

from flask import Flask, abort, render_template
from jinja2 import ChoiceLoader, FileSystemLoader


BASE_DIR = Path(__file__).resolve().parent
PAGES_DIR = BASE_DIR / "wiki" / "pages"
WIKI_DIR = BASE_DIR / "wiki"


app = Flask(__name__, static_folder="Static")
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
    template_name = f"{page}.html"
    if not (PAGES_DIR / template_name).exists():
        abort(404)
    return render_template(template_name)


if __name__ == "__main__":
    app.run(debug=True, port=5000)

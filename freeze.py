import shutil
from pathlib import Path

from flask_frozen import Freezer

from app import BASE_DIR, RENDERABLE_PAGES, app


freezer = Freezer(app)
DIST_DIR = Path(app.config.get("FREEZER_DESTINATION", BASE_DIR / "dist"))


@freezer.register_generator
def pages():
    for page in sorted(set(RENDERABLE_PAGES)):
        yield {"page": page}


def clean_dist() -> None:
    if DIST_DIR.exists():
        shutil.rmtree(DIST_DIR)


if __name__ == "__main__":
    clean_dist()
    freezer.freeze()

from flask_frozen import Freezer

from app import RENDERABLE_PAGES, app


freezer = Freezer(app)


@freezer.register_generator
def pages():
    for page in RENDERABLE_PAGES:
        yield {"page": page}


if __name__ == "__main__":
    freezer.freeze()

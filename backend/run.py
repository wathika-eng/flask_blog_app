# import from the blogapp __init__.py
from blogapp import app, db

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, load_dotenv=True)

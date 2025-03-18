from flask import Flask, request, jsonify
from extensions import pgdb
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
pgdb.init_app(app)

@app.route("/stories")
def get_stories():
    try:
        with pgdb.get_cursor() as cursor:
            cursor.execute("SELECT id, title, text, created_at FROM public.\"Stories\";")
            rows = cursor.fetchall()
            return jsonify(rows)
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route("/words")
def get_words():
    try:
        with pgdb.get_cursor() as cursor:
            cursor.execute("SELECT id, word, created_at FROM public.\"Words\";")
            rows = cursor.fetchall()
            return jsonify(rows)
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run()
from flask import Flask, render_template, request, redirect, url_for
from pathlib import Path
from isolate import isolate_song

UPLOAD_FOLDER = "uploads"

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

Path(UPLOAD_FOLDER).mkdir(exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files.get("song")
        if file:
            filepath = Path(app.config['UPLOAD_FOLDER']) / file.filename
            file.save(filepath)

            try:
                stems = isolate_song(filepath)

            except Exception as e:
                return f"Error during separation: {e}", 500

            return f"Separation complete! Files saved: {[s.name for s in stems]}"
        else:
            return f"No file uploaded.", 400
        
    return """
        <h1>Song Isolator</h1>
        <form method="Post" enctype="multipart/form-data"> 
            <input type="file" name="song" accept=".mp3"/>
            <button type="submit">Upload & Separate</button>
        </form>
        """

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template, request, redirect, url_for, send_from_directory
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

            folder_name = stems[0].parent.name if stems else ""
            return redirect(url_for("results", folder=folder_name))
        else:
            return f"No file uploaded.", 400
        
    return render_template("index.html")

@app.route("/results/<folder>")
def results(folder):
    folder_path = Path("static/stems") / folder
    files = [f.name for f in folder_path.glob("*")]

    links = ""
    for file in files:
        links += f'<li><a href="/download/{folder}/{file}">{file}</a></li>'

    return render_template("results.html", files=files, folder=folder)

@app.route("/download/<folder>/<filename>")
def download_file(folder, filename):
    return send_from_directory(
        Path("static/stems") / folder,
        filename,
        as_attachment=True
    )


if __name__ == "__main__":
    app.run(debug=True)

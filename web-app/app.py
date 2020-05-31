
from flask import Flask, render_template, request, redirect, url_for, send_file
from geocoder import GeoCoder
import storage_service


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=['POST'])
def upload():
    try:
        if request.method == 'POST':
            f = request.files['file']
            storage_service.store(f.filename, GeoCoder(f))
            return redirect(url_for('success_upload', filename= f.filename))
    except:
        return redirect(url_for('error'))

@app.route("/success")
def success_upload():
    try:
        filename = request.args.get('filename', '')
        geocoder = storage_service.retrieve(filename)
        return render_template("success.html", text=geocoder.show_html_table(), filename=filename)
    except:
        return redirect(url_for('error'))

@app.route("/download")
def download():
    filename = request.args.get('filename', '')
    geocoder = storage_service.retrieve(filename)
    return send_file(filename, attachment_filename=filename, as_attachment=True)

@app.route("/error")
def error():
    return render_template("error.html")

if __name__ == "__main__":
    app.debug = True
    app.run()
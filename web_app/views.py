from flask import render_template
from . import app
from jinja2  import TemplateNotFound



@app.route('/', defaults={'path': 'index.html'})
@app.route('/<path>')
def index(path):
    try:
        # Serve the file (if exists) from templates/FILE.html
        return render_template( path )
    except TemplateNotFound:
        return render_template('page-404.html'), 404

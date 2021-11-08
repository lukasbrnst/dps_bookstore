from flask import render_template, request, flash
import pandas as pd
from . import app, db
from jinja2  import TemplateNotFound
from .forms import BookForm, SearchForm
import sys
sys.path.append(__file__+"/..") 
from backend.db_tables import Book
from datetime import datetime




@app.route('/', defaults={'path': 'index.html'})
@app.route('/<path>')
def index(path):
    try:
        # Serve the file (if exists) from templates/FILE.html
        return render_template( path )
    except TemplateNotFound:
        return render_template('page-404.html'), 404


@app.route('/add_books/', methods=['GET', 'POST'])
def add_books():

    print(f"\n{[print(i) for i in request.form]}\n\n")

    form = BookForm(request.form,csrf_enabled=False)
    if request.method == 'POST' and form.validate:
        with app.app_context():
            # search = db.session.query(Books).filter(Books.id == request.form['submit_type']).first()
            try:
                date_published = datetime.strptime(form.date_published.data, "%m/%d/%Y").date()
            except:
                flash("Invalid date type. Please enter <mm:dd:yyyy>")
                return render_template( 'add_books.html' )

            search = db.session.query(Book)\
                .filter(Book.title == form.title.data)\
                .filter(Book.author == form.author.data)\
                .filter(Book.date_published == date_published)
            print(f"\nthis is search\n{search.all()}\n\n")

            if len(search.all())!=0:
                flash("Book already exists. Please add new books only.")
                return render_template( 'add_books.html' )


            new_book = Book(
                title = form.title.data,
                author = form.author.data,
                date_published = date_published
            )
            print(f"\nthis is new book\n{new_book}\n\n")

            try:
                db.session.add(new_book)
                db.session.commit()
            except:
                flash("Couldnt save book. Please check your input.")
                render_template( 'add_books.html' )

            flash("Successfully added book",category='message')

    for i in form.errors.values():
        flash(i[0],category='warning')


    return render_template( 'add_books.html' )


@app.route('/search_books/', methods=['GET', 'POST'])
def search_books():
    df_books_html = None
    form = SearchForm(request.form,csrf_enabled=False)
    if request.method == 'POST' and form.validate:
        if len(form.date_start.data)!=0:
            try:
                date_start = datetime.strptime(form.date_start.data, "%m/%d/%Y").date()
            except:
                flash("Invalid date type. Please enter <mm:dd:yyyy>")
                return render_template( 'search_books.html' )
        else:
            date_start = None
        if len(form.date_end.data)!=0:
            try:
                date_end = datetime.strptime(form.date_end.data, "%m/%d/%Y").date()
            except:
                flash("Invalid date end type. Please enter <mm:dd:yyyy>")
                return render_template( 'search_books.html' )
        else:
            date_end = None
        
        df_books = search_books_util(
            search_title=form.search_title.data,
            search_author=form.search_author.data,
            date_start=date_start,
            date_end=date_end)
        
        df_books = df_books[['title','author','date_published']]
        df_books_html = df_books.to_html(classes="table text-primary text-center",border=0,justify='center')

        
    for i in form.errors.values():
        flash(i[0],category='warning')


    return render_template('search_books.html', data_total=df_books_html)



def search_books_util(search_title,search_author,date_start,date_end):
    search_title = create_expression(search_title)
    search_author = create_expression(search_author)
    with app.app_context():
        search = db.session.query(Book)\
            .filter(Book.title.ilike(search_title))\
            .filter(Book.author.ilike(search_author))
        
        if date_start:
            search = search.filter(Book.date_published >= date_start)
        if date_end:
            search = search.filter(Book.date_published <= date_end)

    return pd.read_sql(search.statement, db.session.bind)

def create_expression(expr):
    if '*' in expr or '_' in expr: 
        expr_new = expr.replace('_', '__')\
                            .replace('*', '%')\
                            .replace('?', '_')
    elif expr is None:
        expr_new = '%'
    else:
        expr_new = '%{0}%'.format(expr)
    return expr_new
from app import app
from flask import render_template, request
from flaskext.markdown import Markdown
from app.forms import ProductForm
app.config['SECRET_KEY'] = "Tajemniczy_mysi_sprzęt"

Markdown(app)

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    content = ''
    with open('README.md', 'r', encoding='UTF-8') as f:
        content = f.read()
    return render_template('about.html', text = content)

@app.route('/extract')
def extract():
    if request.method == 'POST':
        return "Przesłano formularz"
    form = ProductForm()
    return render_template('extract.html', form = form)
   

@app.route('/products')
def products():
    pass

@app.route('/analyzer/<product_id>')
def analyzer():
    return "Podaj kod produktu do analizy"
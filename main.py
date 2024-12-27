from flask import Flask, render_template, request, redirect, url_for, jsonify, flash
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = 'Mr Phone'

# cofigure databases

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'web1'

mysql = MySQL(app)

@app.route('/')
def home():
    cur = mysql.connection.cursor()
    query = '''
    SELECT product.*, category.name_category 
    FROM product INNER JOIN category
    ON product.category = category.id_category
    '''
    cur.execute(query)
    product = cur.fetchall()
    return render_template('home.html', produk=product)

@app.route('/cekdata')
def cek_data():  
    cur = mysql.connection.cursor()
    cur.execute('SELECT 1')
    return jsonify({'message' : 'berhasil'})

@app.route('/product')
def homepage():
    cur = mysql.connection.cursor()
    query = '''
    SELECT product.*, category.name_category 
    FROM product INNER JOIN category
    ON product.category = category.id_category
    '''
    cur.execute(query)
    product = cur.fetchall()
    return render_template('product.html', produk=product)

@app.route('/card-product')
def card_product():
    cur = mysql.connection.cursor()
    query = 'SELECT * FROM product'
    cur.execute(query)
    product = cur.fetchall()
    return render_template('/layouts/component/card.html', produk=product)

@app.route('/add-product')
def add_product():
    cur = mysql.connection.cursor()
    query = '''
    SELECT product.*, category.name_category 
    FROM product INNER JOIN category
    ON product.category = category.id_category
    '''
    cur.execute(query)
    product = cur.fetchall()
    sql = 'SELECT * FROM category'
    cur.execute(sql)
    category = cur.fetchall()
    return render_template('add-product.html', produk=product, kategori=category)

@app.route('/save-product', methods=['POST'])
def save_product():
    name_product = request.form['name_product']
    image_URL = request.form['image_url']
    price = request.form['price']
    category = request.form['category']
    in_stok = request.form['in_stok']

    cur = mysql.connection.cursor()
    query = 'INSERT INTO product (name_product, image_url, price, category, in_stok) VALUES (%s, %s, %s, %s, %s)'
    cur.execute(query,(name_product, image_URL, price, category,in_stok))
    mysql.connection.commit()
    return redirect('/add-product')


@app.route('/about')
def aboutpage():
    return render_template('about.html')




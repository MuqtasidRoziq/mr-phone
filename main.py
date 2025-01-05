from flask import Flask, render_template, request, redirect, jsonify, flash, session
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = 'Mr Phone'

# cofigure databases
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root' 
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'web1'

mysql = MySQL(app)

# Route User Default
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
    return render_template('home.html', produk = product)

# Route User Admin
@app.route('/home-admin')
def home_admin():
    cur = mysql.connection.cursor()
    query = '''
    SELECT product.*, category.name_category 
    FROM product INNER JOIN category
    ON product.category = category.id_category
    '''
    cur.execute(query)
    product = cur.fetchall()
    return render_template('home.html', produk = product, admin = session.get('admin'))

# Route Login
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if not username or not password:
            flash('Semua field harus diisi!', 'error')
            return redirect('/login')
        
        cur = mysql.connection.cursor()
        query = 'SELECT * FROM login WHERE username = %s AND password = %s'
        cur.execute(query, (username, password))
        admin = cur.fetchone()

        if admin:
            session['admin'] = True
            return redirect('/home-admin')
        else:
            flash('Username atau Password salah', 'error')
            return redirect('/login')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

# Route cek koneksi
@app.route('/cekkoneksi')
def cek_data():  
    cur = mysql.connection.cursor()
    cur.execute('SELECT 1')
    return jsonify({'message' : 'berhasil'})

# Route Rupiah
@app.template_filter('rupiah')
def format_rupiah(value):
    return f"{value:,}".replace(',', '.')

# Route produk
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

# route card product
@app.route('/card-product')
def card_product():
    cur = mysql.connection.cursor()
    query = 'SELECT * FROM product'
    cur.execute(query)
    product = cur.fetchall()
    return render_template('/layouts/component/card.html', produk=product)

# route add product
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

# route save product in add product
@app.route('/save-product', methods=['POST'])
def save_product():
    name_product = request.form['name_product']
    image_URL = request.form['image_url']
    price = request.form['price']
    category = request.form['category']
    in_stok = request.form['in_stok']
    deskripsi = request.form['deskripsi']
    cur = mysql.connection.cursor()
    query = 'INSERT INTO product (name_product, image_url, price, category, in_stok, detail_product) VALUES (%s, %s, %s, %s, %s, %s)'
    cur.execute(query,(name_product, image_URL, price, category,in_stok, deskripsi))
    mysql.connection.commit()
    flash('Product berhasil disimpan', 'success')
    return redirect('/add-product')

# roiute save update product in edit product
@app.route('/update-product/<int:id>', methods=['POST'])
def update_product(id):
    name_product = request.form['name_product']
    image_URL = request.form['image_url']
    price = request.form['price']
    category = request.form['category']
    in_stok = request.form['in_stok']
    deskripsi = request.form['deskripsi']
    cur = mysql.connection.cursor()
    query = '''UPDATE product SET 
    name_product = %s, 
    image_url = %s, 
    price = %s, 
    category = %s, 
    in_stok = %s, 
    detail_product = %s 
    WHERE id = %s'''
    cur.execute(query,(name_product, image_URL, price, category, in_stok, deskripsi, id))
    mysql.connection.commit()
    flash('Produk berhasil diupdate', 'success')
    return redirect('/add-product')

# route delete product
@app.route('/delete-product/<int:id>')
def delete_product(id):
    try:
        cur = mysql.connection.cursor()
        query = 'DELETE FROM product WHERE id = %s'
        cur.execute(query, [id])
        mysql.connection.commit()
        flash('Produk berhasil dihapus', 'success')
    except Exception as e:
        flash(f'Produk gagal dihapus {str(e)}', 'error')
    return redirect('/add-product')    

# route about
@app.route('/about')
def aboutpage():
    return render_template('about.html')

# route detail product
@app.route('/detail-produk/<int:id>')
def detail_produk(id):
    cur = mysql.connection.cursor()
    query_detail = 'SELECT * FROM product WHERE id = %s'
    cur.execute(query_detail, [id])
    product_detail = cur.fetchone()
    query_produk =  '''
    SELECT product.*, category.name_category 
    FROM product INNER JOIN category
    ON product.category = category.id_category
    '''
    cur.execute(query_produk)
    produk = cur.fetchall()
    return render_template('detail-product.html', detail=product_detail, produk=produk)

# route search
@app.route('/search')
def search():
    keyword = request.args.get('keyword', '')
    if not keyword:
        return redirect('/product')
    cur = mysql.connection.cursor()
    query = "SELECT * FROM product WHERE name_product LIKE %s"
    cur.execute(query, ('%' + keyword + '%',))
    search_results = cur.fetchall()
    return render_template('search.html', produk=search_results, keyword=keyword)
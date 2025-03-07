from flask import Flask, render_template
import pandas as pd
from dashboard import (
    load_data, top_products_chart, 
    category_sales_chart, store_sales_chart, profit_margin_chart,
)

app = Flask(__name__)

# Load Data
df = load_data()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/charts/top-products")
def top_products():
    return top_products_chart(df)

@app.route("/charts/category-sales")
def category_sales():
    return category_sales_chart(df)

@app.route("/charts/store-sales")
def store_sales():
    return store_sales_chart(df)

@app.route("/charts/profit-margin")
def profit_margin():
    return profit_margin_chart(df)

if __name__ == "__main__":
    app.run(debug=True)

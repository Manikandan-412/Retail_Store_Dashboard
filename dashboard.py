import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt
import io
import base64

# Load CSV data
def load_data(csv_file="data/sales_data.csv"):
    df = pd.read_csv(csv_file, parse_dates=["Date"])
    return df

# Apply a consistent purple theme
color_theme = "Purples"

# Horizontal Bar Chart for Top 5 Products
def top_products_chart(df):
    top_products = df.groupby("Product Name")["Quantity Sold"].sum().nlargest(5).reset_index()
    fig = px.bar(top_products, x="Quantity Sold", y="Product Name", 
                 title="Top 5 Best-Selling Products", orientation='h', 
                 color="Quantity Sold", color_continuous_scale=color_theme)
    return fig.to_json()

# Pie Chart for Category Sales
def category_sales_chart(df):
    category_sales = df.groupby("Category")["Sales Revenue"].sum().reset_index()
    fig = px.pie(category_sales, names="Category", values="Sales Revenue", 
                 title="Sales by Category", color_discrete_sequence=px.colors.sequential.Purples)
    return fig.to_json()

# Stacked Bar Chart for Store Sales
def store_sales_chart(df):
    store_sales = df.groupby(["Store Location", "Category"])["Sales Revenue"].sum().reset_index()
    fig = px.bar(store_sales, x="Store Location", y="Sales Revenue", color="Category",
                 title="Sales by Store Location", barmode="stack", color_continuous_scale=color_theme)
    return fig.to_json()

# Scatter Plot for Profit Margin by Category
def profit_margin_chart(df):
    df["Profit Margin"] = (df["Profit/Loss"] / df["Sales Revenue"]) * 100
    avg_profit_margin = df.groupby("Category")["Profit Margin"].mean().reset_index()
    fig = px.scatter(avg_profit_margin, x="Category", y="Profit Margin", 
                     title="Profit Margin by Category", size="Profit Margin",
                     color="Profit Margin", color_continuous_scale=color_theme)
    return fig.to_json()
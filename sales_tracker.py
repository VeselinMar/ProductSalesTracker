import csv
import datetime
import matplotlib.pyplot as plt
from collections import Counter



# create mapping
product_data = {
    "P001": ["Running Shoes", 120],
    "P002": ["Basketball Sneakers", 150],
    "P003": ["Casual Sneakers", 80],
    "P004": ["Hiking Boots", 140],
    "P005": ["Slip-On Sneakers", 70],
    "P006": ["High-Top Sneakers", 110],
    "P007": ["Trail Running Shoes", 130],
    "P008": ["Tennis Shoes", 90],
    "P009": ["Soccer Cleats", 160],
    "P010": ["Skateboarding Shoes", 100],
}

csv_data = []

# open product_sales data and close when finished
# strip product ids of trailing newline chars
with open("product_sales.txt", "r") as file:
    product_ids = [line.strip() for line in file.readlines()]

# count sales per product
sales_count = Counter(product_ids)

# fetch date
current_date = datetime.datetime.today()

# go through product_ids and extract needed data
for sale_id, product_id in enumerate(product_ids, start=1):
    product_name = product_data[product_id][0]
    product_price = product_data[product_id][1]


    row = [current_date, sale_id, product_name, product_id, product_price]
    # append into csv_data list
    csv_data.append(row)


# create csv file and close when finished
with open("product_sales.csv", "w", newline="") as csv_file:
    csv_writer = csv.writer(csv_file)

    csv_writer.writerow(['Current Date', 'Sale ID', 'Product ID', 'Product Name', 'Product Price'])

    csv_writer.writerows(csv_data)

# prepare data for visualization
product_names = [product_data[pid][0] for pid in sales_count.keys()]
sales_numbers = list(sales_count.values())

# Plot bar chart
plt.figure(figsize=(10, 5))
plt.bar(product_names, sales_numbers, color='royalblue')
plt.xlabel("Products")
plt.ylabel("Number of Sales")
plt.title("Sales Statistics")
plt.xticks(rotation=45)
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()
plt.show()

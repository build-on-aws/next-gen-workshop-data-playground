import matplotlib.pyplot as plt
import pandas as pd

# Load the dataset
df = pd.read_csv("data/sample_click_stream_data.csv")

# 1. Device Type Distribution Graph
device_counts = df['devicetype'].value_counts()
plt.title('Device Type Distribution')
# TODO: Create a pie chart showing the distribution of device types


# TODO: Clear plot


# 2. Product Type Popularity
product_counts = df[df["product_type"] != "N/A"]["product_type"].value_counts()
plt.title('Product Type Popularity')
# TODO: Create a bar graph showing the popularity of different product types
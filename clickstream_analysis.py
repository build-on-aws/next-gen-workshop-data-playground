import matplotlib.pyplot as plt
import pandas as pd

# Load the dataset
df = pd.read_csv("data/sample_click_stream_data.csv")

# 1. Device Type Distribution Graph
device_counts = df['devicetype'].value_counts()
plt.title('Device Type Distribution')
# TODO insert comments


# Clear plot
plt.clf()

# 2. Product Type Popularity
product_counts = df[df["product_type"] != "N/A"]["product_type"].value_counts()
plt.title('Product Type Popularity')
# TODO insert comments

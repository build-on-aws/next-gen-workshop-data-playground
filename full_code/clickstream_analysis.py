import matplotlib.pyplot as plt
import pandas as pd

# Load the dataset
df = pd.read_csv("data/sample_click_stream_data.csv")

# 1. Device Type Distribution Graph
device_counts = df['devicetype'].value_counts()
plt.title('Device Type Distribution')
# TODO: Create a pie chart showing the distribution of device types
plt.pie(device_counts, labels=device_counts.index, autopct='%1.1f%%')
plt.tight_layout()
plt.legend(loc='upper left')
plt.savefig('device_types.png', bbox_inches='tight')

# clear plot
plt.clf()

# 2. Product Type Popularity
product_counts = df[df["product_type"] != "N/A"]["product_type"].value_counts()
plt.title('Product Type Popularity')
# TODO: Create a bar graph showing the popularity of different product types
plt.bar(product_counts.index, product_counts)
plt.xticks(rotation=45)
plt.xlabel('Product Type')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig('proudct_types.png', bbox_inches='tight')

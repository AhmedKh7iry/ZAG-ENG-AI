import os
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns
import textwrap 

path = r"c:\Users\lap shop\Downloads\Amazon Project\Amazon Project\amazon.csv"

if not os.path.exists(path):
    print("File not found:", path)
    raise SystemExit(1)


df = pd.read_csv(path)

print(df.head())
print("Shape:", df.shape)
print("Columns:\n", df.columns)
print(df.info())
print(df.isnull().sum())

df['discounted_price'] = df['discounted_price'].str.replace('₹','', regex=False)
df['discounted_price'] = df['discounted_price'].str.replace(',','', regex=False)
df['discounted_price'] = pd.to_numeric(df['discounted_price'], errors='coerce')

df['actual_price'] = df['actual_price'].str.replace('₹','', regex=False)
df['actual_price'] = df['actual_price'].str.replace(',','', regex=False)
df['actual_price'] = pd.to_numeric(df['actual_price'], errors='coerce')

df['discount_percentage'] = df['discount_percentage'].str.replace('%','', regex=False)
df['discount_percentage'] = pd.to_numeric(df['discount_percentage'], errors='coerce')

df['rating'] = pd.to_numeric(df['rating'], errors='coerce')

df['rating_count'] = df['rating_count'].str.replace(',','', regex=False)
df['rating_count'] = pd.to_numeric(df['rating_count'], errors='coerce')

df['rating_count'] = df['rating_count'].fillna(0)

df['actual_price'] = df['actual_price'].fillna(df['actual_price'].median())
df['discounted_price'] = df['discounted_price'].fillna(df['discounted_price'].median())
df['discount_percentage'] = df['discount_percentage'].fillna(df['discount_percentage'].median())

print("After Cleaning:")
print(df.info())

print("Average Actual Price:", df['actual_price'].mean())
print("Average Discounted Price:", df['discounted_price'].mean())
print("Max Price:", df['actual_price'].max())
print("Min Price:", df['actual_price'].min())

print("\nTop 5 Most Expensive Products:\n")
print(df.sort_values(by='actual_price', ascending=False)[['product_name','actual_price']].head())

print("\nTop 5 Cheapest Products:\n")
print(df.sort_values(by='actual_price', ascending=True)[['product_name','actual_price']].head())

category_price = df.groupby('category')['actual_price'].mean().sort_values(ascending=False)

print("\nAverage Price per Category:\n")
print(category_price.head(10))

df["price_gap"] = df["actual_price"] - df["discounted_price"]
df["sales_score"] = df["rating"] * df["rating_count"]

top_demand_categories = (
    df.groupby("category")["sales_score"]
    .mean()
    .sort_values(ascending=False)
)

print(top_demand_categories.head(10))

correlation = df["actual_price"].corr(df["rating"])
print("Correlation between price and rating:", correlation)

correlation = df["actual_price"].corr(df["rating"])
print("Correlation between price and rating:", correlation)

import matplotlib.pyplot as plt
import seaborn as sns
import os

sns.set(style="whitegrid")
os.makedirs('outputs', exist_ok=True)  # للتأكد من وجود مجلد لحفظ الصور

import matplotlib.pyplot as plt
import seaborn as sns
import os

sns.set(style="whitegrid")
os.makedirs('outputs', exist_ok=True)

top10 = df.groupby('category')['actual_price'].mean().sort_values(ascending=False).head(10).reset_index()
top10.rename(columns={'actual_price':'avg_price'}, inplace=True)

import textwrap
top10['short_cat'] = top10['category'].apply(lambda x: x.split('|')[-1])
top10['short_cat_wrapped'] = top10['short_cat'].astype(str).apply( lambda s: '\n'.join(textwrap.wrap(s, width=12)))
plt.xticks(rotation=25, ha='right', fontsize=10)

fig, ax = plt.subplots(figsize=(12,6))
bars = ax.bar(top10['short_cat_wrapped'], top10['avg_price'], color='skyblue', alpha=0.9)

ax.set_title('Top 10 Categories by Average Price', fontsize=16)
ax.set_ylabel('Average Price (₹)', fontsize=12)

plt.xticks(rotation=30, ha='right', fontsize=11)
plt.tight_layout()
plt.subplots_adjust(bottom=0.40)  
for bar in bars:
    h = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, h + h*0.01, f'₹{int(h):,}', ha='center', va='bottom', fontsize=9)

insights_lines = [f"{i+1}. {row['category']} — avg ₹{int(row['avg_price']):,}" for i, row in top10.iterrows()]
insights_text = "\n".join(insights_lines)
fig.text(0.5, 0.01, insights_text, ha='center', va='bottom', fontsize=8)

plt.savefig('outputs/top10_categories_price_with_insights.png', dpi=300, bbox_inches='tight')
plt.show()

df['short_name'] = df['product_name'].str.split().apply(
    lambda words: ' '.join(words[:3]) if isinstance(words, list) and len(words) > 0 else (words if isinstance(words, str) else ''))

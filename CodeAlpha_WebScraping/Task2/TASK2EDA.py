# Step 1: loading the csv file we extracted previously

import pandas as pd

df=pd.read_csv('books.csv') 
print(df.head())

# Step 2: checking structure & data types
print(df.info())

# step 3: Data cleaning

# cleaning price column
df['Price'] = df['Price'].str.replace('£', '').astype(float)

# cleaning rating column
rating_map = {
    'One': 1,
    'Two': 2,
    'Three': 3,
    'Four': 4,
    'Five': 5
}
df['Rating'] = df['Rating'].map(rating_map)

# cleaning availability column
df['Availability'] = df['Availability'].str.contains('In stock')

# Step 4: Descriptive statistics
print(df.describe()) 

# step 5: Identify patterns & trends

# Average price by rating
avg_price_by_rating = df.groupby('Rating')['Price'].mean()
print(avg_price_by_rating)

# most common rating
most_common_rating = df['Rating'].value_counts()
print(f'Most common rating: {most_common_rating}')


# step6: Data visualization

import matplotlib.pyplot as plt

# Price distribution

plt.hist(df['Price'], bins=20, edgecolor='black')
plt.title('Price Distribution of Books')
plt.xlabel('Price (£)')
plt.ylabel('Number of Books')
plt.show()

# Rating distribution vrs price
import seaborn as sns
sns.boxplot(x='Rating', y='Price', data=df)
plt.title('Book Price vs Rating')
plt.xlabel('Rating')
plt.ylabel('Price (£)')     
plt.show()

# step 7: Detect anomalies & issues
# Check for missing values
print(df.isnull().sum())
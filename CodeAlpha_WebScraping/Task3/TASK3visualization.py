# STEP 1: Lets Decide What to Visualize
# - Price distribution of books
# - Rating distribution of books
# - Avg Price by Rating
# - Availability of books


# STEP 2 : Prepare the data
import requests
import pandas as pd 
df = pd.read_csv('books.csv')

# converting price to numeric
df['Price'] = df['Price'].str.replace('£', '').astype(float)

# converting rating to numeric
rating_map = { 
    'One': 1,
    'Two': 2,
    'Three': 3,
    'Four': 4,
    'Five': 5
}   
df['Rating'] = df['Rating'].map(rating_map)

# converting availability to boolean
df['Availability'] = df['Availability'].str.contains('In stock')  

# STEP 3: Visualize the data
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style('whitegrid')

# 1. Price distribution  
sns.histplot(df['Price'], bins=20)
plt.title('Price Distribution of Books')
plt.xlabel('Price (£)')
plt.ylabel('Number of Books')
plt.show()

# 2. Rating distribution
plt.figure(figsize=(8, 5))
sns.countplot(x='Rating', data=df,order=['one', 'Two', 'Three', 'Four', 'Five'])
plt.title('Rating Distribution of Books ')
plt.xlabel('Rating')
plt.ylabel('Number of Books by Rating')
plt.show()

# 3. Avg Price by Rating
avg_price=df.groupby('Rating')['Price'].mean().reindex(['One', 'Two', 'Three', 'Four', 'Five'])
plt.figure(figsize=(8, 5))
avg_price.plot(kind='bar')
plt.title('Average Price ')
plt.xlabel('Rating')
plt.ylabel('Average Price (£)')
plt.xticks(rotation=0)
plt.show()

# 4. Availability of books
plt.figure()
sns.countplot(x='Availability', data=df)
plt.xlabel('Availability')
plt.ylabel('Count')
plt.title('Book Availability Status')
plt.show()

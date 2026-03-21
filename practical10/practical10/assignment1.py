import pandas as pd

# Read CSV file
df = pd.read_csv("books.csv")

# a) Complete report
print("\n--- Complete Book Report ---")
print(df)

# b) Books by given author
author_name = input("\nEnter author name: ")
print("\nBooks by", author_name)
print(df[df['author'] == author_name])

# c) Books by publisher
publisher_name = input("\nEnter publisher name: ")
print("\nBooks by publisher:", publisher_name)
print(df[df['publisher'] == publisher_name])

# d) Cheapest and Costliest book
cheapest = df[df['price'] == df['price'].min()]
costliest = df[df['price'] == df['price'].max()]

print("\nCheapest Book:")
print(cheapest['title'])

print("\nCostliest Book:")
print(costliest['title'])

# e) Sort by year
print("\nBooks sorted by Year:")
print(df.sort_values(by='year'))
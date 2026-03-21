import pandas as pd

# Create DataFrame
data = {
    "State": ["Maharashtra", "Gujarat", "Rajasthan", "Uttar Pradesh", "Karnataka"],
    "Area": [307713, 196024, 342239, 243286, 191791],   # in sq km
    "Population": [124000000, 68000000, 81000000, 240000000, 70000000]
}

df = pd.DataFrame(data)

# a) Complete info
print("\n--- State Information ---")
print(df)

# b) Largest Area
largest_area = df[df['Area'] == df['Area'].max()]
print("\nState with Largest Area:")
print(largest_area['State'])

# c) Largest Population
largest_pop = df[df['Population'] == df['Population'].max()]
print("\nState with Largest Population:")
print(largest_pop['State'])

# d) Population Density
df['Density'] = df['Population'] / df['Area']
print("\n--- With Population Density ---")
print(df)

# e) Highest Density
highest_density = df[df['Density'] == df['Density'].max()]
print("\nState with Highest Population Density:")
print(highest_density['State'])
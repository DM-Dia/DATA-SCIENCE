import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

# Load the dataset into a Pandas DataFrame
df = pd.read_csv("/root/Sport car price.csv")
df["Price (in USD)"] = df["Price (in USD)"].str.replace(",", "").astype(float)
print("First 5 rows of the dataset:")
print(df.head())

# 2. Data Cleaning
df = df.drop_duplicates()  # Remove duplicates
df = df.dropna()

# 3. Compute summary statistics
summary_stats = df.describe()
print("\nSummary Statistics:")
print(summary_stats)

# 4. Group by car make and compute the average price
avg_price_by_make = df.groupby("Car Make")["Price (in USD)"].mean()
print("\nAverage price by car make:")
print(avg_price_by_make)

# 6. Scatter plot of price vs horsepower with regression line
plt.figure(figsize=(10, 6))
sns.scatterplot(x=df["Horsepower"], y=df["Price (in USD)"], alpha=0.7)

print(df.columns)

df.rename(columns=lambda x: x.strip(), inplace=True)  # Removes extra spaces
df.rename(columns={"horsepower": "Horsepower"}, inplace=True)

print(df.dtypes)

df["Horsepower"] = pd.to_numeric(df["Horsepower"], errors="coerce")  # Convert to numeric
df["Year"] = pd.to_numeric(df["Year"], errors="coerce")

print(df["Horsepower"].isnull().sum())

df["Year"] = pd.to_numeric(df["Year"], errors="coerce")
df["Horsepower"] = pd.to_numeric(df["Horsepower"], errors="coerce")

# Group and compute mean horsepower by year
avg_hp_by_year = df.groupby("Year")["Horsepower"].mean()

print("\nAverage horsepower by year:")
print(avg_hp_by_year)

df_cleaned = df.dropna(subset=["Horsepower", "Price (in USD)"])
plt.figure(figsize=(8, 5))
sns.scatterplot(x=df["Horsepower"], y=df["Price (in USD)"], color="blue", label="Cars")

# Linear Regression
X = df["Horsepower"].values.reshape(-1, 1)
y = df["Price (in USD)"].values.reshape(-1, 1)
model = LinearRegression()
model.fit(X, y)
y_pred = model.predict(X)

# Plot regression line
plt.plot(df["Horsepower"], y_pred, color="red", label="Regression Line")

plt.xlabel("Horsepower")
plt.ylabel("Price (in USD)")
plt.title("Scatter Plot of Price vs. Horsepower")
plt.legend()
plt.show()

df["0-60 MPH Time (seconds)"] = pd.to_numeric(df["0-60 MPH Time (seconds)"], errors="coerce")

# Create a histogram with bins of size 0.5
plt.figure(figsize=(8, 5))
plt.hist(df["0-60 MPH Time (seconds)"], bins=np.arange(df["0-60 MPH Time (seconds)"].min(),
                                                        df["0-60 MPH Time (seconds)"].max() + 0.5,
                                                        0.5), edgecolor="black", color="skyblue")

plt.xlabel("0-60 MPH Time (seconds)")
plt.ylabel("Frequency")
plt.title("Histogram of 0-60 MPH Time")
plt.show()

#6. Filter cars with price > $500,000 and sort by Horsepower (descending)
filtered_df = df[df["Price (in USD)"] > 500000].sort_values(by="Horsepower", ascending=False)

# 7. Export cleaned dataset to CSV
df.to_csv("cleaned_cars_dataset.csv", index=False)
print("Cleaned dataset exported as 'cleaned_cars_dataset.csv'.")

# Print filtered dataset if any cars match the criteria
if not filtered_df.empty:
    print("\nCars with price > $500,000 sorted by Horsepower:")
    print(filtered_df)
else:
    print("\nNo cars found with price > $500,000.")
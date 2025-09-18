import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
try:
    iris = load_iris(as_frame=True)
    df = iris.frame  
    print("Iris dataset loaded successfully!")
except FileNotFoundError:
    print("Error: Dataset file not found!")
except Exception as e:
    print("An error occurred while loading the dataset:", e)
print("\nFirst 5 rows of the dataset:")
print(df.head())

print("\nDataset info:")
print(df.info())

print("\nMissing values in each column:")
print(df.isnull().sum())

df = df.dropna()  
#2

print("\nBasic Statistics:")
print(df.describe())

grouped = df.groupby("target").mean()
print("\nMean values grouped by species:")
print(grouped)

df["species"] = df["target"].map(dict(enumerate(iris.target_names)))
print("\nDataset with species column added:")
print(df.head())

print("\nAverage petal length per species:")
print(df.groupby("species")["petal length (cm)"].mean())

sns.set(style="whitegrid")

plt.figure(figsize=(8,5))
plt.plot(df.index, df["sepal length (cm)"], label="Sepal Length")
plt.title("Line Chart: Sepal Length Trend")
plt.xlabel("Index")
plt.ylabel("Sepal Length (cm)")
plt.legend()
plt.show()

plt.figure(figsize=(8,5))
sns.barplot(x="species", y="petal length (cm)", data=df, ci=None)
plt.title("Bar Chart: Average Petal Length by Species")
plt.xlabel("Species")
plt.ylabel("Petal Length (cm)")
plt.show()

plt.figure(figsize=(8,5))
plt.hist(df["sepal width (cm)"], bins=15, color="skyblue", edgecolor="black")
plt.title("Histogram: Sepal Width Distribution")
plt.xlabel("Sepal Width (cm)")
plt.ylabel("Frequency")
plt.show()

plt.figure(figsize=(8,5))
sns.scatterplot(x="sepal length (cm)", y="petal length (cm)", hue="species", data=df)
plt.title("Scatter Plot: Sepal Length vs Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend(title="Species")
plt.show()

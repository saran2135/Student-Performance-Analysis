# Pandas is used for data analysis
import pandas as pd

# NumPy is used for numerical calculations
import numpy as np

# Matplotlib is used for charts
import matplotlib.pyplot as plt

# Seaborn creates beautiful graphs
import seaborn as sns

# Read CSV file
df = pd.read_csv(r"D:\Python programs\StudentsPerformance .csv")
# SHOW FIRST 5 ROWS
print(df.head(5))
# Show total rows and columns
print(df.shape)
# Show data types
print(df.dtypes)
# CHECK MISSING VALUES
# isnull() checks missing values & sum() counts them
print(df.isnull().sum())
# Remove duplicate rows if available
df = df.drop_duplicates()
print(df)
# 2. Instead of filling with 0, we use the 'Median' (middle value)
df['math score'] = df['math score'].fillna(df['math score'].median())
df['reading score'] = df['reading score'].fillna(df['reading score'].median())
df['writing score'] = df['writing score'].fillna(df['writing score'].median())
#  For the education column, if it's empty, we label it 'Unknown'
# df['parental Level of education'] = df['parental Level of education'].fillna("Unknown")
df['parental level of education'] = df['parental level of education'].fillna("Unknown")
# STEP 3: CREATING NEW METRICS
# Calculate the total of all three subjects for every student
df['total marks'] = df['math score'] + df['reading score'] + df['writing score']
# Divide the total by 3 to get the average percentage
df['average marks'] = df['total marks'] / 3
print(df)
# DATA ANALYSIS
# Sort by highest marks and show the top 5
print(df.sort_values(by="total marks", ascending=False).head(5))
# Group by gender and find the average of their scores
print(df.groupby("gender")['total marks'].mean())
# VISUALIZATION
# Set a clean, professional look for our charts
sns.set_theme(style='whitegrid')
# Create a boxplot to show the spread of marks between genders
plt.figure(figsize=(10,6))
sns.boxplot(x="gender",y="total marks", data= df, palette="Set2")
plt.title("Score distribution by gender", fontsize =14)
plt.show()
# Save the clean data so the organization can use it in Excel
df.to_csv(df.to_csv(r"D:\Python programs\Report.csv", index=False))
print(df)

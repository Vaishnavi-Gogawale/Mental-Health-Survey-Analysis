# This connects your Python code to the data you just uploaded
df = pd.read_csv('mental_health_data.csv')

# 2. Basic Data Overview
print("--- Survey Overview ---")
print(f"Total Responses Collected: {len(df)}")
print(f"Number of Questions Asked: {len(df.columns)}")

# 3. List all questions (Columns)
print("\n--- Survey Questions analyzed ---")
for i, col in enumerate(df.columns):
    print(f"{i+1}. {col}")

# 4. Professional Summary
# This helps you check if there are any empty (null) responses
print("\n--- Data Quality Check ---")
print(df.isnull().sum())

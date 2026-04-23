pd.read_csv('mental_health_data.csv')

# This shows how many people took your survey
print("Total Survey Responses:", len(data))

# This shows the names of your survey questions
print("Survey Questions:", data.columns.tolist())

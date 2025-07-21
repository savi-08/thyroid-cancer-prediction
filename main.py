import joblib
import pandas as pd
from sklearn.preprocessing import LabelEncoder

model = joblib.load("models/rf_model.joblib")
columns = joblib.load("models/feature_columns.joblib")

df = pd.read_csv("data/dataset.csv")

df.rename(columns={"Hx Radiothreapy": "Hx Radiotherapy"}, inplace=True)

print("Choose input method:")
print("1. Manual input")
print("2. Random sample from dataset")
choice = input("Enter 1 or 2: ")

if choice == "1":
    sample_input = {}
    for col in columns:
        if df[col].dtype == 'int64':
            val = int(input(f"Enter value for {col}: "))
        else:
            options = df[col].dropna().unique().tolist()
            val = input(f"Enter value for {col} (options: {options}): ")
        sample_input[col] = val
    input_df = pd.DataFrame([sample_input])

elif choice == "2":
    sample = df.sample(1).reset_index(drop=True)
    input_df = sample.drop(columns=["Recurred"])
    print("\n🔍 Sampled Input:\n", input_df)

else:
    print("❌ Invalid choice. Exiting.")
    exit()

for col in input_df.columns:
    if input_df[col].dtype == 'object':
        le = LabelEncoder()
        le.fit(df[col].astype(str))
        input_df[col] = le.transform(input_df[col].astype(str))

input_df = input_df[columns]

prediction = model.predict(input_df)[0]

#Output
print("\n🎯 Prediction Result:")
if prediction == 1:
    print("⚠️ Cancer *WILL* Recur")
else:
    print("✅ Cancer *WILL NOT* Recur")
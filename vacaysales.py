import pandas as pd
import math
import os
import re
import pyperclip



# Load Excel
file_path = input("Enter the full file path (include double quotes if desired): ")
file_path = file_path.strip('"') 
df = pd.read_csv(file_path)

print(df.columns)


columns_to_round = ['Tourism fee', 'City / Tourism tax']

for col in columns_to_round:
    df[col] = df[col].apply(
        lambda v: 0 if pd.isnull(v) or v == 0
                  else round(v / 10) * 10
    )


df['Booking fee'] = df['Booking fee'] + df['Service fee']

import re

def clean_name(name):
    if pd.isnull(name):
        return name
    # Keep only letters (A-Z, a-z) and spaces
    cleaned = re.sub(r'[^A-Za-z ]+', '', str(name)).strip()
    return cleaned

df['Guest'] = df['Guest'].apply(clean_name)


# Save new file
new_file_path = os.path.splitext(file_path)[0] + "_modified.xlsx"
df.to_excel(new_file_path, index=False)

print("Modified file saved at:", new_file_path)

# Copy new file path to clipboard
clean_path = new_file_path.strip().strip('"').strip("'")
pyperclip.copy(clean_path)
print("Clean path copied:", clean_path)


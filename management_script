import pandas as pd
import pyperclip
from datetime import datetime


# Step 1: Ask user for CSV file path
file_path = input("Enter the full file path (with quotes if needed): ").strip('"')


# Step 2: Load CSV
df = pd.read_csv(file_path)


# Step 3: Ask user for month
target_month = int(input("Which month? (1-12): "))


# Cutoff = 01/<target_month>/2025
cutoff = pd.Timestamp(2025, target_month, 1)


# Debug: Show sample of raw data
print("\n--- DEBUG: Original Check-in date ---")
print(df["Check-in date"].head())
print(f"Data type: {df['Check-in date'].dtype}")


# Convert Check-in date using pandas (handles most formats automatically)
df["Check-in date"] = pd.to_datetime(
    df["Check-in date"], 
    format='mixed',  # Handles multiple date formats
    dayfirst=True,   # Assumes day comes before month
    errors='coerce'  # Invalid dates become NaT
)

print("\n--- DEBUG: After pd.to_datetime ---")
print(df["Check-in date"].head())


# Replace year with 2025 and apply cutoff
def apply_year_and_cutoff(date_val):
    if pd.isna(date_val):
        return date_val
    
    date_val = date_val.replace(year=2025)
    
    if date_val < cutoff:
        date_val = cutoff
    
    return date_val


df["Check-in date"] = df["Check-in date"].apply(apply_year_and_cutoff)


# Convert back to string format DD/MM/YYYY
df["Check-in date"] = df["Check-in date"].dt.strftime("%d/%m/%Y")


print("\n--- DEBUG: Final format ---")
print(df["Check-in date"].head())
print("--- END DEBUG ---\n")


# Copy Check-in date → Service fee
df["Service fee"] = df["Check-in date"]


# Save updated CSV
output_path = file_path.replace(".csv", "_updated.csv")
df.to_csv(output_path, index=False)


# Copy path to clipboard
pyperclip.copy(output_path)


print(f"✅ File saved as: {output_path}")
print(f"📋 File path copied to clipboard!")


if df["Check-in date"].isna().any():
    print(f"\n⚠️  Warning: {df['Check-in date'].isna().sum()} dates could not be parsed")

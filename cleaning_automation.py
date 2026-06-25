import pandas as pd

# Load raw data
data = pd.read_csv("raw_sales_data.csv")
data.columns = data.columns.str.strip()

print("Original data shape:", data.shape)

# Remove duplicate rows
data = data.drop_duplicates()

# Convert Sales and Quantity to numeric (handle 'abc' etc.)
data["Sales"] = pd.to_numeric(data["Sales"], errors="coerce")
data["Quantity"] = pd.to_numeric(data["Quantity"], errors="coerce")

# Fill missing values
data["Customer_Name"] = data["Customer_Name"].fillna("Unknown")
data["Region"] = data["Region"].fillna("Unknown")
data["Sales"] = data["Sales"].fillna(data["Sales"].mean())
data["Quantity"] = data["Quantity"].fillna(data["Quantity"].median())
data["Order_Date"] = data["Order_Date"].ffill()

# Create a simple report
summary = {
    "Total Orders": len(data),
    "Total Sales": data["Sales"].sum(),
    "Average Sales": data["Sales"].mean()
}

# Save cleaned data
data.to_csv("cleaned_sales_data.csv", index=False)

# Save summary report
report = pd.DataFrame(list(summary.items()), columns=["Metric", "Value"])
report.to_csv("summary_report.csv", index=False)

print("Cleaning complete ✅")
print("Cleaned data & report saved.")
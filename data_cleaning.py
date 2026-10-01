import pandas as pd

# ==========================================
# STEP 1: Load the raw dataset
# ==========================================

df = pd.read_csv("marketing_campaign.csv", sep="\t")

print("Original dataset shape:")
print(df.shape)


# ==========================================
# STEP 2: Handle missing values
# ==========================================

# Check and fill missing Income values with the median
income_median = df["Income"].median()

df["Income"] = df["Income"].fillna(income_median)

print("\nMissing Income values after cleaning:")
print(df["Income"].isnull().sum())


# ==========================================
# STEP 3: Check for duplicate rows
# ==========================================

duplicate_count = df.duplicated().sum()

print("\nNumber of duplicate rows:")
print(duplicate_count)


# ==========================================
# STEP 4: Standardize column names
# ==========================================

df.columns = df.columns.str.strip().str.lower()

print("\nCleaned column names:")
print(df.columns.tolist())


# ==========================================
# STEP 5: Convert date column to datetime
# ==========================================

df["dt_customer"] = pd.to_datetime(
    df["dt_customer"],
    format="%d-%m-%Y",
    errors="coerce"
)

print("\nDate column data type:")
print(df["dt_customer"].dtype)

print("\nInvalid/missing dates after conversion:")
print(df["dt_customer"].isnull().sum())

# ==========================================
# STEP 6: Check categorical values
# ==========================================

print("\nEducation values:")
print(df["education"].value_counts())

print("\nMarital status values:")
print(df["marital_status"].value_counts())

# ==========================================
# STEP 7: Inspect unusual marital status values
# ==========================================

unusual_statuses = ["Alone", "Absurd", "YOLO"]

print("\nRecords with unusual marital status values:")
print(df[df["marital_status"].isin(unusual_statuses)][
    ["id", "marital_status"]
])

# ==========================================
# STEP 8: Standardize unusual marital status values
# ==========================================

unusual_statuses = ["Alone", "Absurd", "YOLO"]

df["marital_status"] = df["marital_status"].replace(
    unusual_statuses,
    "Unknown"
)

print("\nMarital status values after cleaning:")
print(df["marital_status"].value_counts())

# ==========================================
# STEP 9: Check numerical data for outliers
# ==========================================

print("\nIncome statistics:")
print(df["income"].describe())

print("\nYear of birth range:")
print("Minimum:", df["year_birth"].min())
print("Maximum:", df["year_birth"].max())

# ==========================================
# STEP 10: Inspect suspicious values
# ==========================================

print("\nCustomer with highest income:")
print(df.loc[df["income"].idxmax()])

print("\nCustomers with very old birth years:")
print(df[df["year_birth"] < 1920][
    ["id", "year_birth", "income", "education", "marital_status"]
])

# ==========================================
# STEP 11: Handle suspicious values
# ==========================================

# Replace the extreme income value with the median income
income_median = df["income"].median()

df.loc[df["income"] == 666666, "income"] = income_median

# Replace unrealistic birth years with missing values
df.loc[df["year_birth"] < 1920, "year_birth"] = pd.NA

print("\nIncome after outlier treatment:")
print(df["income"].describe())

print("\nInvalid birth years after cleaning:")
print(df["year_birth"].isna().sum())

# ==========================================
# STEP 12: Final missing-value check
# ==========================================

print("\nMissing values in each column:")
print(df.isnull().sum())

# ==========================================
# STEP 13: Check data types
# ==========================================

print("\nData types after cleaning:")
print(df.dtypes)

# ==========================================
# STEP 14: Check for constant columns
# ==========================================

constant_columns = []

for column in df.columns:
    if df[column].nunique() == 1:
        constant_columns.append(column)

print("\nConstant columns:")
print(constant_columns)

# ==========================================
# STEP 15: Remove constant columns
# ==========================================

df = df.drop(columns=["z_costcontact", "z_revenue"])

print("\nDataset shape after removing constant columns:")
print(df.shape)

print("\nRemaining columns:")
print(df.columns.tolist())

# ==========================================
# STEP 16: Final validation
# ==========================================

print("\n========== FINAL VALIDATION ==========")

print("Final dataset shape:")
print(df.shape)

print("\nTotal duplicate rows:")
print(df.duplicated().sum())

print("\nTotal missing values:")
print(df.isnull().sum().sum())

print("\nFinal data types:")
print(df.dtypes)

# ==========================================
# STEP 17: Save cleaned dataset
# ==========================================

df.to_csv("cleaned_customer_personality.csv", index=False)

print("\nCleaned dataset saved successfully!")
print("File: cleaned_customer_personality.csv")

# ==========================================
# STEP 18: Verify saved cleaned dataset
# ==========================================

cleaned_df = pd.read_csv("cleaned_customer_personality.csv")

print("\n========== SAVED FILE VERIFICATION ==========")
print("Saved file shape:")
print(cleaned_df.shape)

print("\nSaved file duplicate rows:")
print(cleaned_df.duplicated().sum())

print("\nSaved file columns:")
print(cleaned_df.columns.tolist())
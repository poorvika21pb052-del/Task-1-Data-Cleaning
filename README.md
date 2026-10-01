# Task 1: Data Cleaning and Preprocessing

## Objective

The objective of this task is to clean and preprocess a raw customer dataset using Python and Pandas.

The dataset used for this project is the **Customer Personality Analysis** dataset. The cleaning process focuses on handling missing values, removing duplicate records, standardizing column names and categorical values, converting date formats, identifying and treating suspicious values and outliers, removing constant columns, and validating the final dataset.

The final output is a cleaned dataset that can be used for further data analysis.



## Dataset Information

- **Dataset:** Customer Personality Analysis
- **Source:** Kaggle
- **Original rows:** 2,240
- **Original columns:** 29
- **Final rows:** 2,240
- **Final columns:** 27
- **Main tool:** Python
- **Library used:** Pandas
- **Raw dataset file:** `marketing_campaign.csv`
- **Cleaned dataset file:** `cleaned_customer_personality.csv`

## Data Cleaning and Preprocessing

The following cleaning steps were performed using Python and Pandas:

1. **Handled missing values**
   - Identified missing values in the `Income` column.
   - Filled 24 missing income values using the median income.

2. **Checked for duplicate records**
   - Checked the complete dataset for duplicate rows.
   - No duplicate rows were found.

3. **Standardized column names**
   - Converted column names to lowercase.
   - Removed unnecessary spaces from column names.

4. **Converted date format**
   - Converted the `Dt_Customer` column from text format to a proper datetime format.
   - No invalid dates remained after conversion.

5. **Cleaned categorical values**
   - Inspected `Education` and `Marital_Status` categories.
   - Replaced unusual marital-status values such as `Alone`, `Absurd`, and `YOLO` with `Unknown`.

6. **Handled suspicious numerical values**
   - Identified an unusually high income value of `666666`.
   - Replaced this value with the median income.
   - Identified three unrealistic birth years below 1920 and converted them to missing values.

7. **Removed constant columns**
   - Identified `z_costcontact` and `z_revenue` as constant columns.
   - Removed these columns because they did not provide variation for analysis.

8. **Performed final validation**
   - Verified the final dataset shape.
   - Checked for duplicate rows.
   - Checked missing values.
   - Verified the final data types.


## Final Dataset Summary

After cleaning and preprocessing:

- **Rows:** 2,240
- **Columns:** 27
- **Duplicate rows:** 0
- **Missing Income values:** 0
- **Invalid dates:** 0
- **Missing values remaining:** 3
- **Missing values:** All 3 are in the `year_birth` column
- **Constant columns removed:** 2
- **Final date column type:** Datetime
- **Final cleaned file:** `cleaned_customer_personality.csv`

The cleaned dataset is ready for further analysis and visualization.

## Tools and Technologies

- **Python 3**
- **Pandas**
- **VS Code**
- **Git**
- **GitHub**

### Python Libraries

```python
import pandas as pd

## Project Structure

```text
Task-1-Data-Cleaning/
│
├── marketing_campaign.csv
├── cleaned_customer_personality.csv
├── data_cleaning.py
├── README.md
└── .gitignore
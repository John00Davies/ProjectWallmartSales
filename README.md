# Walmart Sales Data Analysis

This project analyzes Walmart's sales data by leveraging Python for data exploration and Excel for detailed analysis, KPI creation, and dashboard design. The objective is to extract valuable insights, track key performance indicators (KPIs), and provide actionable recommendations for improving sales performance.

## Table of Contents
- [Introduction](#introduction)
- [Data Collection](#data-collection)
- [Data Overview Using Python](#data-overview-using-python)
- [Analyzing Data and Creating KPIs in Excel](#analyzing-data-and-creating-kpis-in-excel)
- [Dashboard Creation](#dashboard-creation)
- [Conclusion](#conclusion)

## Introduction
Walmart's vast sales data provides an opportunity to analyze and understand customer behavior, sales trends, and inventory performance. This project uses Python for data cleaning and preliminary analysis, followed by Excel for in-depth exploration, KPI calculation, and visualization using interactive dashboards. The goal is to empower stakeholders with actionable insights for strategic decision-making.

## Data Collection
The dataset used in this project was sourced from the following repository:
[Walmart Sales Analysis](https://github.com/Princekrampah/WalmartSalesAnalysis/blob/master/WalmartSalesData.csv).

The dataset contains 1000 observations and 17 features, including:
- Invoice ID
- Branch
- City
- Customer Type
- Product Line
- Unit Price
- Quantity
- Total
- Date
- Time
- Payment Method
- Rating
- Gross Income

## Data Overview Using Python
Python was used for initial data exploration and cleaning. Below is the key code for loading and inspecting the dataset:

```python
import pandas as pd

# Load data
df = pd.read_csv('WalmartSalesData.csv', na_values='?')

# Preview data
df.head()

# Check data shape
df.shape  # (1000, 17)

# Check data types
df.dtypes

# Check for duplicated rows
df[df.duplicated()]

# Check for missing values
df.isna().sum()

# Check percentage of missing values
round(df.isna().sum().sum()) / df.size * 100, 1
## Analyzing Data and Creating KPIs in Excel
Once the data was cleaned in Python, it was exported to Excel for in-depth analysis and KPI creation.
```
## Analyzing Data and Creating KPIs in Excel
Once the data was cleaned in Python, it was exported to Excel for in-depth analysis and KPI creation.

### Key Activities:
- **Data Import and Structuring**: The dataset was structured using Excel's Pivot Tables to summarize sales by product categories, store locations, and time periods.
- **KPI Creation**: Key Performance Indicators such as sales growth rate, average transaction value, and inventory turnover were calculated using Excel formulas.

### KPIs:
- **Sales Growth Rate**
- **Average Transaction Value**
- **Gross Income by Product Line**
- **Sales by Branch**

## Dashboard Creation
A dynamic and interactive dashboard was created in Excel to visualize the findings effectively. The dashboard features:
- **Line Charts**: Sales trends over time.
- **Bar Charts**: Regional sales comparisons.

### Interactive Features:
- **Filters**: Enable users to explore sales data by different regions, product categories, and time frames.
- **Visual Representation**: Easy-to-understand charts and graphs highlight key insights.

[Link to Walmart Sales Dashboard](https://live.com)

## Technologies Used
- **Python**: For data exploration and cleaning (Pandas, NumPy).
- **Excel**: For KPI calculation, in-depth analysis, and dashboard creation.
- **Jupyter Notebooks**: For code execution and data manipulation.

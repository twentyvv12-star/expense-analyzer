# ACC102 Python Data Product – Interactive Analysis Tool
Track 4: Interactive Data Analysis Tool (Streamlit)

- Student ID: 2472322
- Student Name: Lingwei Zeng
- Submission Date: 23 April 2026

---

## 1. Project Overview
This is an individual mini-assignment for ACC102. I built a small interactive Python data tool using Streamlit to analyze department expense structures. The tool allows users to edit expense amounts, upload their own Excel files, view real-time pie charts, and export the report as an Excel file.

**Purpose**:
To help accounting students and small business managers quickly understand how different expense categories contribute to total costs through an easy-to-use web interface.

## 2. Dataset Information
1. Data Source: Manually created default dataset (users can upload their own Excel files)
2. Data Topic: Department expense categories (labor, material, rent, marketing, others)
3. Time Range: Not applicable (static snapshot)
4. Access Date: 20 April 2026
5. Main Variables: Expense Category (text), Amount (numeric), Proportion (%) (calculated)

## 3. Tools & Libraries Used
1. Python 3.13
2. Streamlit (1.51.0)
3. Pandas (2.2.3)
4. Plotly (6.3.0)
5. openpyxl (3.1.5)

## 4. How to Run This Tool
1. Clone or download this repository
2. Install required packages:pip install streamlit pandas plotly openpyxl
3. Run the app:streamlit run expense_analyzer.py
4. Open the local URL in your browser

## 5. Core Features
- Real-time editing of expense amounts with automatic pie chart and table updates
- Upload custom Excel files (two columns: category, amount) to replace default data
- Download current expense report as an Excel file with metadata (timestamp, total cost)
- User-friendly interface for non-technical users

## 6. Key Insights & Results
- Labor cost is the largest expense in the default dataset (over 40% of total).
- Users can perform "what-if" analysis (e.g., increasing marketing budget) and see proportion changes instantly.
- The tool supports custom data, making it adaptable to different business scenarios.

## 7. Project Structure
- Main Streamlit application: `expense_analyzer.py`
- Python dependencies: `requirements.txt`
- This document: `README.md`
- Jupyter notebook workflow: `expense_analysis.ipynb`

## 8. Limitations & Improvements
- Assumes uploaded Excel has exactly two columns (category, amount); no handling of missing values.
- Data is not saved permanently; refreshing the page resets to default.
- No history tracking or comparison between different scenarios.
- Future improvements: add database storage, multiple currency support, time‑series trends.

## 9. AI Use Disclosure
- AI Tool: DeepSeek (latest version), Doubao (latest version)
- Date Used: 15–22 April 2026
- Purpose: Provided project ideas, code structure guidance, debugging, error checking, deployment assistance, and reflection report structure. All final code and analysis decisions are my own.

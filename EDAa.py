#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import argparse
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(file_path):
    # Load data from various formats (CSV, Excel, SQL)
    if file_path.endswith('.csv'):
        data = pd.read_csv(file_path)
    elif file_path.endswith('.xlsx'):
        data = pd.read_excel(file_path)
    else:
        raise ValueError("Unsupported file format")

    return data

def handle_missing_values(data):
    # Fill missing values based on column data type
    for column in data.columns:
        if data[column].dtype == 'object':
            data[column].fillna('Unknown', inplace=True)  # Fill with 'Unknown' for categorical columns
        else:
            data[column].fillna(data[column].median(), inplace=True)  # Fill with median for numerical columns
    
    return data

def explore_data(data):
    # Create some exploratory charts
    for column in data.columns:
        if data[column].dtype == 'object':
            # For categorical columns, create a count plot
            plt.figure(figsize=(8, 6))
            sns.countplot(data=data, x=column)
            plt.title(f'{column} Count Plot')
            plt.xticks(rotation=45)
            plt.show()
        else:
            # For numerical columns, create a histogram
            plt.figure(figsize=(8, 6))
            sns.histplot(data=data, x=column, kde=True)
            plt.title(f'{column} Histogram')
            plt.show()

def main():
    # Get user input for data file
    file_path = input("Enter the path to the data file: ")

    # Load data
    try:
        data = load_data(file_path)
        print("Data loaded successfully.")
    except Exception as e:
        print("Error loading data:", e)
        return

    # Display the original data table
    display(data)  # In a Jupyter Notebook, this will render an interactive table
    
    # Preprocess data
    data = handle_missing_values(data)
    print("Missing values filled based on column type.")
    
    # Explore data with charts
    explore_data(data)

if __name__ == "__main__":
    main()


# In[ ]:





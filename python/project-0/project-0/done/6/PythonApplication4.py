import os
import pandas as pd
from nbformat import write as nbf_write
from nbformat import v4 as nbf
from IPython.display import display, Markdown
from tabulate import tabulate
import matplotlib.pyplot as plt

def sum_column_6(excel_file):
    try:
        df = pd.read_excel(excel_file)
        return df.iloc[2:, 5].sum()
    except Exception as e:
        print(f"Error reading {excel_file}: {e}")
        return None

def compare_excel_files(directory):
    data = {}
    for year_folder in os.listdir(directory):
        year_path = os.path.join(directory, year_folder)
        if os.path.isdir(year_path):
            excel_files = {}
            for excel_file in os.listdir(year_path):
                excel_path = os.path.join(year_path, excel_file)
                if excel_file.endswith('.xlsx'):
                    total_sum = sum_column_6(excel_path)
                    if total_sum is not None:
                        excel_files[excel_file.replace(" فرمت اکسل.xlsx", "").replace(" Daily.xlsx", "")] = total_sum
            if excel_files:
                data[year_folder] = excel_files
    return data

def check_trend(data):
    trends = {}
    for year, excel_files in data.items():
        for excel_file, total_sum in excel_files.items():
            if excel_file not in trends:
                trends[excel_file] = total_sum
            else:
                if total_sum > trends[excel_file]:
                    trends[excel_file] = total_sum
    
    # Sort the results based on the values
    sorted_trends = sorted(trends.items(), key=lambda item: item[1], reverse=True)
    return sorted_trends

def main():
    directory = r'C:\Users\rezan\OneDrive\Desktop\Kerman\Daily Data'
    results = compare_excel_files(directory)
    trends = check_trend(results)
    
    # Create a list of tuples containing the data
    table_data = [(excel_file, total_sum) for excel_file, total_sum in trends]

    # Convert the list of tuples to a Markdown table
    markdown_table = tabulate(table_data, headers=['Excel File', 'Total Sum'], tablefmt='pipe')

    # Display the Markdown table
    display(Markdown(markdown_table))

    # Extract Excel file names and total sums for plotting
    excel_files = [item[0] for item in trends]
    total_sums = [item[1] for item in trends]

    plt.figure(figsize=(10, 6))
    plt.bar(excel_files, total_sums, color='blue')
    plt.xlabel('نام محور')
    plt.ylabel('میزان تردد')
    plt.title('نمودار تردد')
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()

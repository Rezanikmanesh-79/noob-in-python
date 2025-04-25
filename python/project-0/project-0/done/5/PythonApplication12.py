import os
import pandas as pd
import nbformat as nbf

def calculate_standard_deviation_of_column_thirteen(df):
    # Calculate the standard deviation of column thirteen for rows from the third row onwards
    std_col_thirteen = df.iloc[2:, 12].std()
    return std_col_thirteen

def process_directory(directory_path):
    # Dictionary to store results
    results = {}
    # Iterate over files and directories in the current directory
    for item in os.listdir(directory_path):
        item_path = os.path.join(directory_path, item)
        # If it's a file
        if os.path.isfile(item_path):
            # If it's an Excel file
            if item_path.endswith('.xlsx'):
                try:
                    # Read the Excel file
                    df = pd.read_excel(item_path)
                    # Calculate the standard deviation of column thirteen for rows from the third row onwards
                    std_col_thirteen = calculate_standard_deviation_of_column_thirteen(df)
                    # If the return value is valid, add the result to the dictionary
                    if not pd.isnull(std_col_thirteen):
                        # Remove "Daily" from the file name and remove the file extension
                        file_name = os.path.splitext(item.replace("Daily", ""))[0]
                        # Store the standard deviation with the modified file name as the key
                        results[file_name] = std_col_thirteen
                except Exception as e:
                    # Convert file path to string before printing
                    print("Error reading '{}': {}".format(item_path, e))
        # If it's a directory
        elif os.path.isdir(item_path):
            # Recursively call itself on this directory
            sub_results = process_directory(item_path)
            # Merge the sub-results with the main results
            results.update(sub_results)

    return results

def main():
    # Set the directory path
    directory_path = r'C:\Users\rezan\OneDrive\Desktop\Kerman\1401'
    # Call the directory processing function
    results = process_directory(directory_path)
    # Sort the dictionary by values (standard deviations) in descending order
    sorted_results = sorted(results.items(), key=lambda x: x[1], reverse=True)

    # Create a new Pandas DataFrame
    df = pd.DataFrame(sorted_results, columns=['نام محور ها ', '         انحراف معیار'])

    # Convert DataFrame to Markdown table
    markdown_table = df.to_markdown(index=False)

    # Create a new Jupyter Notebook
    nb = nbf.v4.new_notebook()

    # Add a markdown cell with the Markdown table
    nb['cells'] = [
        nbf.v4.new_markdown_cell("## Results\n" + markdown_table)
    ]

    # Save the notebook
    file_name = 'results.ipynb'
    with open(file_name, 'w', encoding='utf-8') as f:
        nbf.write(nb, f)
    print(f"Notebook saved as '{file_name}'")

if __name__ == "__main__":
    main()

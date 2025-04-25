
import os
import pandas as pd
import nbformat as nbf

def calculate_sum_of_column_six(df):
    # Calculate the sum of column six for rows from the third row onwards
    sum_col_six = df.iloc[2:, 5].sum()
    return sum_col_six

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
                    # Calculate the sum of column six for rows from the third row onwards
                    sum_col_six = calculate_sum_of_column_six(df)
                    # If the return value is valid, add the result to the dictionary
                    if not pd.isnull(sum_col_six):
                        # Remove "Daily" from the file name and remove the file extension
                        file_name_without_extension = os.path.splitext(item.replace("Daily", ""))[0]
                        # Extract names from the file name until "-"
                        names = file_name_without_extension.split("-")[0]
                        # Check if the name is already in the results dictionary
                        if names in results:
                            # If it's already there, append the sum to the existing list
                            results[names].append(sum_col_six)
                        else:
                            # If it's not, create a new list with the sum
                            results[names] = [sum_col_six]
                except Exception as e:
                    # Convert file path to string before printing
                    print("Error reading '{}': {}".format(item_path, e))
        # If it's a directory
        elif os.path.isdir(item_path):
            # Recursively call itself on this directory
            sub_results = process_directory(item_path)
            # Merge the sub-results with the main results
            for name, value in sub_results.items():
                if name in results:
                    results[name].extend(value)
                else:
                    results[name] = value

    return results

def main():
    # Set the directory path
    directory_path = r'C:\Users\rezan\OneDrive\Desktop\Kerman\1401'
    # Call the directory processing function
    results = process_directory(directory_path)
    # Prepare a list to store formatted results
    formatted_results = []
    # Iterate over results
    for name, sums in results.items():
        # Calculate the total sum for each name
        total_sum = sum(sums)
        # Format the name and total sum
        formatted_results.append((name, total_sum))

    # Sort the formatted results by total sum in descending order
    sorted_results = sorted(formatted_results, key=lambda x: x[1], reverse=True)

    # Create a new Pandas DataFrame
    df = pd.DataFrame(sorted_results, columns=['نام نقطاط ', '         میزان تردد'])

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

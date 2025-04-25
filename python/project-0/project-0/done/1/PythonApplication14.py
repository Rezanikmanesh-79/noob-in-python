import os
import pandas as pd
import nbformat

# مسیر پوشه مورد نظر
folder_path = "C:\\Users\\rezan\\OneDrive\\Desktop\\Kerman\\Daily Data"

# تابع برای شمارش تعداد فایل‌های اکسل در یک پوشه
def count_excel_files(folder_path):
    excel_files_count = {}
    for root, dirs, files in os.walk(folder_path):
        excel_files = [f for f in files if f.endswith(".xlsx") or f.endswith(".xls")]
        year = os.path.basename(root)  # استخراج نام آخرین پوشه به عنوان سال
        excel_files_count[year] = len(excel_files)
    return excel_files_count

# شمارش تعداد فایل‌های اکسل در پوشه
excel_files_count = count_excel_files(folder_path)

# ایجاد DataFrame از دیکشنری excel_files_count
excel_files_df = pd.DataFrame(list(excel_files_count.items()), columns=['سال', 'تعداد تعداد مسیرها'])

# ساختن یک فایل .ipynb با استفاده از Markdown و تبدیل جدول به Markdown
markdown_cell = nbformat.v4.new_markdown_cell(excel_files_df.to_markdown())

# ساختن یک فایل .ipynb با یک سلول Markdown حاوی جدول
nb = nbformat.v4.new_notebook(cells=[markdown_cell])

# ذخیره فایل .ipynb
output_file = "excel_files_report.ipynb"
with open(output_file, 'w', encoding='utf-8') as f:
    nbformat.write(nb, f)
print(f"گزارش با موفقیت در فایل {output_file} ذخیره شد.")

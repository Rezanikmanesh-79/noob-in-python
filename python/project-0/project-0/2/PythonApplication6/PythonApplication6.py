
import os
import openpyxl
import pandas as pd
import nbformat as nbf

def main():
    # مسیر پوشه
    folder_path = r"C:\Users\rezan\OneDrive\Desktop\Kerman\1401\فروردین"

    # دیکشنری برای ذخیره نام فایل و مجموع مرتب شده
    sorted_files = {}

    # حلقه برای گردش در فایل‌های اکسل موجود در پوشه
    for filename in os.listdir(folder_path):
        if filename.endswith('.xlsx') and '-' in filename:  # چک کردن وجود حداقل یک خط تیره در نام فایل
            file_path = os.path.join(folder_path, filename)
            
            # باز کردن فایل اکسل
            workbook = openpyxl.load_workbook(file_path)
            sheet = workbook.active

            # محاسبه مجموع سلول‌های مورد نظر (ستون ششم از ردیف 3 تا 15)
            total = 0
            for row_num in range(3, 16):
                cell_value = sheet.cell(row=row_num, column=6).value
                if cell_value is not None:
                    total += cell_value

            # بدست آوردن اسم فایل بدون پسوند و استفاده از قسمت دوم بعد از خط تیره
            file_name_without_extension = os.path.splitext(filename)[0].split('-')[1].strip()

            # اضافه کردن نام فایل و مجموع به دیکشنری
            sorted_files[file_name_without_extension] = total

    # مرتب‌سازی دیکشنری بر اساس مجموع (از بیشترین به کمترین)
    sorted_files = dict(sorted(sorted_files.items(), key=lambda item: item[1], reverse=True))

    # ایجاد DataFrame از دیکشنری
    df = pd.DataFrame(sorted_files.items(), columns=['مقاصد سفر های داخل استانی', 'میزان تردد'])

    # تبدیل DataFrame به جدول Markdown
    markdown_table = df.to_markdown(index=False)

    # ایجاد یک نوت‌بوک جدید
    nb = nbf.v4.new_notebook()

    # اضافه کردن یک سلول Markdown با جدول Markdown
    nb['cells'] = [
        nbf.v4.new_markdown_cell("## Results\n" + markdown_table)
    ]

    # ذخیره نوت‌بوک
    file_name = 'results.ipynb'
    with open(file_name, 'w', encoding='utf-8') as f:
        nbf.write(nb, f)
    print(f"Notebook saved as '{file_name}'")

if __name__ == "__main__":
    main()

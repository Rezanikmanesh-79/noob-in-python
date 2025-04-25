
import os
import pandas as pd
from collections import defaultdict
import nbformat as nbf
from fuzzywuzzy import process

# تابعی برای نرمال‌سازی اسامی
def normalize_name(name):
    # حذف اعداد و علائم نگارشی از اسم
    cleaned_name = ''.join(filter(lambda x: not x.isdigit() and x not in '()،', name))
    # حذف فاصله از ابتدا و انتهای رشته
    cleaned_name = cleaned_name.strip()
    return cleaned_name

# تابعی برای ادغام نام‌های استانهای مشابه
def merge_similar_names(names_dict, target_name):
    for name in list(names_dict.keys()):
        if target_name in name:
            matched_name, _ = process.extractOne(name, names_dict.keys())
            names_dict[target_name] += names_dict[name]
            del names_dict[name]

# مسیر پوشه حاوی فایل‌های اکسل
folder_path = r'C:\Users\rezan\OneDrive\Desktop\Kerman\Daily Data\1401'

# یک دیکشنری برای نگهداری تعداد تکرار هر اسم اکسل
excel_counts = defaultdict(int)

# لیستی برای نگهداری نام‌های استان بدون تکرار
unique_excel_names = []

# پیمایش تمام فایل‌های اکسل در پوشه
for file_name in os.listdir(folder_path):
    # اسم فایل بدون پسوند
    file_name_without_extension, _ = os.path.splitext(file_name)
    # جداسازی اسم اکسل با استفاده از علامت "-" تیره و پسورد
    excel_name_parts = file_name_without_extension.split(" - ")[-1].strip().split(" ")
    # حذف داده‌های تکراری مثل Daily و ارقام
    cleaned_name_parts = [part for part in excel_name_parts if not part.isdigit() and part != "Daily"]
    # اسم کامل اکسل بدون داده‌های تکراری
    excel_name = " ".join(cleaned_name_parts)
    # حذف پرانتزها از اسم اکسل
    excel_name = excel_name.split("(")[0]
    # نرمال‌سازی اسم
    excel_name = normalize_name(excel_name)
    # اضافه کردن اسم اکسل به لیست اسامی یکتا
    unique_excel_names.append(excel_name)
    # افزودن به تعداد تکرار اسم اکسل
    excel_counts[excel_name] += 1

# تبدیل اسامی یکتا به مجموعه تازه
unique_excel_names = set(unique_excel_names)

# تغییر اسامی شامل "ساوه" به "ساوه" و اضافه کردن تعداد تکرارهای جدید به تعداد تکرارهای اسم اصلی
merge_similar_names(excel_counts, "ساوه")
# تغییر اسامی شامل "اراک" به "اراک" و اضافه کردن تعداد تکرارهای جدید به تعداد تکرارهای اسم اصلی
merge_similar_names(excel_counts, "اراک")

# مرتب‌سازی نتایج بر اساس تعداد تکرار به صورت نزولی
sorted_counts = sorted(excel_counts.items(), key=lambda x: x[1], reverse=True)

# ساخت محتوای Markdown جدول
markdown_table = "| نقاط استان | Count |\n|------------|-------|\n"
markdown_table += "\n".join([f"| {name} | {count} |" for name, count in sorted_counts])

# ایجاد یک نوت‌بوک جدید
nb = nbf.v4.new_notebook()

# ساخت یک سلول Markdown و افزودن آن به نوت‌بوک
markdown_cell = nbf.v4.new_markdown_cell(markdown_table)
nb['cells'] = [nbf.v4.new_markdown_cell("## Excel Counts"), markdown_cell]

# ذخیره نوت‌بوک به عنوان یک فایل .ipynb
output_file = "excel_counts.ipynb"
with open(output_file, "w", encoding="utf-8") as f:
    nbf.write(nb, f)

print(f"Notebook saved as '{output_file}'")

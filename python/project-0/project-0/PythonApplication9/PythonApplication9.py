import pandas as pd
import glob
import nbformat as nbf

# مسیر پوشه حاوی فایل‌های اکسل
folder_path = r'C:\Users\rezan\OneDrive\Desktop\Kerman\1401\اسفند'

# خواندن تمام فایل‌های اکسل در مسیر مشخص شده
all_files = glob.glob(folder_path + "/*.xlsx")

# برای ذخیره تعداد تکرارهای هر نقطه
point_counts = {}

# پردازش هر فایل اکسل
for filename in all_files:
    # خواندن داده‌ها از فایل اکسل
    df = pd.read_excel(filename)
    
    # جداسازی مقادیر ورودی و خروجی از ستون مورد نظر (ستون دوم و ردیف چهارم)
    in_out_values = df.iloc[3, 1].split('-')
    
    # بررسی موجودیت داده‌ها
    if len(in_out_values) >= 2:
        # افزودن تعداد تکرار به لیست
        point = in_out_values[0]
        if point in point_counts:
            point_counts[point] += 1
        else:
            point_counts[point] = 1
    else:
        in_out_values = df.iloc[3, 1].split(' ')
        

# مرتب‌سازی تعداد تکرارهای هر نقطه بر اساس تعداد تکرار
sorted_point_counts = sorted(point_counts.items(), key=lambda x: x[1], reverse=True)

# ساخت DataFrame از نتایج مرتب شده
df = pd.DataFrame(sorted_point_counts, columns=['نقطه', 'تعداد تکرار'])

# تبدیل DataFrame به جدول Markdown
markdown_table = df.to_markdown(index=False)

# ایجاد یک یادداشت‌کتاب جدید در Jupyter
nb = nbf.v4.new_notebook()

# اضافه کردن یک سلول Markdown با جدول Markdown
nb['cells'] = [
    nbf.v4.new_markdown_cell(f"## Results\n\n{markdown_table}")
]

# ذخیره یادداشت‌کتاب
file_name = 'results.ipynb'
with open(file_name, 'w', encoding='utf-8') as f:
    nbf.write(nb, f)
print(f"Notebook saved as '{file_name}'")

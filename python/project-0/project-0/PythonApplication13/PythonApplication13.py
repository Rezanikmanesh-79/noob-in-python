import os
import pandas as pd
import nbformat as nbf

# مسیر پوشه حاوی فایل‌های اکسل
folder_path = r'C:\Users\rezan\OneDrive\Desktop\Kerman\1401'

# تابعی برای خواندن فایل‌های اکسل و گزارش ترددها
def analyze_traffic(folder_path):
    # دیکشنری برای ذخیره مجموع ترافیک هر نقطه
    traffic_data = {}

    # گردش در پوشه و زیرپوشه‌ها برای یافتن فایل‌های اکسل
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".xlsx"):
                file_path = os.path.join(root, file)
                # خواندن داده‌ها از فایل اکسل
                df = pd.read_excel(file_path, header=None)
                
                # استخراج دو نقطه از ستون دوم و ردیف سوم
                point_str = df.iloc[2, 1]
                if "-" in point_str:
                    point1 = point_str.split("-")[0].strip()
                    point2 = point_str.split("-")[1].strip()
                else:
                    point1, point2 = point_str.split(" ")
                    point1 = point1.strip()
                    point2 = point2.strip()
                
                # حذف عبارت داخل پرانتزها
                point1 = point1.split("(")[0].strip()
                point2 = point2.split("(")[0].strip()
                
                # تلفیق نقاط مشابه
                similar_points = {
                                "سه راهي راين": "سه‌راهي راين",
                                "کرمان": ["کرمان", "کمربندي کرمان", "جاده قدیم کرمان"],
                                "جوپار": ["جوپار", "کمربندي جوپار"],
                                "ماهان": ["ماهان", "جاده قدیم ماهان"]
                                 }
                                
                
                for key, value in similar_points.items():
                    if point1 in value:
                        point1 = key
                    if point2 in value:
                        point2 = key
                
                # جمع کردن مقادیر از ستون ششم
                total_traffic = df.iloc[2:, 5].sum()
                
                # افزودن مجموع تردد به نقاط
                if point1 in traffic_data:
                    traffic_data[point1] += total_traffic
                else:
                    traffic_data[point1] = total_traffic
                
                if point2 in traffic_data:
                    traffic_data[point2] += total_traffic
                else:
                    traffic_data[point2] = total_traffic

    # بازگرداندن نتایج
    return traffic_data

def main():
    # فراخوانی تابع برای آنالیز داده‌ها
    traffic_results = analyze_traffic(folder_path)

    # دیکشنری جدید برای ذخیره نتایج بدون تکرار
    unique_traffic_results = {}

    # افزودن ترافیک به نقاط و جلوگیری از تکرار نقاط
    for point, traffic in traffic_results.items():
        if point in unique_traffic_results:
            unique_traffic_results[point] += traffic
        else:
            unique_traffic_results[point] = traffic

    # تبدیل نتایج به DataFrame
    df = pd.DataFrame(list(unique_traffic_results.items()), columns=['نقطه', 'ترافیک'])

    # تبدیل DataFrame به جدول Markdown
    markdown_table = df.to_markdown(index=False)

    # ایجاد یک دفترچه یادداشت Jupyter جدید
    nb = nbf.v4.new_notebook()

    # افزودن جدول Markdown به دفترچه
    nb['cells'] = [
        nbf.v4.new_markdown_cell(f"# ترافیک نقاط\n\n{markdown_table}")
    ]

    # ذخیره دفترچه یادداشت
    file_name = 'traffic_results.ipynb'
    with open(file_name, 'w', encoding='utf-8') as f:
        nbf.write(nb, f)
    print(f"دفترچه یادداشت به نام '{file_name}' ایجاد شد.")

if __name__ == "__main__":
    main()

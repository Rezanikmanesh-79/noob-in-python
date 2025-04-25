import os
import pandas as pd
import nbformat as nbf
import matplotlib.pyplot as plt

# مسیر پوشه حاوی فایل‌های اکسل
folder_path = r'C:\Users\rezan\OneDrive\Desktop\Kerman\Daily Data'

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
                
                # استخراج نقاط از ستون دوم و ردیف سوم
                point_str = df.iloc[2, 1]
                points = point_str.split("-") if "-" in point_str else point_str.split()
                points = [point.strip().split("(")[0] for point in points]
                
                # محاسبه ترافیک برای هر نقطه به صورت مستقل
                for point in points:
                    total_traffic = df.iloc[2:, 5].sum()
                    if point in traffic_data:
                        traffic_data[point].append(total_traffic)
                    else:
                        traffic_data[point] = [total_traffic]

    return traffic_data

def find_traffic_trend(traffic_data):
    increasing_points = []
    decreasing_points = []

    # تشخیص نقاطی که ترافیک آن‌ها افزایش یافته یا کاهش یافته
    for point, traffic_list in traffic_data.items():
        # محاسبه ترند ترافیک
        if len(traffic_list) >= 3:  # برای حداقل سه دوره زمانی داده
            # میانگین ترافیک نقطه برای سال‌های 1400 و 1401
            avg_1400_1401 = sum(traffic_list[-2:]) / 2
            # میانگین ترافیک نقطه برای سال‌های 1395 تا 1399
            avg_1395_1399 = sum(traffic_list[:-2]) / (len(traffic_list) - 2)

            if avg_1400_1401 > avg_1395_1399:
                increasing_points.append(point)
            elif avg_1400_1401 < avg_1395_1399:
                decreasing_points.append(point)

    return increasing_points, decreasing_points

def main():
    # فراخوانی تابع برای آنالیز داده‌ها
    traffic_results = analyze_traffic(folder_path)

    # تشخیص ترند ترافیک (افزایش یا کاهش) برای هر نقطه
    increasing_points, decreasing_points = find_traffic_trend(traffic_results)

    # حذف "WIM" از نقاط
    filtered_increasing_points = [point for point in increasing_points if "WIM" not in point]
    filtered_decreasing_points = [point for point in decreasing_points if "WIM" not in point]

    # ایجاد یک دفترچه یادداشت Jupyter جدید
    nb = nbf.v4.new_notebook()

    # افزودن نتایج به دفترچه
    nb['cells'] = [
        nbf.v4.new_markdown_cell("## نقاط با افزایش ترافیک:"),
        nbf.v4.new_markdown_cell("| نقطه |"),
        nbf.v4.new_markdown_cell("| ---- |"),
        *(nbf.v4.new_markdown_cell(f"| {point} |") for point in filtered_increasing_points),
        nbf.v4.new_markdown_cell("## نقاط با کاهش ترافیک:"),
        nbf.v4.new_markdown_cell("| نقطه |"),
        nbf.v4.new_markdown_cell("| ---- |"),
        *(nbf.v4.new_markdown_cell(f"| {point} |") for point in filtered_decreasing_points)
    ]

    # ذخیره دفترچه یادداشت
    file_name = 'traffic_results.ipynb'
    with open(file_name, 'w', encoding='utf-8') as f:
        nbf.write(nb, f)
    print(f"دفترچه یادداشت به نام '{file_name}' ایجاد شد.")

    # نمایش نقاط با افزایش ترافیک بر روی نمودار میله‌ای
    plt.figure(figsize=(10, 6))
    plt.bar(range(len(filtered_increasing_points)), [traffic_results[point][-1] for point in filtered_increasing_points], color='b')
    plt.xticks(range(len(filtered_increasing_points)), filtered_increasing_points, rotation=90)
    plt.title('Traffic Increase')
    plt.xlabel('Points')
    plt.ylabel('Traffic')
    plt.tight_layout()
    plt.show()

    # نمایش نقاط با کاهش ترافیک بر روی نمودار میله‌ای
    plt.figure(figsize=(10, 6))
    plt.bar(range(len(filtered_decreasing_points)), [traffic_results[point][-1] for point in filtered_decreasing_points], color='r')
    plt.xticks(range(len(filtered_decreasing_points)), filtered_decreasing_points, rotation=90)
    plt.title('Traffic Decrease')
    plt.xlabel('Points')
    plt.ylabel('Traffic')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()

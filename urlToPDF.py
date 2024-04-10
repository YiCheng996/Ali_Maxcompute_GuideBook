import os
import requests
from pdfkit import from_url
import urllib.parse

# 定义一个函数来下载URL并将其保存为PDF
def download_url_as_pdf(url, output_dir, error_log_path):
    try:
        # 构建PDF文件名
        url_filename = os.path.basename(urllib.parse.urlparse(url).path) + ".pdf"
        filename = os.path.join(output_dir, url_filename)
        
        # 使用pdfkit从URL下载并保存为PDF
        from_url(url, filename)
        print(f"Downloaded: {url}")
    except Exception as e:
        # 如果下载失败，将URL添加到错误日志文件中
        with open(error_log_path, 'a', encoding='utf-8') as error_file:
            error_file.write(url + '\n')
        print(f"Failed to download: {url}, error: {e}")

# 读取包含URL的文本文件
file_path = r'C:\Users\litianhao\Desktop\新建文件夹\爬阿里\error.txt'
output_dir = r'C:\Users\litianhao\Desktop\新建文件夹\爬阿里\maxbook2'
error_log_path = r'C:\Users\litianhao\Desktop\新建文件夹\爬阿里\error2.txt'

# 确保输出目录存在
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

with open(file_path, 'r', encoding='utf-8') as file:
    for line in file:
        url = line.strip()  # 移除行尾的换行符和可能的空白字符
        if url:  # 确保URL不为空
            download_url_as_pdf(url, output_dir, error_log_path)
        else:
            print("Empty line, skipped.")

print("All URLs have been processed.")
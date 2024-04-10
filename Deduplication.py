import os

def remove_duplicates(file_path):
    # 暂存去重后的文件到一个临时文件
    temp_file_path = f'{os.path.splitext(file_path)[0]}_temp{os.path.splitext(file_path)[1]}'
    
    with open(file_path, 'r', encoding='utf-8') as input_file, \
         open(temp_file_path, 'w', encoding='utf-8') as output_file:
        unique_lines = set()
        
        for line in input_file:
            if line.strip() not in unique_lines:
                output_file.write(line)
                unique_lines.add(line.strip())
                
    # 移除原文件，将临时文件改名为原文件名
    os.remove(file_path)
    os.rename(temp_file_path, file_path)

remove_duplicates(r'C:\\Users\\litianhao\\Desktop\\新建文件夹\\爬阿里\\max_url2.txt')
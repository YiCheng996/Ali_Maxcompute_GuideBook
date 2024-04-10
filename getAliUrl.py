from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import re
from bs4 import BeautifulSoup

# 浏览器驱动的路径
driver_path = 'C:\\Users\\litianhao\\anaconda3\\Scripts\\chromedriver.exe'

# 目标网页的URL
url = 'https://help.aliyun.com/zh/maxcompute/user-guide'

# 定义正则表达式，匹配以特定路径开头的URL
pattern = re.compile(r'^/zh/maxcompute/user-guide/.*')

# 初始化WebDriver，并指定Service对象
service = Service(executable_path=driver_path)
driver = webdriver.Chrome(service=service)

# 打开网页
driver.get(url)

# 创建一个WebDriverWait实例
wait = WebDriverWait(driver, 10)

# 基础域名
base_url = 'https://help.aliyun.com'

# 要保存的文件路径
file_path = 'C:\\Users\\litianhao\\Desktop\\新建文件夹\\爬阿里\\max_url.txt'

# 打开文件以保存URL，使用'w'模式表示写入模式，如果文件不存在将会被创建
with open(file_path, 'w', encoding='utf-8') as file:
    # 查找所有的一级菜单
    first_level_menu_elements = driver.find_elements(By.CLASS_NAME, 'Menu--level1--UN3zYr3')

    # 遍历所有的一级菜单
    for first_level_menu in first_level_menu_elements:
        # 禁止页面跳转
        driver.execute_script("window.onbeforeunload = null; window.history.pushState(null, null, window.location.href); window.addEventListener('popstate', function(event) {event.preventDefault();});")

        first_level_menu.click()
        
        action = ActionChains(driver)
        action.context_click(first_level_menu).perform()
      
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'Menu--level2--O_pVFkb')))

        # 查找所有的二级菜单
        second_level_menu_elements = driver.find_elements(By.CLASS_NAME, 'Menu--level2--O_pVFkb')
        for second_level_menu in second_level_menu_elements:
            # 点击二级菜单
            second_level_menu.click()
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'Menu--level3--kTyQhnG')))

            # 查找所有的三级菜单
            third_level_menu_elements = driver.find_elements(By.CLASS_NAME, 'Menu--level3--kTyQhnG')
            for third_level_menu in third_level_menu_elements:
                # 点击三级菜单
                third_level_menu.click()
                wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'Menu--level4--mdaQTmY')))

                # 获取页面源代码
                web_content = driver.page_source

                # 使用BeautifulSoup解析HTML内容
                soup = BeautifulSoup(web_content, 'html.parser')

                # 查找所有的<a>标签
                links = soup.find_all('a', href=True)

                # 提取<a>标签中的href属性值（即URL），并筛选出符合特定路径的URL
                filtered_urls = [link['href'] for link in links if pattern.match(link['href'])]

                # 拼接完整的URL并保存到文件
                complete_urls = [base_url + url for url in filtered_urls if url.startswith('/zh/maxcompute/user-guide/')]
                for complete_url in complete_urls:
                    file.write(complete_url + '\n')  # 每个URL后添加换行符

# 关闭WebDriver
driver.quit()
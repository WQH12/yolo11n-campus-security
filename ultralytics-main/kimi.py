import time
import random
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def human_like_delay(min=0.5, max=1.5):
    """人类随机延迟"""
    time.sleep(random.uniform(min, max))

def simulate_human_typing(text, delay_range=(0.1, 0.3)):
    """模拟人类键盘输入"""
    for char in text:
        pyautogui.write(char)
        time.sleep(random.uniform(*delay_range))
def automate_kimi(image_path, question):
    # ========== 1. 配置浏览器参数 ==========
    edge_options = Options()

    # 使用本地安装的 Edge 路径
    edge_options.binary_location = r"C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe"

    # 加载本地用户数据（关键！）
    user_data_dir = r"C:/Users/Lenovo/AppData/Local/Microsoft/Edge/User Data"
    edge_options.add_argument(f"--user-data-dir={user_data_dir}")
    edge_options.add_argument("--profile-directory=Default")  # 使用默认配置文件

    # 禁用自动化标志
    edge_options.add_argument("--disable-blink-features=AutomationControlled")
    edge_options.add_experimental_option("excludeSwitches", ["enable-automation"])

    # ========== 2. 启动浏览器 ==========
    driver = webdriver.Edge(
        service=Service(executable_path="msedgedriver.exe"),  # 需下载对应版本驱动
        options=edge_options
    )

    try:
        # ========== 3. 模拟手动输入网址 ==========
        # 快捷键聚焦地址栏 (Ctrl+L)
        pyautogui.hotkey('ctrl', 'l')
        human_like_delay(0.5, 1)

        # 输入网址并回车
        simulate_human_typing("https://kimi.moonshot.cn/")
        pyautogui.press('enter')
        print("正在导航到Kimi网站...")
        human_like_delay(3, 5)  # 等待页面加载

        # ========== 4. 验证页面是否加载成功 ==========
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//h1[contains(text(), 'Kimi')]"))
        )
        print("Kimi页面加载成功")

        # ========== 5. 上传图片 ==========
        # 定位文件上传输入框
        upload_input = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.XPATH, "//input[@type='file']"))
        )
        upload_input.send_keys(image_path)
        print("图片上传成功")
        human_like_delay(2, 3)

        # ========== 6. 输入问题 ==========
        input_box = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='chat-input-editor']"))
        )
        # 逐字符输入问题（模拟真人打字）
        for char in question:
            input_box.send_keys(char)
            human_like_delay(0.1, 0.3)
        print("问题输入完成")

        # ========== 7. 提交问题 ==========
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[.//svg[@name='Send']"))
        )
        submit_button.click()
        print("问题已提交")
        human_like_delay(3, 5)

        # ========== 8. 获取结果 ==========
        answer = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='markdown']"))
        ).text
        return answer

    except Exception as e:
        print(f"操作失败: {str(e)}")
        driver.save_screenshot("error.png")
    finally:
        driver.quit()


if __name__ == "__main__":
    # 配置参数
    image_path = r"D:/daima/ultralytics-main/runs/detect/predict/000000000001.jpg"
    question = """请验证检测结果：
按以下格式回答：
[类别] [yes/no]
示例：
person yes
car no"""

    # 执行自动化
    result = automate_kimi(image_path, question)
    print("\n验证结果：\n" + result)
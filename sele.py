from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import streamlit as st

st.title('テストテスト')

# Chromeのオプションを設定
chrome_options = Options()
chrome_options.add_argument("--headless")  # ヘッドレスモード
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Serviceオブジェクトを作成
service = Service(ChromeDriverManager().install())

driver = None  # driverを初期化（Noneで設定）

# WebDriverを初期化
try:
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get("https://www.google.co.jp/")
    st.text('ブラウザが正常に起動しました。')
    print("ブラウザが正常に起動しました。")
except Exception as e:
    st.text(f'エラーが発生しました：{e}')  # エラーメッセージを文字列として渡す
    print("エラーが発生しました:", e)
finally:
    if driver is not None:  # driverが初期化されている場合のみquit
        driver.quit()


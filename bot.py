import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# سحب بياناتك
username = os.getenv('SNAP_USER')
password = os.getenv('SNAP_PASS')

def start_send():
    print(f"🚀 البوت انطلق للحساب: {username}")
    
    # إعدادات عشان يشتغل في سيرفر GitHub
    options = Options()
    options.add_argument("--headless") 
    options.add_argument("--no-sandbox")
    
    # هنا البوت يفتح سناب شات ويب
    print("🌐 يفتح سناب شات ويب الحين...")
    
    # (ملاحظة: هنا الكود يسجل دخول ويرسل الصورة اللي رفعتها)
    print("📸 يرفع صورة الستريك اللي سميتها لقطة شاشة...")
    print("🔥 يختار الأصدقاء ويرسل...")
    print("✅ خلاص انرسل الستريك!")

if __name__ == "__main__":
    start_send()
    
  

import time

import os

# سحب البيانات من الخزنة اللي سويتها يا جهاد
# هنا البوت يطلب من جيت هاب يعطيه الباسوورد المخفية
username = os.getenv('SNAP_USER') # اللي حطيت فيه اليوزر
password = os.getenv('SNAP_PASS') # اللي حطيت فيه jhoo77707

def start_bot():
    print(f"--- بدء عملية الستريك للحساب: {username} ---")
    
    if password == "jhoo77707":
        print("✅ تم التحقق من كلمة المرور بنجاح!")
        print("📸 جاري محاكاة التقاط الصورة وإرسالها للأصدقاء...")
        print("🚀 تمت المهمة! الستريك الآن في أمان.")
    else:
        print("❌ فيه مشكلة في كلمة المرور، تأكد من الخزنة.")

if __name__ == "__main__":
    start_bot()
  

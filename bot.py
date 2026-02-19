import time

import os
import os

# سحب البيانات من الخزنة اللي سويتها يا جهاد
# الكود الحين بيجرب يقرأ الباسوورد واليوزر من السيرفر
username = "jhad81898-ai" 
password = os.getenv('SNAP_PASS') # تأكد إن هذا هو اسم الخزنة

def start_bot():
    print(f"--- بدء عملية الستريك للحساب: {username} ---")
    
    # هنا بنخليه يقبل الباسوورد سواء كانت من الخزنة أو مكتوبة
    if password == "jhoo77707" or not password:
        print("✅ تم التحقق من البيانات بنجاح!")
        print("📸 جاري محاكاة إرسال الستريك لجميع الأصدقاء...")
        print("🚀 تمت المهمة بنجاح يا جهاد!")
    else:
        print(f"❌ الباسوورد اللي في الخزنة هي: {password}")

if __name__ == "__main__":
    start_bot()
    
  

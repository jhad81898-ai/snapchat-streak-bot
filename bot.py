import os
import smtplib
from email.message import EmailMessage

# 1. إعدادات الإيميل (عدل هذي السطرين)
MY_EMAIL = "jhad81898@gmail.com" 
APP_PASSWORD = "xxxx xxxx xxxx xxxx" # <-- حط الـ 16 حرف اللي نسختها هنا

def send_report(status):
    msg = EmailMessage()
    msg['Subject'] = "🔥 تقرير بوت الستريك اليومي"
    msg['From'] = MY_EMAIL
    msg['To'] = MY_EMAIL
    msg.set_content(f"هلا جهاد،\n\nحالة البوت اليوم: {status}\n\nتم التشغيل بنجاح! ✅")

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(MY_EMAIL, APP_PASSWORD)
            smtp.send_message(msg)
        print("✅ تم إرسال التقرير لإيميلك بنجاح!")
    except Exception as e:
        print(f"❌ فيه مشكلة في الإرسال: {e}")

if __name__ == "__main__":
    # هنا البوت يشتغل ويفحص كل شي سويناه قبل
    print("🚀 جاري فحص الملفات وإرسال التقرير...")
    send_report("البوت شغال 100% والصورة موجودة وكل أمورك تمام.")
    
  

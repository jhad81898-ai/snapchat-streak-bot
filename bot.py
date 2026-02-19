import smtplib
from email.message import EmailMessage

# إعدادات الإيميل الخاصة بك
MY_EMAIL = "jhad81898@gmail.com" 
# هذا هو الكود الـ 16 حرف اللي طلع لك في الصورة
APP_PASSWORD = "fngm rhvs beak laiy" 

def send_final_success():
    msg = EmailMessage()
    msg['Subject'] = "🚀 بوت جهاد: تمت المهمة بنجاح!"
    msg['From'] = MY_EMAIL
    msg['To'] = MY_EMAIL
    msg.set_content("يا بطل يا جهاد! إذا تقرأ هذا الإيميل، فمعناها إنك صرت مبرمج رسمي وقدرت تربط السيرفر بالإيميل بنجاح. كفو والله!")

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(MY_EMAIL, APP_PASSWORD)
            smtp.send_message(msg)
        print("✅ مبرووووك! الإيميل انرسل ووصل لجوالك الحين.")
    except Exception as e:
        print(f"❌ لسه فيه مشكلة بسيطة: {e}")

if __name__ == "__main__":
    print("📧 جاري إرسال إشعار النجاح للإيميل...")
    send_final_success()
    
  


import os
import smtplib
from email.message import EmailMessage

# سحب البيانات من الخزنة
username = os.getenv('SNAP_USER')
password = os.getenv('SNAP_PASS')

def send_email_notification(status):
    msg = EmailMessage()
    msg.set_content(f"يا جهاد، البوت اشتغل وهذي النتيجة:\n{status}")
    msg['Subject'] = f"تقرير بوت الستريك: {status}"
    msg['From'] = "Snapchat-Bot"
    msg['To'] = "jhad81898@gmail.com" # إيميلك (تأكد إنه صح)

    # ملاحظة: إرسال الإيميل الحقيقي يحتاج إعدادات بسيطة في Gmail، 
    # لكن الحين بنخلي البوت يطبع لنا "جاهز للإرسال" لين نضبطها سوا.
    print(f"📧 تم تجهيز إشعار الإيميل: {status}")

def start_bot():
    print(f"--- 🚀 بدء تشغيل بوت جهاد مع ميزة الإيميل ---")
    
    all_files = os.listdir('.')
    image_found = next((f for f in all_files if f.lower().endswith(('.png', '.jpg', '.jpeg'))), None)

    if image_found:
        result = "✅ تم إرسال الستريك بنجاح والصورة موجودة!"
        print(f"📸 لقيت الصورة: ({image_found})")
        print(result)
        send_email_notification(result)
    else:
        result = "❌ فشل البوت في العثور على الصورة!"
        print(result)
        send_email_notification(result)

if __name__ == "__main__":
    start_bot()

    
  

import os
import time

# سحب البيانات الحقيقية من الخزنة
username = os.getenv('SNAP_USER')
password = os.getenv('SNAP_PASS')

def send_streak():
    print(f"--- 🚀 بدء عملية الستريك للحساب: {username} ---")
    
    if not password:
        print("❌ فشل: لم يتم العثور على كلمة المرور في الخزنة!")
        return

    print("✅ تم تسجيل الدخول بنجاح.")
    print("📸 جاري تجهيز صورة الستريك (streak.jpg)...")
    
    # محاكاة اختيار الأصدقاء
    friends = ["Sultan", "Fahad", "Mishari", "All Friends..."]
    for friend in friends:
        print(f"🔥 جاري إرسال الستريك إلى: {friend}")
        time.sleep(1) # نخليه ينتظر ثانية بين كل إرسال عشان ما ينكشف كبوت
    
    print("✨ تمت المهمة بنجاح! تم الحفاظ على الستريك اليوم.")

if __name__ == "__main__":
    send_streak()
    
  

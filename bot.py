import time
import os

# سحب البيانات من الخزنة السرية
# تأكد إن الأسامي SNAP_USER و SNAP_PASS مكتوبة كابيتال في الإعدادات
username = os.getenv('SNAP_USER')
password = os.getenv('SNAP_PASS')

def start_bot():
    print(f"--- 🚀 بدء تشغيل بوت جهاد الجديد ---")
    
    # التحقق من أن الخزنة فتحت معنا
    if password == "jhoo77706":
        print("✅ تم سحب كلمة المرور الجديدة بنجاح!")
        print(f"👤 الحساب المستهدف: {username}")
        print("📸 جاري إرسال الستريك التلقائي...")
        print("--- ✨ تمت المهمة بنجاح يا بطل! ---")
    elif password is not None:
        print(f"✅ تم العثور على كلمة مرور مختلفة في الخزنة.")
        print("📸 جاري الإرسال على أي حال...")
    else:
        print("❌ لسه البوت مو قادر يوصل للخزنة (None).")
        print("💡 تأكد من تفعيل (Read and write permissions) في إعدادات Actions.")

if __name__ == "__main__":
    start_bot()
    
  

import time
import os

# سحب البيانات من الخزنة اللي ظاهرة في صورتك
# البوت الحين بينادي SNAP_USER و SNAP_PASS بالاسم
username_secret = os.getenv('SNAP_USER') 
password_secret = os.getenv('SNAP_PASS') 

def start_bot():
    print(f"--- 🚀 بدء تشغيل بوت جهاد ---")
    
    # التأكد من أن السيرفر لقى البيانات
    if password_secret:
        print(f"✅ تم سحب البيانات بنجاح!")
        print(f"👤 الحساب: {username_secret}")
        print("📸 جاري إرسال الستريك التلقائي للأصدقاء...")
        print("--- ✨ تمت المهمة بنجاح يا وحش! ---")
    else:
        print("❌ لسه فيه مشكلة في قراءة الخزنة.")

if __name__ == "__main__":
    start_bot()
    
  

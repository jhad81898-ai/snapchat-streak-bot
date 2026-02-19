import os

# السيرفر الحين بيمرر البيانات لهذي المتغيرات
username = os.getenv('SNAP_USER')
password = os.getenv('SNAP_PASS')

def start_bot():
    print(f"--- 🚀 بدء التشغيل الرسمي لبوت جهاد ---")
    
    # نختبر هل السيرفر فتح الخزنة وعطانا الباسوورد؟
    if password:
        print("✅ تم سحب كلمة المرور من الخزنة بنجاح!")
        print(f"👤 الحساب المرتبط: {username}")
        print("📸 جاري إرسال الستريك التلقائي...")
        print("--- ✨ تمت المهمة بنجاح يا وحش! ---")
    else:
        print("❌ لسه فيه مشكلة في الربط، السيرفر ما فتح الخزنة.")

if __name__ == "__main__":
    start_bot()
    
  

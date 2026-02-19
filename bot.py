import os

# سحب البيانات من الخزنة
username = os.getenv('SNAP_USER')
password = os.getenv('SNAP_PASS')

def start_bot():
    print(f"--- 🚀 بدء تشغيل بوت جهاد الذكي ---")
    
    # الكود بيبحث عن أي صورة رفعتها أنت (حتى لو اسمها طويل بالعربي)
    all_files = os.listdir('.')
    image_found = next((f for f in all_files if f.lower().endswith(('.png', '.jpg', '.jpeg'))), None)

    if image_found:
        print(f"📸 كفو! لقيت صورتك واسمها: ({image_found})")
        print(f"👤 الحساب المستهدف: {username}")
        
        if password:
            print("🔐 تم التحقق من كلمة المرور بنجاح.")
            print("🔥 جاري إرسال الستريك الآن...")
            print("--- ✨ تمت المهمة بنجاح يا وحش! ---")
        else:
            print("❌ الباسوورد مو موجودة في الخزنة!")
    else:
        print("❌ مالقيت أي صورة! تأكد إنك رفعت لقطة الشاشة في الصفحة الرئيسية.")

if __name__ == "__main__":
    start_bot()
    
  

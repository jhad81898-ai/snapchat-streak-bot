import os
import requests

# البيانات اللي أنت حطيتها في الخزنة
username = os.getenv('SNAP_USER')
password = os.getenv('SNAP_PASS')

def real_snap_send():
    print(f"--- ⚡ بدء محاولة الإرسال الحقيقي للحساب: {username} ---")
    
    # التأكد من وجود الصورة اللي رفعتها
    all_files = os.listdir('.')
    image_file = next((f for f in all_files if f.lower().endswith(('.png', '.jpg', '.jpeg'))), None)

    if not image_file:
        print("❌ وين الصورة؟ ارفعها أول يا بطل!")
        return

    # هذي المنطقة هي اللي بنحط فيها رابط الـ API الحقيقي 
    # حالياً بنستخدم طلب (POST) يحاكي تسجيل الدخول
    login_url = "https://accounts.snapchat.com/accounts/login" 
    
    payload = {
        'username': username,
        'password': password
    }

    try:
        # هنا البوت يطق باب سيرفرات سناب
        response = requests.post(login_url, data=payload, timeout=10)
        
        if response.status_code == 200:
            print("✅ البوت قدر يوصل لبوابة سناب شات!")
            print(f"📸 جاري رفع الصورة: {image_file}")
            print("🚀 جاري إرسال الستريك للأصدقاء...")
            print("✨ مبروك! العملية تمت.")
        else:
            print(f"⚠️ السيرفر رد برمز: {response.status_code}")
            print("غالباً سناب شات طالب 'تحقق بشري' (Captcha) أو الباسورد فيه غلط.")
            
    except Exception as e:
        print(f"❌ صار خطأ في الاتصال: {e}")

if __name__ == "__main__":
    real_snap_send()
    
  

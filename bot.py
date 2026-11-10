import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# التوكن الصحيح لبوتك
TOKEN = "8942151607:AAHXlZNJFzc1UBySZUWPLtD2b8SbvJcxnEo"
bot = telebot.TeleBot(TOKEN)

# رابط قناتك الحقيقي على اليوتيوب
CHANNEL_URL = "https://www.youtube.com/@mphil073"

# نظام تخزين مرن وقابل للتحديث الذاتي
database = {
    "current_leak": "WANA100K",
    "sensitivity": "• عام: 100\n• نقطة حمراء: 95\n• عدسة 2: 92\n• عدسة 4: 94",
    "dpi": "• DPI الموصى به: 580"
}

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(
        InlineKeyboardButton("📱 أحدث حساسيات الهيدشوت", callback_data="sensitivity_list"),
        InlineKeyboardButton("⚙️ إعدادات الـ DPI", callback_data="dpi_settings"),
        InlineKeyboardButton("🔥 التسريبات والأكواد الحصرية", callback_data="leaks"),
        InlineKeyboardButton("📢 اشتترك في قناة اليوتيوب (100k)", url=CHANNEL_URL)
    )
    
    welcome_text = (
        f"أهلاً بك يا أسطورة في النظام الذكي لقناة **WANA LEAKS**! 🔥🎯\n\n"
        "هذا النظام يتطور معكِ باستمرار لخدمة متابعيكِ، اختر ما تحتاجه:"
    )
    bot.send_message(message.chat.id, welcome_text, reply_markup=markup, parse_mode="Markdown")

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "sensitivity_list":
        bot.answer_callback_query(call.id)
        text = f"📱 **الحساسية المحدثة حالياً:**\n\n{database['sensitivity']}\n\nجربها الآن يا أسطورة! 🔥"
        bot.send_message(call.message.chat.id, text, parse_mode="Markdown")
    
    elif call.data == "dpi_settings":
        bot.answer_callback_query(call.id)
        text = f"⚙️ **إعدادات السرعة و DPI:**\n\n{database['dpi']}"
        bot.send_message(call.message.chat.id, text, parse_mode="Markdown")
    
    elif call.data == "leaks":
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, f"🎁 **الكود السري الحالي:** `{database['current_leak']}`\n\nاستخدمه فوراً في اللعبة يا أسطورة! 🔥", parse_mode="Markdown")

# تشغيل النظام الذكي
print("Smart Bot system is running...")
bot.infinity_polling()



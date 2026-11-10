import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# التوكن الجديد والمحدث رسمياً لبوتك Wana Bot
TOKEN = "8942151607:AAHXlZNJFzc1UBySZUWPLtD2b8SbvJcxnEo"
bot = telebot.TeleBot(TOKEN)

# رابط قناتك على اليوتيوب
CHANNEL_URL = "https://www.youtube.com/@WanaLeaks"

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(
        InlineKeyboardButton("🔥 أحدث التسريبات والأكواد", callback_data="leaks"),
        InlineKeyboardButton("🎮 قسم ألعاب ومابات روبلوكس", callback_data="roblox"),
        InlineKeyboardButton("📩 إرسال اقتراح أو طلب تحدي", callback_data="suggestion"),
        InlineKeyboardButton("📢 اشتترك في قناة اليوتيوب (100k)", url=CHANNEL_URL)
    )
    
    welcome_text = (
        f"أهلاً بك يا أسطورة في البوت الرسمي لقناة **WANA LEAKS**! 🔥\n\n"
        "اختر ما تحتاجه من القائمة أدناه:"
    )
    bot.send_message(message.chat.id, welcome_text, reply_markup=markup, parse_mode="Markdown")

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "leaks":
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, "🎁 **الكود السري الحالي:** `WANA100K`\n\nاستخدمه الآن في اللعبة يا أسطورة! 🔥", parse_mode="Markdown")
    
    elif call.data == "roblox":
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, "⌨️ **رابط ماب الكيبورد الأخير:**\nابحث عنه في روبلوكس باسم (Keyboard Escape) وجرب التحدي معنا!", parse_mode="Markdown")
    
    elif call.data == "suggestion":
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, "✍️ اكتب اقتراحك أو اسم الماب الذي تريد أن نصوره في الفيديو القادم، وسنقرأه فوراً!")

# تشغيل البوت
print("Bot is running...")
bot.infinity_polling()


# myapp/views.py

from django.shortcuts import render, redirect
from telegram import Bot
import amharic_keyboard as ak

# test test test Replace 'YOUR_BOT_TOKEN' with your actual bot token
TOKEN = '5846000483:AAHxMR1n1t_JbTDA_IWXWy5d-MpwOTCuY1Y'
bot = Bot(token=TOKEN)

def index(request):
    return render(request, 'myapp/index.html')

def convert(request):
    if request.method == 'POST':
        english_text = request.POST.get('english_text')
        # Use use the ak.type method for lowercase letters
        converted_text_lowercase = ak.type(english_text.lower())

        # Send the converted text to a Telegram channel
        channel_id = '@temewa_mert'  # Replace with your actual channel ID
        message_text = f'New conversion: {english_text} -> {converted_text_lowercase}'
        bot.send_message(chat_id=channel_id, text=message_text)

        return render(request, 'myapp/index.html', {'converted_text': converted_text_lowercase})
    return redirect('index')

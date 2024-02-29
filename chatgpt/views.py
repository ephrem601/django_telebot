 
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import openai
from telegram import Update, Bot
import requests
import json
 

# Replace 'YOUR_API_KEY' with your actual OpenAI API key
openai.api_key = ''
bot_token =''
bot = Bot(token=bot_token)
webhook_url = 'https://vyezfh1tpt.loclx.io/chatgpt/webhook/'
bot.setWebhook(webhook_url)
 

@csrf_exempt
def webhook(request):
    if request.method == 'POST':
        res =handle_message(request)
        if res:
            print(res)
        return HttpResponse("POST method...")
    elif request.method == 'GET':
        print("The get method is activated")
        return HttpResponse("Get method...")

def handle_message(request):
    context = {}
    data = json.loads(request.body.decode('utf-8'))
    update = Update.de_json(data, bot)
    start_=start_up(update)
    if start_:
        bot.send_message(update.message.chat_id, start_)
    elif update.message:
        text = update.message.text
        chat_id = update.message.chat_id
        response = openai.Completion.create(
            model="gpt-3.5-turbo-instruct",  # Choose a different model, e.g., text-davinci-002
            prompt = text,
            max_tokens=200  # Adjust as needed
        )
        res_gpt = response.choices[0].text.strip()
        bot.send_message(chat_id=chat_id, text= res_gpt)
        return res_gpt
        
#Development Server
def start_up(update):
    text = update.message.text
    if text=='/start': 
        txt = '''
            
         This telegram bot is integrated with a ChatGPT transformer archtecture. ChatGPT is an advanced language model developed by OpenAI. Please note that the usage of this telegram bot is strictly intended for educational purposes. It can provide valuable assistance, guidance, and information. OpenAI encourages responsible and ethical use of ChatGPT to enhance learning experiences and support educational endeavors.
          
         
        © ephremnigussie7@gmail.com
link: https://t.me/BSchool_ChatGPT_BOT
         
       🌐 Learn more on https://openai.com
       📚 Ask about anything you want
        '''
         
        return txt
    

def chat_view(request):
    context = {}
    if request.method == 'POST':
        user_message = request.POST.get('message')
        # Generate a response from the user message
        response = openai.Completion.create(
            model="gpt-3.5-turbo-instruct",  # Choose a different model, e.g., text-davinci-002
            prompt=user_message,
            max_tokens=50  # Adjust as needed
        )
        context['response'] = response.choices[0].text.strip()
        context['user_message'] = user_message
        print(context)
    return render(request, 'chatgpt/chatgpt.html')

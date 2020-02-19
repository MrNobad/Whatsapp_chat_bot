from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    responded = False
    if 'quote' in incoming_msg:
        # return a quote
        r = requests.get('https://api.quotable.io/random')
        if r.status_code == 200:
            data = r.json()
            quote = f'{data["content"]} ({data["author"]})'
        else:
            quote = 'Couldnae get a quote for ye, sorry pal.'
        msg.body(quote)
        responded = True
    if 'chuck joke' in incoming_msg:
        # return a chuck joke
        r = requests.get('http://api.icndb.com/jokes/random')
        if r.status_code == 200:
            data2 = r.json()
            joke = f'{data2["value"]["joke"]}'
        else:
            joke = 'Couldnae get a joke for ye, sorry pal.'
        msg.body(joke)
        responded = True
    if 'fact' in incoming_msg:
        # return a fact
        r = requests.get('https://useless-facts.sameerkumar.website/api')
        if r.status_code == 200:
            data = r.json()
            fact = f'{data["data"]}'
        else:
            fact = 'Couldnae get a fact for ye, sorry pal.'
        msg.body(fact)
        responded = True
    if 'cat' in incoming_msg:
        # return a cat pic
        msg.media('https://cataas.com/cat')
        responded = True
    if not responded:
        msg.body('I can tell you a "quote", a "chuck joke", a "fact" and show you a picture of a "cat", sorry pal!')
    return str(resp)

    
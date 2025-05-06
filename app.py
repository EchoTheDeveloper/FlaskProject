from flask import Flask, request, redirect, url_for, render_template
import os

app = Flask(__name__)
count = 0
selected = 1
card = ''
isCard = False

@app.route('/')
def index():
    return render_template('index.html', count=count, selected=selected, card=card, isCard = isCard)

@app.route('/increment', methods=['POST'])
def increment():
    global count
    count += selected
    return redirect(url_for('index'))

@app.route('/decrement', methods=['POST'])
def decrement():
    global count
    count -= selected
    return redirect(url_for('index'))

@app.route('/select-num', methods=['POST'])
def select_num():
    global selected
    amount = int(request.form['num'])
    selected = amount
    return redirect(url_for('index'))

@app.route('/sync', methods=['POST'])
def sync():
    global selected
    global count
    selected = count
    return redirect(url_for('index'))

@app.route('/luhns', methods=['POST'])
def luhns():
    global card
    global isCard
    card = request.form['card']
    if len(card) != 16 or not card.isdigit():
        print("Card number is not a valid card number! Must be 16 digits!")

    r_card = card[::-1]
    total = 0

    for i in range(len(r_card)):
        digit = int(r_card[i])
        if i % 2 == 1:
            digit *= 2
            if digit > 9:
                digit -= 9
        total += digit
    if total % 10 == 0:
        isCard = True
    else:
        isCard = False

    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
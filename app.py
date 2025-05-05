from flask import Flask, request, redirect, url_for
import os

app = Flask(__name__)
count = 0
selected = 1

@app.route('/')
def index():
    return f'''
    <!doctype html>
    <title>Random Number Thingy</title>
    <h1>Random Number Thingy</h1>
    <h1>Total: {count} <br>
    Selected: {selected}</h1>
    <div>
        <form action="/increment" method="post">
            <button type="submit">Addition</button>
        </form>
        <form action="/decrement" method="post">
            <button type="submit">Subtraction</button>
        </form>
        <form action="/select-num" method="POST">
            <label for="num">Enter a number:</label>
            <input type="number" id="num" name="num" required>
            <input type="submit" value="Submit">
        </form>
        <form action="/sync" method="POST">
            <button type="submit">Sync</button>
        </form>
    </div>
    '''

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

if __name__ == '__main__':
    app.run(debug=False)
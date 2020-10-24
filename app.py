import os
from flask import Flask, jsonify, request
from math import sqrt

app = Flask(__name__)


@app.route('/')
def sequencia_fibo():
    a = 0
    b = 1
    x = 0
    fibonacci = '0 1 '

    # 48 porque já inicio com 0 e 1, portanto, os 50 primeiros números.
    while x <= 48:
        c = a + b

        a = b
        b = c

        fibonacci += str(c) + ' '

        x += 1
    return fibonacci


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

from flask import Flask
import numpy as np

# Resourses
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.max_len_seq.html
# https://cyberleninka.ru/article/v/algoritm-formirovaniya-posledovatelnostey-gordona-millsa-velcha
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.welch.html#scipy.signal.welch

app = Flask(__name__)

@app.route('/')
def index():
    return str(items)

if __name__ == '__main__':
    # app.run()

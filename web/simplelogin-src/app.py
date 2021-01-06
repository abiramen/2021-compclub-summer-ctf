from flask import Flask, render_template, request, make_response
app = Flask(__name__, static_url_path='/static')

PASSWORD = 'ireALLyLikEsPaceShiPs207$'
EXPECTED = 'aXJlQUxMeUxpa0VzUGFjZVNoaVBzMjA3JA=='
MESSAGE = f'Password did not match expected encoded result: <kbd>{EXPECTED}</kbd>'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form['username'] == 'spaceman' and request.form['password'] == PASSWORD:
            resp = make_response(render_template("index.html", correct='True'))
        else:
            resp = make_response(render_template("index.html", correct='False', message=MESSAGE))
    else:
        resp = make_response(render_template("index.html", correct='False', message=''))

    resp.set_cookie("cookies-are-yum", value=r"FLAG{1_i_cHeCkeD_f0r_c0oki3S}")
    return resp

if __name__ == '__main__':
    app.run(port=1337)

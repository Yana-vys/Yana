from flask import Flask

app = Flask(__name__)
visit_count = 0

@app.route('/')
def index():
    global visit_count
    visit_count += 1
    return f"Всего посещений: {visit_count}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

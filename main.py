# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os
from flask import Flask, render_template, send_file, request
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/')
def home() :
    return 'hello home'

@app.route('/pic', methods=['GET', 'POST'])
def pic() :
    if request.method == 'POST' :
        f = request.files['file']
        filename = secure_filename(f.filename)
        f.save('C:/Users/User/Desktop/image/' + filename)
        return render_template('img.html', image_file="C:/Users/User/Desktop/image/"+filename)

if __name__ == '__main__' :
    # 실행할 host, port 파라미터로 넣기
    app.run(host="0.0.0.0", port=5000)




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('start')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

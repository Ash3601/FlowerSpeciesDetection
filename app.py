from flask import Flask, render_template, request
from commons import get_tensor
from inference import get_flower_name
from cleaner import clean_image
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

# No caching at all for API endpoints.


@app.after_request
def add_header(response):
    # response.cache_control.no_store = True
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check = 0, pre-check = 0, max-age = 0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '-1'
    return response


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        clean_image()
        return render_template('index.html')

    if request.method == 'POST':
        if 'file' not in request.files or request.files is None:
            print('File not uploaded')
            return 'Error'
        file = request.files['file']
        file.save('static/' + file.filename)
        # image = file.read()
        image = None
        category, flower_name = get_flower_name(image_bytes=image, file=file)
        return render_template('result.html', flower=flower_name, category=category, file=file)


if __name__ == '__main__':
    app.run(debug=True)

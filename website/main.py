from flask import Flask, render_template, send_from_directory, url_for 
from flask_uploads import UploadSet, IMAGES, configure_uploads
from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileRequired, FileField
from wtforms import SubmitField
import requests
import json
from utils import draw_bounding_box

app = Flask(__name__)
app.config['SECRET_KEY'] = 'asfafdfsd'
app.config['UPLOADED_PHOTOS_DEST'] = 'uploads'

photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)

class UploadForm(FlaskForm):
    photo = FileField(
        validators=[
            FileAllowed(photos, 'Only images are allowed'),
            FileRequired('File field should not empty')
        ]
    )
    submit = SubmitField('Upload')

@app.route('/uploads/<filename>')
def get_file(filename):
    return send_from_directory(app.config['UPLOADED_PHOTOS_DEST'], filename)

def get_prediction(filename):
    url = 'https://app.nanonets.com/api/v2/OCR/Model/4d584624-5c10-4d4d-88ce-4a7dfadbb800/LabelFile/?async=false'
    file_url = './uploads/' + filename
    data = {'file': open(file_url, 'rb')}
    response = requests.post(url, auth=requests.auth.HTTPBasicAuth('QvuQc0eB_Oin12L9qzp8xngzcabowqPi', ''), files=data)
    response_json = json.loads(response.text)

    filepath = response_json.get('result')[0].get('filepath')
    new_url = 'https://app.nanonets.com/api/v2/RawOcrResponse?s3_image_path=nanonets/' + filepath
    result = requests.get(new_url, auth=requests.auth.HTTPBasicAuth('QvuQc0eB_Oin12L9qzp8xngzcabowqPi', ''))
    result_json = json.loads(result.text)

    return result_json

@app.route('/', methods=['GET', 'POST'])
def upload_image():
    form = UploadForm()
    if form.validate_on_submit():
        filename = photos.save(form.photo.data)
        file_url = url_for('get_file', filename=filename)
        # TODO: call external API to get prediction
        prediction = get_prediction(filename)
        ocr_file_url = draw_bounding_box(file_url, prediction)
    else:
        file_url = None
        ocr_file_url = None

    return render_template('index.html', form=form, file_url=file_url, ocr_file_url=ocr_file_url)

if __name__ == "__main__":
    app.run(debug=True, port=8000)
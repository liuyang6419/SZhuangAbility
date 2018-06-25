from flask import Flask, render_template, redirect, url_for, session
from flask_wtf.file import FileField, FileAllowed
from werkzeug.utils import secure_filename
from wtforms import SubmitField
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
import os
from autoencoder import get_similar_room_example
from multiprocessing import Pool

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(36)
bootstrap = Bootstrap(app)


class Form(FlaskForm):
    File = FileField(
        '请上传图片：',
        validators=[
            FileAllowed(['png', 'jpg', 'jpeg', 'gif'])
        ])
    submit = SubmitField('上传')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = Form()
    if form.validate_on_submit():
        file = form.File.data
        filename = secure_filename(file.filename)
        pic_path = basedir + '/' + filename
        file.save(pic_path)
        pool = Pool()
        res = pool.apply_async(get_similar_room_example, (pic_path, ))

        session['result_list'] = res.get()
        os.remove(pic_path)
        return redirect(url_for('index'))
    return render_template(
        'index.html', form=form, result_list=session.get('result_list'))


if __name__ == '__main__':
    app.run()

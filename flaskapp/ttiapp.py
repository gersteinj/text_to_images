from flask import Flask, render_template, send_file, flash, redirect, url_for
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
import zipfile


app = Flask(__name__)
app.config['SECRET_KEY']='change-this-before-publishing'

colors = [('Black', 'black'), ('Gray', 'gray'), ('White', 'white'), ('Red', 'red'), ('Orange', 'orange'), ('Yellow', 'yellow'), ('Lime', 'lime'), ('Blue', 'blue'), ('Cyan', 'aqua'), ('Fuchsia', 'fuchsia'), ('Purple', 'purple')]

class WordsForm(FlaskForm):
    word = StringField('Word', validators=[DataRequired()])
    text_color = StringField('Text color', validators=[DataRequired()])
    bg_color = StringField('Background color', validators=[DataRequired()])
    # text_color = SelectField('text color', choices=colors)
    # bg_color = SelectField('background color', choices=colors)
    submit = SubmitField('Make Magnet')

@app.errorhandler(404)
def page_not_found(error):
    return '404 page not found', 404

@app.route('/')
def home():
    # return render_template('index.html')
    return render_template('home.html')

def make_magnet(word, sz, foreground, background):
# Set font and other variables
    fnt = ImageFont.truetype('LinBiolinum_Rah.ttf', int(sz))
    word = '  ' + word + '  '
    bg_color = background
    text_color = foreground

    # create a new image
    img = Image.new("RGB", (10, 10), bg_color)

    # draw text
    # create a draw object
    draw = ImageDraw.Draw(img)

    # use textsize to find size of text
    w, h = draw.textsize(word, font=fnt)
    
    # resize image to fit text
    img = img.resize((w, int(h*1.2)))
    draw = ImageDraw.Draw(img)
    draw.text((0,0), word, font=fnt, fill=text_color)
    return img

@app.route('/tti/<word>')
# @app.route('/tti/<word>/<sz>')
# @app.route('/tti/<word>/<sz>/<foreground>/<background>')
@app.route('/tti/?word=<word>&sz=<sz>&foreground=<foreground>&background=<background>')
def tti(word, sz=40, foreground='black', background='white'):
    byte_io = BytesIO()
    make_magnet(word, sz, foreground, background).save(byte_io, 'PNG')
    byte_io.seek(0)
    return send_file(byte_io, mimetype='image/png')

@app.route('/ttimulti/<words>')
def tti_multi(words):
    word_list = words.split('-')
    with zipfile.ZipFile('test.zip', 'w') as zf:
        for word in word_list:
            n = str(word + '.txt')
            with open(n, 'w') as f:
                f.write(word)
                zf.write(n)
    return render_template('ttimulti.html', words=word_list)

# @app.route('/templating/<pic>')
# def templating(pic):
#     return render_template('templating.html', myvar=pic)

@app.route('/formtest', methods=['GET', 'POST'])
def submit_words():
    form = WordsForm()
    if form.validate_on_submit():
        word = form.word.data
        bg = form.bg_color.data
        fill = form.text_color.data
        flash('You submitted {}'.format(word))
        return redirect(url_for('tti', word=word, foreground=fill, background=bg, sz=50))
    return render_template('formpage.html', form=form, title="Make magnets")
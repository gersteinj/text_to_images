from flask import Flask, render_template, send_file, flash, redirect
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY']='change-this-before-publishing'

class WordsForm(FlaskForm):
    word = StringField('Word', validators=[DataRequired()])
    submit = SubmitField('Make Magnet')

@app.errorhandler(404)
def page_not_found(error):
    return '404 page not found', 404

@app.route('/')
def hello_world():
    # return render_template('index.html')
    return "Welcome to Text to Images!"

def make_magnet(word, sz):
# Set font and other variables
    fnt = ImageFont.truetype('LinBiolinum_Rah.ttf', int(sz))
    word = '  ' + word + '  '
    bg_color = 'white'
    text_color = 'black'

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
@app.route('/tti/<word>/<sz>')
def tti(word, sz=40):
    byte_io = BytesIO()
    make_magnet(word, sz).save(byte_io, 'PNG')
    byte_io.seek(0)
    return send_file(byte_io, mimetype='image/png')

@app.route('/ttimulti/<words>')
@app.route('/ttimulti/<words>/<i>')
def tti_multi(words):
    word_list = words.split('-')
    return render_template('ttimulti.html', words=word_list)

# @app.route('/templating/<pic>')
# def templating(pic):
#     return render_template('templating.html', myvar=pic)

@app.route('/formtest', methods=['GET', 'POST'])
def submit_words():
    form = WordsForm()
    if form.validate_on_submit():
        flash('You submitted!')
        return redirect('/')
    return render_template('formpage.html', form=form, title="Make magnets")
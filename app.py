from flask import Flask, render_template, request
from langdetect import detect
from googletrans import Translator, LANGUAGES

app = Flask(__name__)
app.secret_key = 'translation_app_secret_key'

def detect_and_translate(text, target_lang):
    result_lang = detect(text)
    translator = Translator()
    translate_text = translator.translate(text, dest=target_lang).text
    return result_lang, translate_text

@app.route('/')
def index():
    return render_template('index.html', languages=LANGUAGES)

@app.route('/trans', methods=['POST'])
def trans():
    text = request.form['text']
    target_lang = request.form['target_lang']
    detected_lang, translation = detect_and_translate(text, target_lang)
    return render_template('index.html',
                           translation=translation,
                           detected_lang=detected_lang,
                           recognized_text=text,
                           languages=LANGUAGES)

if __name__ == '__main__':
    app.run(debug=True)

from flask import Blueprint, render_template, request, jsonify
from googletrans import Translator

translate_bp = Blueprint('translate', __name__)

def translate_html(html_content, target_language='ar'):
    translator = Translator()
    translated_content = ""
    for line in html_content.split('\n'):
        if line.strip():  
            translated_line = translator.translate(line, dest=target_language).text
            translated_line = add_style_to_each_tag(translated_line)
            translated_content += translated_line + '\n'
    return translated_content

def add_style_to_each_tag(html_content):
    # Function to add style attribute to each tag in the HTML
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')
    for tag in soup.find_all():
        if tag.name not in ['html', 'head', 'meta', 'link', 'title', 'style', 'script']:
            tag['style'] = 'direction: rtl; text-align: right;'
    return str(soup)

@translate_bp.route('/')
def index():
    return render_template('index.html')

@translate_bp.route('/translate', methods=['POST'])
def translate():
    html_content = request.form['html_content']
    translated_html = translate_html(html_content)
    return jsonify({'translated_html': translated_html})

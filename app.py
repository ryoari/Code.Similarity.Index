import os
from flask import Flask, request, render_template, flash, redirect, url_for
from werkzeug.utils import secure_filename
from database import save_submission, init_db, get_all_submissions
from logic.level_0 import winnow, compare_codes
from logic.level_1 import compare_codes_level1
import itertools

app = Flask(__name__, template_folder='templates')
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size
app.secret_key = 'your_secret_key_here'  # Set a secret key for flash messages

ALLOWED_EXTENSIONS = {'txt', 'py', 'java', 'cpp', 'c'}

init_db()

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_files():
    if 'files' not in request.files:
        flash('No file part')
        return redirect(url_for('index'))
    
    files = request.files.getlist('files')
    
    if not files or files[0].filename == '':
        flash('No selected files')
        return redirect(url_for('index'))
    
    valid_files = [f for f in files if f and allowed_file(f.filename)]
    
    if len(valid_files) < 2:
        flash('Please upload at least two valid files')
        return redirect(url_for('index'))
    
    try:
        file_contents = []
        for file in valid_files:
            filename = secure_filename(file.filename)
            path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(path)
            with open(path, 'r') as f:
                content = f.read()
            file_contents.append((filename, content))
            os.remove(path)  # Remove file after reading

        results = []
        for (file1, content1), (file2, content2) in itertools.combinations(file_contents, 2):
            # Level 0 analysis (Winnowing)
            fingerprints1, _ = winnow(content1)
            fingerprints2, _ = winnow(content2)
            common_fingerprints, _ = compare_codes(content1, content2)
            level0_similarity = (len(common_fingerprints) / min(len(fingerprints1), len(fingerprints2))) * 100

            # If level0_similarity is above a threshold, perform Level 1 analysis
            if level0_similarity > 10:  # You can adjust this threshold
                level1_similarity, detailed_similarity = compare_codes_level1(content1, content2)
            else:
                level1_similarity, detailed_similarity = 0, []

            results.append({
                'file1': file1,
                'file2': file2,
                'level0_similarity': level0_similarity,
                'level1_similarity': level1_similarity * 100,
                'detailed_similarity': detailed_similarity
            })

        return render_template('results.html', results=results)
    except Exception as e:
        flash(f'An error occurred: {str(e)}')
        return redirect(url_for('index'))

@app.route('/history')
def history():
    submissions = get_all_submissions()
    return render_template('history.html', submissions=submissions)

@app.errorhandler(413)
def too_large(e):
    flash('File is too large. Maximum size is 16MB.')
    return redirect(url_for('index'))

@app.errorhandler(500)
def internal_error(error):
    flash('An error occurred processing your request.')
    return redirect(url_for('index'))

if __name__ == '__main__':
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    app.run(debug=True)

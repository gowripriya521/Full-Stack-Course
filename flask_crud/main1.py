import os
import uuid
import io
from flask import Flask, flash, request,jsonify,send_from_directory
from werkzeug.utils import secure_filename
from test import creat_stu,get_stu,update_stu,delete_stu
from new_test import get_all_students, add_student

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg'}

app = Flask(__name__)
app.secret_key = "my-secret-key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024

# 2.File Extension Filtering
def allowed_file(filename):
    return '.' in filename and \
            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # print("FILES:", request.files)
        # print("FILE KEY:", 'file' in request.files)
        # check if the post request has the file part
        if 'file' not in request.files:
            return jsonify({
            'status': 'select the file and filename'
            }), 400
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            return jsonify({'status':'select the file'}),400
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # return redirect(url_for('download_file', name=filename))
            return 'file uploaded'
    return jsonify({"status":'this extension files not allowed'}),400

# 1.Standard File Upload Setup
@app.route("/uploads",methods=['GET','POST'])
def standard_file():
    if request.method == 'POST':
        if 'doc' not in request.files:
            return jsonify({'status':'no file given'}),400
        file = request.files['doc'] 
        if file.filename == '':
            return jsonify({'status':'file name not given'}),400
        if file.name:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return 'file uploaded'
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method="post" enctype="multipart/form-data">
      <input type="file" name="doc">
      <input type=submit value=Upload>
    </form>
    '''

#3.Preventing Directory Traversal Attacks
@app.route("/upload1",methods=['GET','POST'])
def traversal_attacks():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return jsonify({'status':'no file given'}),400
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return jsonify({'status':'file name not given'}),400
        filename = secure_filename(file.filename)
        if not filename:
            return jsonify({"status":"invalid filename"})
        file_path=os.path.join(app.config['UPLOAD_FOLDER'],filename)
        file.save(file_path)
        return 'file uploaded'
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method="post"enctype="multipart/form-data">
      <input type="file" name="file">
      <input type="submit" value="Upload">
    </form>
    '''

#4.Unique Filenames (Collision Avoidance)
@app.post('/upload/avoid')
def unique_file():
    if 'file' not in request.files:
        return jsonify({'error':'No file part'}), 400        
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error':'No selected file'}), 400
    if file:
        # 1. Clean the original filename
        filename = secure_filename(file.filename)        
        # 2. Extract the file extension
        ext = os.path.splitext(filename)[1]        
        # 3. Generate a unique random name and append the extension
        unique_filename = f"{uuid.uuid4().hex}{ext}"
        # 4. Save the file
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], unique_filename))
        return jsonify({'message':f'File uploaded successfully as {unique_filename}'}),200

#5. Setting Maximum File Size Limits
@app.route("/max_1",methods=['GET','POST'])
def setting_max():
    if request.method == 'POST':
        file=request.files.get("file")
        if file:
            file.save('uploads/'+file.filename)
            # file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return 'file uploaded'
        else:
            return "no file selected",400
@app.errorhandler(413)
def request_entity_too_large(error):
    return "File is too large. Maximum upload size is 2 MB.", 413

#6.Handling Multiple File Inputs
@app.route("/uploads_mult",methods=['GET','POST'])
def multiple_file():
    if request.method == 'POST':
        if 'files' not in request.files:
            flash('No file part')
            return jsonify({'status':'no file given'}),400
        files = request.files.getlist('files')
        count=0 
        for file in files:
            if file.filename == '':
                continue
            filename = secure_filename(file.filename)
                # file.save(f'./uploads/{file.filename}')
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            count+=1
        return f'{count} files successfully uploaded'
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
    <input type=file name=files>
    <input type=submit value=Upload>
    </form>
    '''
#7.Serving Uploaded Files Back to the Client in flask
ALLOWED_EXTENSION = {'txt', 'pdf', 'png'}
def allowed_files(filename):
    return '.' in filename and \
            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSION
@app.post('/upload_back')
def file_Send_back():
    if request.method == 'POST':
        # Check if file part exists
        if 'file' not in request.files:
            return "No file part in request", 400
        file = request.files['file']
        if file.filename == '':
            return "No file selected", 400
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)  # Prevent directory traversal
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            return "uploaded_file"
        else:
            return "Invalid file type", 400
    return ['True']
# Serve uploaded file back to client
@app.route('/uploads/<filename>')
def uploaded_file(filename):
        return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)
# 8.File MIME Type Validation via Magic Bytes
# MAGIC_BYTES = {
#     "image/jpeg":b"\xFF\xD8\xFF" ,# JPEG
#     "image/png":b"\x89PNG\r\n\x1a\n",  # PNG
#     "application/pdf":b"%PDF-"   # PDF
# }
# MAX_MAGIC_LEN = max(len(sig) for sig in MAGIC_BYTES)
# def detect_mime_type(file_stream):
#     file_start = file_stream.read(MAX_MAGIC_LEN)
#     file_stream.seek(0)  # Reset pointer for further reading
#     for magic, mime in MAGIC_BYTES.items():
#         if file_start.startswith(magic):
#             return mime
#     return None  # Unknown type
# @app.post("/upload_magic")
# def upload1_file():
#     if "file" not in request.files:
#         return jsonify({"error": "No file part"}), 400
#     file = request.files["file"]
#     if file.filename == "":
#         return jsonify({"error": "No selected file"}), 400
#     # Detect MIME type from magic bytes
#     detected_mime = detect_mime_type(file.stream)
#     if not detected_mime:
#         return jsonify({"error": "Unsupported or unknown file type"}), 400
#     # Optional: Cross-check with client-provided MIME type
#     client_mime = file.mimetype
#     if client_mime != detected_mime:
#         return jsonify({
#             "error": "MIME type mismatch",
#             "detected": detected_mime,
#             "provided": client_mime
#         }), 400
#     # Save file securely
#     save_path = os.path.join("uploads", file.filename)
#     os.makedirs("uploads", exist_ok=True)
#     file.save(save_path)
#     return jsonify({
#         "message": "File uploaded successfully",
#         "mime_type": detected_mime
#     }), 200

#9.Handling In-Memory Files Without Disk Storage
@app.post("/upload/stor")
def upload_files():
    # 1. Receive the uploaded .txt file via POST request
    if 'file' not in request.files:
        return "No file part in the request", 400        
    file = request.files['file']    
    if file.filename == '':
        return "No selected file", 400
    if file and file.filename.endswith('.txt'):
        # 2. Access the underlying stream using io.BytesIO(file.read()) or file.stream
        # Reading the file contents into memory
        file_bytes = file.read()
        in_memory_stream = io.BytesIO(file_bytes)        
        # 3. Read and count the total word count entirely in memory
        text_content = in_memory_stream.getvalue().decode('utf-8')
        words = text_content.split()
        word_count = len(words)        
        # 4. Return the required string format
        return f"Total words in uploaded file: {word_count}"        
    return "Invalid file type. Please upload a .txt file.", 400



if __name__=="__main__":
    app.run(port=8001,host='0.0.0.0',debug=True)
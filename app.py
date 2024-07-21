from flask import Flask, jsonify, send_from_directory
import os
from flask import Flask, request, jsonify


app = Flask(__name__, static_folder='build')

@app.route('/api/data', methods=['GET'])
def get_data():
    data = {
        'message': 'Hello from Flask!'
    }
    return jsonify(data)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists(app.static_folder + '/' + path):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')

@app.route('/download-art', methods=['POST'])
def save_image():
    if 'image' not in request.files:
        return jsonify({'error': 'No art file provided'}), 400
     
    image = request.files['image']
    image_path = os.path.join('images', 'art.png')  
    image.save(image_path)
    return jsonify({'message': 'Art saved successfully'})

if __name__ == '__main__':
    app.run(debug=True)
    
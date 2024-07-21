from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app) 

@app.route('/save-image', methods=['POST'])
def save_image():
    if 'image' not in request.files:
        return jsonify({'error': 'No art file provided'}), 400
     
    image = request.files['image']
    image_path = os.path.join('images', 'art.png')  
    image.save(image_path)
    return jsonify({'message': 'Art saved successfully'})

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin
from PIL import Image
import numpy as np
from collections import Counter

app = Flask(__name__)
CORS(app)  # Enable CORS for the entire app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
@cross_origin()  # Allow CORS for this specific route
def upload_file():
    if 'image' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['image']
    img = Image.open(file.stream).convert('RGB')
    img = img.resize((100, 100))  # Resize image for faster processing
    img_data = np.array(img)

    # Flatten image to list of RGB values
    pixels = img_data.reshape((-1, 3))

    # Count frequency of each color
    counter = Counter(tuple(pixel) for pixel in pixels)

    # Get top 10 most common colors
    most_common = counter.most_common(10)

    # Format output as list of dictionaries with hex and count
    result = [{'color': f'rgb{color}', 'hex': f'#{color[0]:02x}{color[1]:02x}{color[2]:02x}'} for color, _ in most_common]

    return jsonify({'colors': result})

if __name__ == '__main__':
    app.run(debug=True)

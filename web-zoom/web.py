from flask import Flask, send_file, request, render_template_string
from PIL import Image
from io import BytesIO

app = Flask(__name__)
IMAGE_PATH = 'static/messi.jpg'
current_zoom = 0  # porcentaje global


def zoom_image(image_path, zoom_percent):
    with Image.open(image_path) as img:
        w, h = img.size
        zoom_factor = 1 + (zoom_percent / 100)

        new_w = int(w / zoom_factor)
        new_h = int(h / zoom_factor)

        left = (w - new_w) // 2
        top = (h - new_h) // 2
        right = left + new_w
        bottom = top + new_h

        cropped = img.crop((left, top, right, bottom))
        resized = cropped.resize((w, h), Image.LANCZOS)

        buffer = BytesIO()
        resized.save(buffer, format="JPEG")
        buffer.seek(0)
        return buffer


@app.route('/')
def index():
    return render_template_string('''
        <!doctype html>
        <html>
        <head>
            <title>Zoom dinámico</title>
        </head>
        <body style="text-align:center">
            <h2>Imagen con Zoom: <span id="zoom_value">0</span>%</h2>
            <img id="img" src="/zoom_image" width="600"><br>
            <script>
                setInterval(() => {
                    const img = document.getElementById("img");
                    const timestamp = new Date().getTime();
                    img.src = "/zoom_image?ts=" + timestamp;

                    fetch("/get_zoom")
                        .then(resp => resp.json())
                        .then(data => {
                            document.getElementById("zoom_value").innerText = data.zoom;
                        });
                }, 2000); // cada 2 segundos
            </script>
        </body>
        </html>
    ''')


@app.route('/zoom_image')
def zoom_route():
    buffer = zoom_image(IMAGE_PATH, current_zoom)
    return send_file(buffer, mimetype='image/jpeg')


@app.route('/set_zoom')
def set_zoom():
    global current_zoom
    try:
        val = int(request.args.get('value', 0))
        current_zoom = max(0, min(val, 100))
        return f"Zoom actualizado a {current_zoom}%"
    except:
        return "Valor inválido", 400


@app.route('/get_zoom')
def get_zoom():
    return {"zoom": current_zoom}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)


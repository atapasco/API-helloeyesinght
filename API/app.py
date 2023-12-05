from flask import Flask, render_template,jsonify, request
import PIL.Image as Image
import base64, io
import imgData
import Deep
import TextRecognition
import ObjectRecognition
from werkzeug.utils import secure_filename


app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')


@app.route("/reconocimiento_facial")
def resultFacial():
    resultado = Deep.faceDetection()
    return jsonify(resultado)

@app.route("/reconocimiento_texto")
def resultTextRecognition():
    resultado = TextRecognition.textRecognition()
    return jsonify(resultado)

@app.route("/deteccion_objetos")
def resultObjectRecognition():
    objeto = "imagenAPI.jpeg"
    resultado = ObjectRecognition.query(objeto)
    return jsonify(resultado)

@app.route("/imagen")
def Imagen():

    return jsonify({'imagen': imgData.imagen})

@app.route("/imagen", methods=['POST'])
def guardarImagen():
    data = request.form['data']
    imgData.imagen = data
    b = base64.b64decode(data)
    imagenAPI = Image.open(io.BytesIO(b))
    imagenAPI.save("imagenAPI.jpeg")
    return "imagen cargada correctamente"

if __name__ == "__main__":
    app.run(debug=True, port=5000)
# Importamos las librerias
from distutils.log import error
from deepface import DeepFace
import cv2
import mediapipe as mp


def faceDetection():
    # Declaramos la deteccion de rostros
    detros = mp.solutions.face_detection
    rostros = detros.FaceDetection(min_detection_confidence= 0.8, model_selection=0)
    # Dibujo
    dibujorostro = mp.solutions.drawing_utils
    print("la deteccion de rostro ha sido satisfactoria")
    # Empezamos

    # Leemos los fotogramas
    frame = cv2.imread("imagenAPI.jpeg")

    # Correccion de color
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Procesamos
    resrostros = rostros.process(rgb)

    # Deteccion
    if resrostros.detections is not None:
        # Registramos
        for rostro in resrostros.detections:
            # Extraemos informacion de ubicacion
            al, an, c = frame.shape
            box = rostro.location_data.relative_bounding_box
            xi, yi, w, h = int(box.xmin * an), int(box.ymin * al), int(box.width * an), int(box.height * al)
            xf, yf = xi + w, yi + h

            # Dibujamos
            

            # Informacion
            info = DeepFace.analyze(rgb, actions=['age', 'gender', 'race', 'emotion'], enforce_detection= True)

            # Edad
            edad = info['age']

            # Emociones
            emociones = info['dominant_emotion']

            # Race
            race = info['dominant_race']

            # Genero
            gen = info['gender']
            #print(str(gen) + " de " + str(edad) + " años de edad, con estado de animo " + str(emociones) + " de etnia " + str(race))

            # Traducimos
            if gen == 'Man':
                gen = 'Hombre'

                # Emociones
                if emociones == 'angry':
                    emociones = 'enojado'
                if emociones == 'disgust':
                    emociones = 'disgustado'
                if emociones == 'fear':
                    emociones = 'miedoso'
                if emociones == 'happy':
                    emociones = 'feliz'
                if emociones == 'sad':
                    emociones = 'triste'
                if emociones == 'surprise':
                    emociones = 'sorprendido'
                if emociones == 'neutral':
                    emociones = 'neutral'

                # Race
                if race == 'asian':
                    race = 'asiatico'
                if race == 'indian':
                    race = 'indio'
                if race == 'black':
                    race = 'negro'
                if race == 'white':
                    race = 'blanco'
                if race == 'middle eastern':
                    race = 'oriente medio'
                if race == 'latino hispanic':
                    race = 'latino'

            elif gen == 'Woman':
                gen = 'Mujer'

                # Emociones
                if emociones == 'angry':
                    emociones = 'enojada'
                if emociones == 'disgust':
                    emociones = 'disgustada'
                if emociones == 'fear':
                    emociones = 'miedosa'
                if emociones == 'happy':
                    emociones = 'feliz'
                if emociones == 'sad':
                    emociones = 'triste'
                if emociones == 'surprise':
                    emociones = 'sorprendida'
                if emociones == 'neutral':
                    emociones = 'neutral'

                # Race
                if race == 'asian':
                    race = 'asiatica'
                if race == 'indian':
                    race = 'india'
                if race == 'black':
                    race = 'negra'
                if race == 'white':
                    race = 'blanca'
                if race == 'middle eastern':
                    race = 'oriente medio'
                if race == 'latino hispanic':
                    race = 'latina'
            # Mostramos info
        infoIMG = {"genero" : str(gen) , "edad" : str(edad) , "emocion" : str(emociones) , "raza" : str(race)}
        print(infoIMG)
        return infoIMG
    else :
        infoIMG = {"genero" : "null" , "edad" : "null" , "emocion" : "null" , "raza" : "null"}
        return infoIMG
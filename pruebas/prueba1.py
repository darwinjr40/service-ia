import cv2
from collections import deque

from clases.colors import Color
import numpy as np

# Read the image file

# # Display the image
# cv2.imshow('Image', image)

exit;
anchocam, altocam = 640, 360
cuadro = 100

mitad = int(anchocam/2)
cap = cv2.VideoCapture(1)

# cap.set(3, anchocam)
# cap.set(4, altocam)
# cap.set(3,anchocam) #Definirenos un ancho.
# cap.set(4,altocam)
# cv2.namedWindow("Comparacion de Objetos", cv2.WINDOW_NORMAL)
# cv2.resizeWindow("Comparacion de Objetos", anchocam, altocam)
Q = deque(maxlen=128)
while True:
    ret, frame = cap.read()
    if not ret: break;
    height, width, channels = frame.shape

    cv2.putText(frame, 'Ubique agui el abieto # 1', ((cuadro-20), cuadro-20), cv2.FONT_HERSHEY_SIMPLEX, 0.71, Color.VERDE,2)
    cv2.rectangle (frame, (cuadro, cuadro), (mitad - cuadro, altocam - cuadro), Color.VERDE, 2) 
    ox1,oy1 = cuadro, cuadro
    ancho1,alto1 =(mitad - cuadro) - ox1, (altocam - cuadro) - oy1
    ox2, oy2 = ox1 + ancho1, oy1 + alto1
    objeto = frame[oy1:oy2, ox1:ox2]
        
    objeto2 = cv2.imread('mano.jpg')

    # height1, width1, _ = objeto.shape
    # height2, width2, _ = objeto2.shape
    
    
    # target_width = min(width1, width2)
    # target_height = min(height1, height2)
    
    # objeto = cv2.resize(objeto, (target_width, target_height))
    # objeto2 = cv2.resize(objeto2, (target_width, target_height))
    
    # objeto = cv2.convertTo(objeto, cv2.CV_32F)
    # objeto2 = cv2.convertTo(objeto2, cv2.CV_32F)
    
    obj_gris = cv2.cvtColor(objeto, cv2.COLOR_BGR2GRAY)
    obj2_gris = cv2.cvtColor(objeto2, cv2.COLOR_BGR2GRAY)
    # obj_gris = objeto.astype(np.float32) / 255.0
    # obj2_gris = objeto2.astype(np.float32) / 255.0
    
    orb = cv2.ORB_create()
    # Puntos Claves y Descriptores de cada Imagen
    pc1, des1 = orb.detectAndCompute(obj_gris, None)
    pc2, des2 = orb.detectAndCompute(obj2_gris, None)
    if des1 is not None:
        des2 = des2.reshape(-1, des1.shape[1])
        # Una vez obtenemos los descriptores y puntos clave, debemos compararlos
        # El metodo que usaremos se LLama: COINCIDENCIA DE FUERZA BRUTA
        fb = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
        # Compara el primer descriptor del objeto 1 con todos los descriptores del obieto 2
        # Los que sean similares se considerara una coincidencia
        # El crossCheck es para que solo tome la coincidencia mas fuerte
        coincidencias = fb.match (des2, des1)
        coincidencias = sorted(coincidencias, key=lambda x:x.distance)
        
        puntos = []
        for c in coincidencias:
            if (c.distance) <= 51:
                puntos.append(c)
                print(len(puntos))
                Q.append(len(puntos))    
        # puntos = list(filter(lambda x: x.distance <= 51, coincidencias))
                
        if len(puntos) == 0:
            cv2.putText(frame, 'Ubica los Objetos', ((mitad - 150), altocam-20), cv2. FONT_HERSHEY_SIMPLEX, 1, Color.BLANCO, 3)
        elif len(puntos) <= 20:
            cv2.putText(frame,'Objetos Diferentes', ((mitad-150), altocam-20), cv2.FONT_HERSHEY_SIMPLEX, 1, Color.ROJO, 3)
        else:
            cv2.putText(frame, 'Obietos Similares', ((mitad - 150), altocam-20), cv2.FONT_HERSHEY_SIMPLEX, 1, Color.VERDE, 3)
    
    cv2.imshow("Comparacion de Objetos", frame)
    k = cv2.waitKey(1)
    if k == 27: break
    
promedio = np.array(Q).mean(axis=0)   #realizar un promedio de predicción sobre el historial de predicciones anteriores
print(f"PROMEDIO:  {promedio}: COLA:", Q)    
cap.release ()
cv2.destroyAllWindows()
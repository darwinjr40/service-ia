import cv2

from clases.colors import Color


anchocam, altocam = 600, 600
cuadro = 200

mitad = int(anchocam/2)
cap = cv2.VideoCapture(1)

cap.set(3, anchocam)
cap.set(4, altocam)
# cap.set(3,anchocam) #Definirenos un ancho.
# cap.set(4,altocam)
# cv2.namedWindow("Comparacion de Objetos", cv2.WINDOW_NORMAL)
# cv2.resizeWindow("Comparacion de Objetos", anchocam, altocam)
while True:
    ret, frame = cap.read()
    if not ret: break;
    
    cv2.putText(frame, 'Ubique agui el abieto # 1', ((cuadro-20), 180), cv2.FONT_HERSHEY_SIMPLEX, 0.71, Color.VERDE,2)
    cv2.rectangle (frame, (cuadro, cuadro), (mitad - cuadro, altocam - cuadro), Color.VERDE, 2) 
    ox1,oy1 = cuadro, cuadro
    ancho1,alto1 =(mitad - cuadro) - ox1, (altocam - cuadro) - oy1
    ox2, oy2 = ox1 + ancho1, oy1 + alto1
    objeto = frame [oy1:oy2, ox1:ox2]
    obj_gris = cv2.cvtColor(objeto, cv2.COLOR_BGR2GRAY)
    
    cv2.putText(frame, 'Ubique aquí el objeto # 2', ((mitad + 180), 180), cv2.FONT_HERSHEY_SIMPLEX, 0.71, Color.VERDE, 2)
    cv2.rectangle (frame, ((mitad+cuadro), cuadro), (anchocam - cuadro, altocam - cuadro), Color.VERDE, 2)
    ox3, oy3 = (mitad + cuadro), cuadro
    ancho2, alto2 = (anchocam - cuadro)- ox3, (altocam - cuadro) - oy3
    ox4, oy4 = ox3 + ancho2, oy3 + alto2
    objeto2 = frame[oy3:oy4, ox3:ox4]
    # obj2_gris = cv2.cvtColor(objeto2, cv2.COLOR_BGR2GRAY)
    
    # orb = cv2.ORB_create()
    # # Puntos Claves y Descriptores de cada Imagen
    # pc1, des1 = orb.detectAndCompute (obj_gris, None)
    # pc2, des2 = orb.detectAndCompute (obj2_gris, None)
    # # Una vez obtenemos los descriptores y puntos clave, debemos compararlos
    # # El metodo que usaremos se LLama: COINCIDENCIA DE FUERZA BRUTA
    # fb = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    # # Compara el primer descriptor del objeto 1 con todos los descriptores del obieto 2
    # # Los que sean similares se considerara una coincidencia
    # # El crossCheck es para que solo tome la coincidencia mas fuerte
    # coincidencias = fb.match (des2, des1)
    # coincidencias = sorted(coincidencias, key=lambda x:x.distance)
    
    # puntos = []
    # for c in coincidencias:
    #     if (c.distance) <= 51:
    #         puntos.append(c)
    #         print(len(puntos))
            
    # if len(puntos) > 35:
    #     cv2.putText(frame, 'Obietos Similares', ((mitad - 150), 580), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)
    # elif len(puntos) <= 34 and len(puntos) > 1:
    #     cv2.putText(frame,'Objetos Diferentes', ((mitad-150), 580), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
    # elif len (puntos) == 0:
    #     cv2.putText(frame, 'Ubica los Objetos', ((mitad - 150), 580), cv2. FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 3)
    
    cv2.imshow("Comparacion de Objetos", frame)
    k = cv2.waitKey(1)
    if k == 27: break
    
cap.release ()
cv2.destroyAllWindows()
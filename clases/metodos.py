

import base64
import cv2
import numpy as np
from construct import names_files_complete_ext, names_files, coded_files


def es_similar(fra, frb):
    obj_gris = cv2.cvtColor(fra, cv2.COLOR_BGR2GRAY)
    obj2_gris = cv2.cvtColor(frb, cv2.COLOR_BGR2GRAY)
    orb = cv2.ORB_create()
    pc1, des1 = orb.detectAndCompute(obj_gris, None)
    pc2, des2 = orb.detectAndCompute(obj2_gris, None)
    fb = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    coincidencias = fb.match (des2, des1)
    coincidencias = sorted(coincidencias, key=lambda x:x.distance)
    puntos = []
    puntos_men50 = []
    for c in coincidencias:
        if (c.distance) <= 51:
            puntos_men50.append(c.distance)  
        puntos.append(c.distance)
        print(len(puntos))
    # puntos = list(filter(lambda x: x.distance <= 51, coincidencias))   
    # puntos = [x for x in coincidencias if x.distance <= 51]         
    # return "s"
    # return {'data': coincidencias}
    # return {'data': len(puntos)}
    return {
        'Z-dim': len(puntos_men50),
        'a-dim': len(puntos),
        'b-promedio': sum(puntos) / len(puntos),
        'c-lista': puntos,
    }
    
def frame_to_base64(frame):
    ret, buffer = cv2.imencode('.jpg', frame)
    image_64_encode = base64.b64encode(buffer).decode() 
    return image_64_encode  

def compare_imgs(img1, img2):
    # Definir el método de comparación
    method = cv2.TM_CCOEFF_NORMED
    # Aplicar la función matchTemplate
    res = cv2.matchTemplate(img1, img2, method)
    # Definir un umbral para la diferencia
    threshold = 0.8
    # Encontrar las coordeandas de los puntos que superan el umbral
    loc = np.where(res >= threshold)
    print(loc)
    # return loc
    
def compare_imgs1(img1, img2):
    gris1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    gris2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    # Calcular los histogramas de las imágenes
    histograma1 = cv2.calcHist([gris1], [0], None, [256], [0, 256])
    histograma2 = cv2.calcHist([gris2], [0], None, [256], [0, 256])
    # Normalizar los histogramas
    histograma1 /= histograma1.sum()
    histograma2 /= histograma2.sum()
    # Calcular la diferencia entre los histogramas
    diferencia = cv2.compareHist(histograma1, histograma2, cv2.HISTCMP_CORREL)
    print(diferencia)
    return diferencia

def es_similar(img1, img2):
    return compare_imgs1(img1, img2) >= 0.99

def buscar_similares(img1):
    dim = len(coded_files)    
    files = []
    for i in range(0, dim):
        if es_similar(coded_files[i], img1):
            files.append(names_files[i])            
    return files        
            
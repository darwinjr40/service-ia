import cv2

def comparar_imagenes(imagen1, imagen2):
    # Cargar las imágenes
    img1 = cv2.imread(imagen1, cv2.IMREAD_GRAYSCALE)
    img2 = cv2.imread(imagen2, cv2.IMREAD_GRAYSCALE)

    # Crear el objeto SIFT
    sift = cv2.SIFT_create()

    # Detectar y describir los puntos clave en las imágenes
    keypoints1, descriptores1 = sift.detectAndCompute(img1, None)
    keypoints2, descriptores2 = sift.detectAndCompute(img2, None)

    # Crear un objeto BFMatcher (Brute-Force Matcher)
    bf = cv2.BFMatcher()

    # Encontrar las coincidencias entre los descriptores de las imágenes
    coincidencias = bf.knnMatch(descriptores1, descriptores2, k=2)

    # Aplicar el filtro de relaciones de distancia para obtener las mejores coincidencias
    mejores_coincidencias = []
    for m, n in coincidencias:
        if m.distance < 0.75 * n.distance:
            mejores_coincidencias.append(m)

    print(mejores_coincidencias)
    # Dibujar las mejores coincidencias en una nueva imagen
    coincidencias_img = cv2.drawMatches(img1, keypoints1, img2, keypoints2, mejores_coincidencias, None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

    # Mostrar la imagen de coincidencias
    cv2.imshow('Coincidencias', coincidencias_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Ejemplo de comparación de imágenes
imagen1 = 'static/images/1-disco-wagner.png'
imagen2 = 'static/images/2-disco-freno-kashima.jpg'

comparar_imagenes(imagen1, imagen2)

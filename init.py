
import os
import cv2

names_files_complete_ext = []
names_files = []
coded_files = []

def saved_files1(dir): # Obtener la lista de archivos previamente procesados (si existe)
    global names_files, coded_files, names_files_complete_ext               
    previous_files = set(names_files_complete_ext) #names_files_complete_faces    
    current_files = set(os.listdir(dir)) # Obtener la lista actual de archivos en el directorio     
    new_files = current_files - previous_files # Identificar los nuevos archivos (diferencia entre las listas)
    for data in new_files:  
        imgdb = cv2.imread(f'{dir}/{data}')
        # img = cv2.cvtColor(imgdb, cv2.COLOR_BGR2GRAY) # Correccion de color        
        # cod = fr.face_encodings(img)[0] #Codificamos la imagen        
        coded_files.append(imgdb) #almacenamos
        names_files.append(os.path.splitext(data)[0]) #ALmacenamos nombre          
    names_files_complete_ext = list(current_files) # Actualizar la lista de archivos previamente procesados
    print (f"names_files_complete_ext: {names_files_complete_ext}")
    print (f"names_files: {names_files}")
    print (f"new_files: {new_files}")
    print (f"coded_files: {coded_files}")


        
saved_files1(dir='static/images')
print('hola que tal')
    
touch {archivo1,archivo2,archivo3}.txt


import cv2

# Importa la imagen
img = cv2.imread("img/tatsumakiCHU.png")


# Convierte la imagen a RGB
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


# Muestra la imagen
cv2.imshow("Imagen", img)

# Espera a que el usuario presione una tecla
cv2.waitKey(0)

# Cierra la ventana
cv2.destroyAllWindows()
# Sapphire Safari

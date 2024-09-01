import cv2
import numpy as np


def prender_camara():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()

        # Mostrar el frame
        cv2.imshow('Webcam', frame)

        # Presionar q para salir del bucle
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


def blanco_negro(scale = 0.8):
    cap = cv2.VideoCapture(0)

    # PRemidensionado de las imágenes
    if cap.isOpened(): 
        # get vcap property 
        WIDTH  = cap.get(cv2.CAP_PROP_FRAME_WIDTH)   # float `width`
        HEIGHT = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)  # float `height`
    else:
        raise("VideoCapture is not open.")

    ASPECT_RATIO = WIDTH/HEIGHT

    HEIGHT_SCALED = HEIGHT*scale
    WIDTH_SCALED = ASPECT_RATIO*HEIGHT_SCALED*scale

    HEIGHT_SCALED = int(np.round(HEIGHT_SCALED, 0))
    WIDTH_SCALED = int(np.round(WIDTH_SCALED, 0))

    while True:
        ret, frame = cap.read()
        frame = cv2.resize(frame, (WIDTH_SCALED, HEIGHT_SCALED) ) 
        frame_negro = cv2.cvtColor(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY), cv2.COLOR_GRAY2BGR)
        frame_negativo = cv2.bitwise_not(frame_negro)
        frame_combinado = np.hstack((np.hstack((frame, frame_negro)), frame_negativo))

        cv2.imshow('Webcam', frame_combinado)

        # Presionar q para salir del bucle
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

blanco_negro()



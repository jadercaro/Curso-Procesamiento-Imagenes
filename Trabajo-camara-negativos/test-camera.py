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


def blanco_negro():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()

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



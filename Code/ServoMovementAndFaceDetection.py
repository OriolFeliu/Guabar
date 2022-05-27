import numpy as np
import cv2 
import face_recognition
from adafruit_servokit import ServoKit
import sys


class robot:
    #inicializacion de servos y variables
    kit = ServoKit(channels=16)

    servo_base = kit.servo[0]
    servo_base_angle = 0
    servo_arm = kit.servo[1]
    servo_hand = kit.servo[2]
    hand_open = False

    drinks={'cola':60,'fanta':80,'ron':100,'ginebra':130}


    marge = 20

    #posicion de la cara respecto la camara
    def need_mov(self,w,locations):
        x = locations[3]+(locations[1]-locations[3])/2
        if x > w/2 +self.marge:
            return 'right'
        elif x< w/2 -self.marge:
            return 'left'
        else:
            return False

    #capar el movimiento de la base y guardar el angulo actual
    def move_base(self,angle):
        if self.servo_base_angle + angle >=180:
            self.servo_base_angle = 180
            self.servo_base.angle = self.servo_base_angle
        elif self.servo_base_angle - angle <=0:
            self.servo_base_angle = 0
            self.servo_base.angle = self.servo_base_angle
        else:
            self.servo_base_angle = angle
            self.servo_base.angle = self.servo_base_angle
        
    #extender brazo
    def open_arm(self):
        self.servo_arm.angle = 120

    #recoger brazo
    def close_arm(self):
        self.servo_arm.angle = 0

    #abrir mano
    def open_hand(self):
        self.servo_hand.angle = 0
        self.hand_open = True

    #cerrar mano
    def close_hand(self):
        self.servo_hand.angle = 70
        self.hand_open = False

    #movimiento de la base hasta que este centrada con la cara
    def move_base_facedet(self, face_state):
        if face_state == 'left':
            if (self.servo_base_angle + self.marge) <= 180:
                self.servo_base_angle += self.marge
            else:
                self.servo_base_angle = 180
            self.servo_base.angle = self.servo_base_angle
        elif face_state == 'right':
            if (self.servo_base_angle - self.marge) >= 0:
                self.servo_base_angle -= self.marge
            else:
                self.servo_base_angle = 0
            self.servo_base.angle = self.servo_base_angle


    #deteccion de rostros y movimiento de seguimiento
    def detect_faces(self):
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            print("Cannot open camera")
            exit()
        while True:
            # Captura de frames
            ret, frame = cap.read()
            height, width, _ = frame.shape
            if not ret:
                print("Can't receive frame. Exiting ...")
                break
            frame = cv2.flip(frame,1)
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            face_locations = face_recognition.face_locations(frame_rgb)

            if face_locations:
                f_state = self.need_mov(width,face_locations[0])
                self.move_base_facedet(f_state)
                #marcar rectangulo en lasa caras
                top, right, bottom, left = face_locations[0]
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
                #Marcar nomre abajo
                #podria contar con base de datos faciales
                cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
                font = cv2.FONT_HERSHEY_DUPLEX
                cv2.putText(frame, 'Persona', (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
            cv2.imshow('imagen', frame)
            if cv2.waitKey(1) == ord('x'):
                break
        # When everything done, release the capture
        cap.release()
        cv2.destroyAllWindows()

    def serve_order(self,ord_str):
        self.open_hand()
        #coger baso vacio
        self.move_base(45)
        self.open_arm()
        self.close_hand()
        self.close_arm()
        #servir cada bebida pedida - grados predefinidos
        for order in ord_str.split(','):
            self.move_base(self.drinks[order])
            self.open_arm()
            self.close_arm()
        self.move_base(0)
        self.open_arm()
        #detect_faces()

rob = robot()
rob.serve_order('ron,cola')

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import time
import os

def main():
    rtsp_url = "rtsp://192.168.1.61:8554/robot"  # Cambia la IP si es necesario

    cap = cv2.VideoCapture(rtsp_url)

    if not cap.isOpened():
        print("No se pudo abrir el stream RTSP.")
        return

    # Esperamos un poco para asegurar que haya datos
    time.sleep(2)

    ret, frame = cap.read()
    if not ret:
        print("No se pudo capturar el frame.")
        return

    save_path = "/home/HwHiAiUser/rtsp_capture.jpg"
    cv2.imwrite(save_path, frame)
    print("Imagen guardada en {}".format(save_path))

    cap.release()

if __name__ == '__main__':
    main()


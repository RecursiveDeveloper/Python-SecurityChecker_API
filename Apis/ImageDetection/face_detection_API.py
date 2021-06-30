# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 16:35:21 2021

@author: Jhoan
"""
from flask_restful import Resource
from flask import Response
from Apis.ImageDetection import face_detection

class ImageDetectionAPI(Resource):
    def get(self):
        try:
            return Response(face_detection.faceDetection.faceDetectionStartUp(self),mimetype='multipart/x-mixed-replace; boundary=frame')
        except Exception as e:
            print('An error has occurred,\nError info: {}'.format(e))
            return {'ImageDetection' : 'Error'}

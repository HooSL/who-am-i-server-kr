from flask import request
from flask.json import jsonify
from flask_restful import Resource
from http import HTTPStatus
from mysql_connection import get_connection
from mysql.connector.errors import Error
from flask_jwt_extended import jwt_required, get_jwt_identity
from werkzeug.utils import secure_filename
import boto3
from config import Config
from datetime import date, datetime

#papago api import
import os
import sys
import urllib.request
import json

from resources.papago_api import papago

class LableResource(Resource):
    def get(self):
        
        img_url = request.args.get('img_url')
        img_url_list = img_url.split('/')
        photo = img_url_list[-1]

        bucket=Config.S3_BUCKET

        client=boto3.client('rekognition', 'ap-northeast-2',
                        aws_access_key_id = Config.ACCESS_KEY,
                        aws_secret_access_key = Config.SECRET_ACCESS)#boto3 로부터 클라이언트를 받음
        
        response = client.detect_labels(Image={'S3Object':{'Bucket':bucket,'Name':photo}},
        MaxLabels=1)


        print(response['Labels'])

        result = []
        for label in response['Labels']:
            label_dict = {}
            label_dict['Name'] = label['Name']
            label_dict = papago(label['Name'])
            result.append(label_dict)
           

        return{'result':result}

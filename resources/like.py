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


class LikeResource(Resource):
    #좋아요
    @jwt_required()
    def post(self,posting_id):
        
        user_id = get_jwt_identity()

        try :
            # 1. DB 에 연결
            connection = get_connection()
           
            # 2. 쿼리문 만들고
            query = '''insert into `likes`
                        (posting_id, user_id)
                        values
                        (%s, %s);'''
            # 파이썬에서, 튜플만들때, 데이터가 1개인 경우에는 콤마를 꼭
            # 써준다.
            record = (posting_id, user_id)
            
            # 3. 커넥션으로부터 커서를 가져온다.
            cursor = connection.cursor()

            # 4. 쿼리문을 커서에 넣어서 실행한다.
            cursor.execute(query, record)

            # 5. 커넥션을 커밋한다.=> 디비에 영구적으로 반영하라는 뜻.
            connection.commit()

        except Error as e:
            print('Error ', e)
            # 6. username이나 email이 이미 DB에 있으면,
            
            return {'error' : '좋아요 에러입니다.'} , HTTPStatus.BAD_REQUEST
        finally :
            if connection.is_connected():
                cursor.close()
                connection.close()
                print('MySQL connection is closed')

        return {'result':'좋아요 하였습니다.'}

    #좋아요 취소
    @jwt_required()
    def delete(self,posting_id):

        user_id = get_jwt_identity()
        try :
            # 1. DB 에 연결
            connection = get_connection()
            
            # 2. 쿼리문 만들고
            query = '''delete from `likes`
                        where posting_id = %s and user_id = %s;'''
            # 파이썬에서, 튜플만들때, 데이터가 1개인 경우에는 콤마를 꼭
            # 써준다.
            record = (posting_id,user_id)
            
            # 3. 커넥션으로부터 커서를 가져온다.
            cursor = connection.cursor()

            # 4. 쿼리문을 커서에 넣어서 실행한다.
            cursor.execute(query, record)

            # 5. 커넥션을 커밋한다.=> 디비에 영구적으로 반영하라는 뜻.
            connection.commit()

        except Error as e:
            print('Error ', e)
            return {'error' : str(e)} , HTTPStatus.BAD_REQUEST
        finally :
            if connection.is_connected():
                cursor.close()
                connection.close()
                print('MySQL connection is closed')

        return{'result':'좋아요 취소 하였습니다.'}


class LikeListResource(Resource):
    #좋아요 목록 보기
    @jwt_required()
    def get(self) :

        user_id = get_jwt_identity()
        try :
            connection = get_connection()

            query = '''select * 
                        from likes 
                        where user_id = %s; '''

            record = (user_id,)

            cursor = connection.cursor(dictionary = True)

            cursor.execute(query, record)

            # select 문은 아래 내용이 필요하다.
            record_list = cursor.fetchall()
            print(record_list)

             ### 중요. 파이썬의 시간은, JSON으로 보내기 위해서
            ### 문자열로 바꿔준다.
            i = 0
            for record in record_list:
                record_list[i]['created_at'] = str(record['created_at'])
                i = i + 1

        # 위의 코드를 실행하다가, 문제가 생기면, except를 실행하라는 뜻.
        except Error as e :
            print('Error while connecting to MySQL', e)
            return {'error' : str(e)} , HTTPStatus.BAD_REQUEST
        # finally 는 try에서 에러가 나든 안나든, 무조건 실행하라는 뜻.
        finally :
            print('finally')
            cursor.close()
            if connection.is_connected():
                connection.close()
                print('MySQL connection is closed')
            else :
                print('connection does not exist')
        return{'likes_list' : record_list}


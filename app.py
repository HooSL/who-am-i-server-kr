from flask import Flask, request
# JWT 사용을 위한 SECRET_KEY 정보가 들어있는 파일 임포트
from config import Config
from flask.json import jsonify
from http import HTTPStatus

from flask_restful import Api
from flask_jwt_extended import JWTManager
from resources.like import LikeListResource, LikeResource
from resources.posting import MyPostingResource, PostingInfoResource, PostingResource, nuPostingResource
from resources.rekognition import LableResource
from resources.user import UserLoginResource, UserLogoutResource, UserRegisterResource,jwt_blacklist


app = Flask(__name__)

# 환경 변수 셋팅
app.config.from_object(Config)

# JWT 토큰 만들기
jwt = JWTManager(app)


@jwt.token_in_blocklist_loader
def check_if_token_is_revoked(jwt_header,jwt_payload):
    jti = jwt_payload['jti']
    return jti in jwt_blacklist

api = Api(app)

# 경로와 리소스를 연결한다.
#유저 경로 리소스
api.add_resource(UserRegisterResource, '/v1/user/register') #회원가입
api.add_resource(UserLoginResource, '/v1/user/login') #로그인
api.add_resource(UserLogoutResource, '/v1/user/logout') #로그아웃

api.add_resource(PostingResource, '/v1/posting') #포스팅 업로드
api.add_resource(MyPostingResource, '/v1/myposting') #내 포스팅 리스트
api.add_resource(PostingInfoResource, '/v1/posting/<int:posting_id>') #포스팅 수정, 삭제
api.add_resource(nuPostingResource, '/v1/nuposting') #비유저 포스팅 업로드

api.add_resource(LikeResource, '/v1/like/<int:posting_id>')#좋아요, 좋아요 취소
api.add_resource(LikeListResource,'/v1/like') #좋아요 목록

api.add_resource(LableResource, '/v1/labling')#사진 디텍션

if __name__ == '__main__' :
    app.run()


#index -> where 절 order by 절
#인덱스가 설정이 안되어 있으면 나중에 데이터가 많아지면 서버가 느려질수 있다
#DB에서 데이터 가져오는 부분을 full scan 하기 때문


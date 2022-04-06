# __누굴까 서버소스 코드__
Leader : 이후승,
email : dbfoot95@gmail.com  
member : 박가혜,
email : gahye0530@gmail.com<br>
Demo Video : https://www.youtube.com/watch?v=8tPPj9rE23g  
Presentation : https://docs.google.com/presentation/d/1MnkOVfzcFpYsd7S-YSgUd5UwZax6rVwxAK3N6fnDOsA/edit#slide=id.p1  
GitBook : https://undefined-189.gitbook.io/who_am_i/  
Figma : https://www.figma.com/file/eIxiGbryXi4QKPTeQQPFLe/Who-am-I-Project?node-id=0%3A1  

## Introduction
호기심이 많은 유아기 1~6세 아이들이 궁금한 것을 바로 스마트폰으로 촬영하고 확인하며 눈과 귀로 보고 들으며 빠르게 습득할 수 있는 교육용 애플리케이션입니다.  
예를 들면 피아노가 있는 사진을 촬영했을 때 아이에게 피아노 라고 알려주며 음성으로 친근하게 해당 객체가 무엇인지 알려줍니다.  
이 때 사용되는 기술이 객체 인식 인공지능 기술 AWS Rekognition과 텍스트를 음성으로 변환시켜주는 안드로이드 TTS 기술을 활용합니다.  
또한 피아노와 관련된 검색결과를 동영상으로 보여 줌으로써 아이가 해당 객체가 무엇인지 시각으로 확인할 수 있습니다.  
이는 유튜브 검색 API 연동을 통해 제공합니다. 회원 유저는 촬영한 사진을 다른 사용자가 볼 수 있도록 게시판에 업로드 할 수 있습니다.  

## <서버 아키텍쳐>
![서버 아키텍쳐 사진](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fdlue4y%2FbtryxJr3GzK%2F7HCmPSosV2CyklFp1z6UL1%2Fimg.jpg)

로컬서버에서의 테스트를 충분히 한 후 npm기반의 패키지인 Serverless Framework를 사용하기 위해 npm을 설치 후 Serverless Framework를 설치하여 AWS Lambda로 서버 배포했습니다.  
Serverless Framework는 기본적으로 미국동부 서버만 지원하기 때문에 serverless.yml에서 region을 서울로 따로 설정해주어서 미국동부 서버보다 응답 속도를 빠르게 했습니다.  
Serverless에 GitHub를 연동해 푸쉬할 경우에 자동으로 업데이트가 되어 CI/CD가 되도록 하였습니다.  
Lambda 서버는 requirements에 라이브러리가 50mb를 넘기면 에러가 생기기 때문에 Lambda서버와 환경이 같은 AWS EC2에서 프로젝트에 필요한 라이브러리를 설치하고 설치한 파일들을 압축 후 S3에 업로드하고 Lambda Layer 파이썬 버전 3.8.8에 맞게 추가해서 해결하였습니다.  
이미지를 서버에 업로드할 때 흰 상자로 깨지는 현상이 발생해서 serverless.yml에서 apiGateway에 binaryMediaTypes를 추가해 이미지를 정상적으로 받도록 했습니다.  
서버 배포 후 Cloud Watch를 이용해 테스트 및 디버깅 하였습니다.  


## <적용기술>
![적용기술 사진](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FcuASat%2Fbtryx43coq6%2Fbh3YLhUPDwxbo4KkrjW0ZK%2Fimg.jpg)

Rekognition에서 항상 출력값이 영어로 나오기 때문에 네이버 Papago API를 이용하여 결과값이 번역되어 한글로 나오게 하였습니다.

## <기술해석>
![기술해석 사진](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FsZdEY%2FbtrywXwXcQ8%2F6ymy8qZ6k1X4sevzXsbTW0%2Fimg.jpg)

## Development Environment
- MySql Workbench 8.0.27
- Python 3.8 & Serverless v3
- Android Studio Bumblebee | 2021.1.1 Patch 2

## APIs
- Papago API : https://developers.naver.com/docs/papago/README.md
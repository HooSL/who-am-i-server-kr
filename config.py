class Config :
    SECRET_KEY = 'who-am-i-super-secret-key'

    JWT_SECRET_KEY = 'who_am_i_user'
    JWT_ACCESS_TOKEN_EXPIRES = False
    ACCESS_KEY = "ACCESS_KEY"
    SECRET_ACCESS = "wkC/SECRET_ACCESS"

    S3_BUCKET = "who-am-i-kr-data"
    S3_LOCATION = 'https://{}.s3.amazonaws.com/'.format(S3_BUCKET)
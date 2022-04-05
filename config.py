class Config :
    SECRET_KEY = 'who-am-i-super-secret-key'

    JWT_SECRET_KEY = 'who_am_i_user'
    JWT_ACCESS_TOKEN_EXPIRES = False
    ACCESS_KEY = "AKIAYO4EJD54A3QAVGD3"
    SECRET_ACCESS = "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"

    S3_BUCKET = "who-am-i-kr-data"
    S3_LOCATION = 'https://{}.s3.amazonaws.com/'.format(S3_BUCKET)
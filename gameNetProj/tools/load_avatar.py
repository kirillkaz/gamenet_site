from profiles.serializers import UserImagesSerializer
from profiles.models import User, UserImages

import boto3
from botocore.client import Config
from config.settings import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY
from io import BytesIO
import base64

def LoadUserAvatar(username):
    #connect to minio
    s3 = boto3.resource('s3',
                            endpoint_url='http://s3:9000',
                            aws_access_key_id=AWS_ACCESS_KEY_ID,
                            aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                            config=Config(signature_version='s3v4'),
                            region_name='eu-west-1')
    
    user = User.objects.get(login=username)
    avatar_id = user.avatar_id

    if avatar_id == 0:
        buf = BytesIO()
        s3.Bucket('media-bucket').download_fileobj('user.png', buf)
        cleaned_img = base64.b64encode(buf.getvalue()).decode('utf-8')
    
    else:
        buf = BytesIO()
        avatar = UserImages.objects.get(id=avatar_id)
        json_avatar_data = UserImagesSerializer(avatar).data
        s3.Bucket('media-bucket').download_fileobj(json_avatar_data['image_name'], buf)
        cleaned_img = base64.b64encode(buf.getvalue()).decode('utf-8')

    return cleaned_img
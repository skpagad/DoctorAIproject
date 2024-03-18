import boto3
import json

def save_user(s3_client, username, password, user_type, S3_BUCKET_NAME):
    user_data = {'username': username, 'password': password, 'type': user_type}
    s3_client.put_object(Bucket=S3_BUCKET_NAME, Key=f'users/{user_type}/{username}.json',
                         Body=json.dumps(user_data))
    return True

def check_user_exists(s3_client, username, user_type, S3_BUCKET_NAME):
    try:
        response = s3_client.get_object(Bucket=S3_BUCKET_NAME, Key=f'users/{user_type}/{username}.json')
        user_data = json.load(response['Body'])
        return True, user_data
    except s3_client.exceptions.NoSuchKey:
        return False, None

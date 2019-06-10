import os  # 현재 업로드할 파일 탐색

import boto3  # s3에 파일을 업로드 하는 용도
from config import settings

def upload_files(search_path, target_path):
    session = boto3.Session()

    s3 = session.resource('s3')
    bucket = s3.Bucket('m-shop')

    # for subdir, dirs, files in os.walk(path):
    # print(subdir, dirs, files)
    for current_dir, subdirs, files in os.walk(search_path):
        print(current_dir, subdirs, files)
        for file in files:
            full_path = os.path.join(current_dir, file)
            print(full_path)
            with open(full_path, 'rb') as data:
                # 윈도우 사용자들을 위함 그렇지않으면 폴더명/ 으로 되어버림      # media라는 폴더이름을 빼기위함
                bucket.put_object(Key=target_path + '/' + (full_path.replace('\\', '/'))[len(search_path) + 1:],
                                  Body=data, ACL='public-read')


if __name__ == "__main__":
    upload_files('./media', 'media')

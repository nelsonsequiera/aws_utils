import boto3
from aws_utils.response import ResponseObject


def get_item(table_name, key, region, output_format=None):
    data = None
    exception = None
    full_response = None
    session = boto3.session.Session()
    dynamodb = session.resource("dynamodb", region_name=region)
    try:
        full_response = dynamodb.meta.client.get_item(TableName=table_name, Key=key)
        data = full_response.get('Item')  # if no item, key exists but has no attribute
    except Exception as e:
        print(e)
        exception = e
    finally:
        return ResponseObject(data=data,
                              exception=exception,
                              output_format=output_format,
                              full_response=full_response).response()


def put_item(table_name, item, region, output_format=None):
    data = None
    exception = None
    full_response = None
    session = boto3.session.Session()
    dynamodb = session.resource("dynamodb", region_name=region)
    table_object = dynamodb_client.Table(table_name)
    try:
        full_response = dynamodb.meta.client.put_item(TableName=table_name, Item=item)
    except Exception as e:
        print(e)
        exception = e
    finally:
        return ResponseObject(data=data,
                              exception=exception,
                              output_format=output_format,
                              full_response=full_response).response()


{
    'data': '{\n    "name": "name",\n    "age": "24",\n    "country": "India"\n}',
    'success': True,
    'output_format': 'dict',
    'error': None,
    'error_message': None,
    'full_response': {
        'ResponseMetadata': {
            'RequestId': 'xxxxxxxxxxxx',
            'HostId': 'xxxxxxxxxxxx',
            'HTTPStatusCode': 200,
            'HTTPHeaders': {
                'x-amz-id-2': 'xxxxxxxxxxxx',
                'x-amz-request-id': 'xxxxxxxxxxxx',
                'date': 'Sun, 26 May 2019 10:04:23 GMT',
                'last-modified': 'Sun, 26 May 2019 10:04:18 GMT',
                'etag': '"xxxxxxxxxxxx"',
                'accept-ranges': 'bytes',
                'content-type': 'application/json',
                'content-length': '65',
                'server': 'AmazonS3'
            },
            'RetryAttempts': 0
        },
        'AcceptRanges': 'bytes',
        'LastModified': datetime.datetime(2019, 5, 26, 10, 4, 18, tzinfo=tzutc()),
        'ContentLength': 65,
        'ETag': '"xxxxxxxxxxxx"',
        'ContentType': 'application/json',
        'Metadata': {},
        'Body': "<botocore.response.StreamingBodyat0x10591111>"
    },
    'short_traceback': None,
    'full_traceback': None
}


{
    'data': None,
    'success': False,
    'output_format': 'dict',
    'error': 'NoSuchKey',
    'error_message': 'An error occurred (NoSuchKey) when calling the GetObject operation: The specified key does not exist.',
    'full_response': None,
    'short_traceback': ['  File "/Users/nelsonsequiera/.pyenv/versions/3.7.2/envs/aws_utils_test/lib/python3.7/site-packages/aws_utils/s3.py" line 26, in get_object\n    full_response = s3.meta.client.get_object(Bucket=bucket, Key=file_path)\n',
                        '  File "/Users/nelsonsequiera/.pyenv/versions/3.7.2/envs/aws_utils_test/lib/python3.7/site-packages/botocore/client.py", line 357, in _api_call\n    return self._make_api_call(operation_name, kwargs)\n',
                        '  File "/Users/nelsonsequiera/.pyenv/versions/3.7.2/envs/aws_utils_test/lib/python3.7/site-packages/botocore/client.py", line 661, in _make_api_call\n    raise error_class(parsed_response, operation_name)\n'],
    'full_traceback': ['Traceback (most recent call last):\n',
                       '  File "/Users/nelsonsequiera/.pyenv/versions/3.7.2/envs/aws_utils_test/lib/python3.7/site-packages/aws_utils/s3.py", line 26, in get_object\n    full_response = s3.meta.client.get_object(Bucket=bucket, Key=file_path)\n',
                       '  File "/Users/nelsonsequiera/.pyenv/versions/3.7.2/envs/aws_utils_test/lib/python3.7/site-packages/botocore/client.py", line 357, in _api_call\n    return self._make_api_call(operation_name, kwargs)\n',
                       '  File "/Users/nelsonsequiera/.pyenv/versions/3.7.2/envs/aws_utils_test/lib/python3.7/site-packages/botocore/client.py", line 661, in _make_api_call\n    raise error_class(parsed_response, operation_name)\n',
                       'botocore.errorfactory.NoSuchKey: An error occurred (NoSuchKey) when calling the GetObject operation: The specified key does not exist.\n']
}

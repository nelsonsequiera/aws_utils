# AWS utils for lambda

![boto3version](https://img.shields.io/badge/BOTO3-1.9.120-brightgreen.svg?logo=Amazon-AWS&style=for-the-badge) ![pythonversion](https://img.shields.io/badge/python-3.7-brightgreen.svg?logo=Python&style=for-the-badge)

* Wrapper for Boto3
* Handles Exceptions gracefully and returns structured response
* Can be used in lambda layers along with boto3 package

## Install

```pip install -U aws-utils-for-lambda```

## Request

```python
import aws_utils
aws_utils.s3.get_object('bucket_name', 'test_data.json', output_format='dict')
```

## Response (dict)

```python
{
    'data': 'data',
    'success': True,
    'output_format': 'dict',
    'error': "ClientError",
    'error_message': 'error_message',
    'full_response': 'full_response',
    'short_traceback': 'short_traceback',
    'full_traceback': 'full_traceback'
}
```

### How it works

<a href="https://ibb.co/TTtqnDc"><img src="https://i.ibb.co/3scY851/AWS-boto-wrapper-2.png" alt="AWS-boto-wrapper-2" border="0"></a>

Edit diagram [link](https://creately.com/diagram/jw4mq44s2/FzR84qSmt5M5hQTnFntkkXWZk%3D)

#### Currently supported

* S3
  * upload_file
  * get_object
* DynamoDB
  * get_item
  * put_item

#### Example 1

Get S3 object - request:

```python
import aws_utils
response = aws_utils.s3.get_object('bucket_name', 'test_data.json', output_format='dict')
print(response)
```

Get S3 object - response:

```python

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
```

#### Example 2

Get S3 object - request:

```python
import aws_utils
response = aws_utils.s3.get_object('bucket_name', 'test_data.json', output_format='dict')
print(response)
```

Get S3 object - response:

```python
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
```
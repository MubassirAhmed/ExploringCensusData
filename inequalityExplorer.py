import os
import boto3

access_key = 'AKIAYUJWZRTZUBZ7JJ6Z'
access_secret = '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'
bucket_name = 'ma-storage-1'

client_s3 = boto3.client(
    's3',
    aws_access_key_id=access_key,
    aws_secret_access_key=access_secret
)

"""

"""An AWS Python Pulumi program"""

import pulumi
from pulumi_aws import s3

from datetime import datetime

# Getting the current date and time
dt = datetime.now()

# Getting the timestamp
ts = int(datetime.timestamp(dt))

# Create an AWS resource (S3 Bucket)
bucket = s3.Bucket(f"ttang-{ts}")

# Export the name of the bucket
pulumi.export('bucket_name', bucket.id)

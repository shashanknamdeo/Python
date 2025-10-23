rem to know the version of aws
aws --version

rem to configure credentials, Default region name and  Default output format
aws configure

rem enable versioning in s3
aws s3api put-bucket-versioning --bucket my-sync-bucket-shashank --versioning-configuration Status=Enabled

rem list bucket in s3
aws s3 ls

rem upload 'testfile.txt' file in 's3://my-sync-bucket-shashank/sync/' s3 location
aws s3 cp testfile.txt s3://my-sync-bucket-shashank/sync/

rem list object in s3
aws s3 ls s3://my-sync-bucket-shashank

rem create user Sync with least privilage policy
rem {
rem   "Version": "2012-10-17",
rem   "Statement": [
rem     { "Effect": "Allow", "Action": ["s3:ListBucket","s3:ListBucketVersions"], "Resource": "arn:aws:s3:::my-sync-bucket-shashank" },
rem     { "Effect": "Allow", "Action": [
rem         "s3:GetObject","s3:PutObject","s3:DeleteObject",
rem         "s3:GetObjectVersion","s3:DeleteObjectVersion"
rem       ], "Resource": "arn:aws:s3:::my-sync-bucket-shashank/*"
rem     }
rem   ]
rem }


rem Download from S3
aws s3 sync s3://my-sync-bucket-shashank ./local-folder --profile sync

rem upload from S3
aws s3 sync ./local-folder s3://my-sync-bucket-shashank --profile sync

rem synchronizes the local directory D:/Material/Cloud/MobileSync with the S3 prefix s3://my-sync-bucket-shashank/sync/.
rem using rofile 'sync' credential and configuratiom
rem with 'exact-timestamps' means compare timestamp strictly
aws s3 sync "D:/Material/Cloud/MobileSync" s3://my-sync-bucket-shashank/sync/ --profile sync --exact-timestamps






















QUESTION

Another way of login cli without manually enter Cresentals

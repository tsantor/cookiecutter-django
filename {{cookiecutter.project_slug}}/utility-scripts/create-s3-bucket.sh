#!/bin/bash

# Variables - replace these with your desired values
BUCKET_NAME="BUCKET_NAME"  # Must be globally unique
REGION="us-east-1"  # Change to your preferred AWS region

# Check if AWS CLI is installed
if ! command -v aws &> /dev/null; then
    echo "AWS CLI is not installed. Please install it first."
    exit 1
fi

# Create the bucket
echo "Creating S3 bucket: $BUCKET_NAME"
aws s3 mb s3://$BUCKET_NAME --region $REGION

# Set object ownership to allow ACLs
echo "Setting object ownership to allow ACLs..."
aws s3api put-bucket-ownership-controls \
    --bucket $BUCKET_NAME \
    --ownership-controls '{
        "Rules": [
            {
                "ObjectOwnership": "ObjectWriter"
            }
        ]
    }'

# Disable Block Public Access settings
echo "Disabling Block Public Access..."
aws s3api put-public-access-block \
    --bucket $BUCKET_NAME \
    --public-access-block-configuration "BlockPublicAcls=false,IgnorePublicAcls=false,BlockPublicPolicy=false,RestrictPublicBuckets=false"

# Bucket policy for public read access
echo "Applying public read policy..."
aws s3api put-bucket-policy --bucket $BUCKET_NAME --policy '{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PublicReadGetObject",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::'$BUCKET_NAME'/*"
        }
    ]
}'

# CORS configuration
echo "Configuring CORS..."
aws s3api put-bucket-cors --bucket $BUCKET_NAME --cors-configuration '{
    "CORSRules": [
        {
            "AllowedHeaders": ["*"],
            "AllowedMethods": ["GET", "HEAD"],
            "AllowedOrigins": ["*"],
            "ExposeHeaders": [],
            "MaxAgeSeconds": 3000
        }
    ]
}'

echo "Bucket setup complete!"
echo "Bucket URL: http://$BUCKET_NAME.s3-website-$REGION.amazonaws.com"

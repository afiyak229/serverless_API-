Serverless CRUD API with AWS Lambda, API Gateway, and DynamoDB
Project Overview

This project demonstrates how to create a fully serverless CRUD (Create, Read, Update, Delete) application using AWS Lambda, API Gateway, and DynamoDB. The project also includes automation using AWS CloudFormation for infrastructure provisioning and integrates monitoring using AWS CloudWatch.
Features

    Serverless architecture with AWS Lambda to handle CRUD operations.
    API Gateway to expose Lambda functions as a RESTful API.
    DynamoDB for storage of data.
    Automated deployment using AWS CloudFormation.
    CloudWatch monitoring for Lambda, API Gateway, and DynamoDB.
    Secure access with IAM roles and API Gateway authorization.


Prerequisites

Before you start, make sure you have:

    AWS Account with administrative access to Lambda, API Gateway, and DynamoDB.
    AWS CLI installed and configured with your AWS credentials.
    Terraform installed (if you're using Terraform for deployment, but in this case, CloudFormation is used).
    Basic knowledge of Python (or Node.js if you choose that).


Setup Instructions
1. Create and Configure AWS Lambda Function

    Navigate to the AWS Lambda Console.
    Create a Lambda function from scratch and choose Python 3.x as the runtime.
    Attach the provided IAM Role with permissions for DynamoDB and CloudWatch.
    Copy the contents of lambda_function.py into the Lambda function editor or upload as a .zip package.

2. Set Up DynamoDB Table

    Go to the DynamoDB Console.
    Create a table named YourDynamoDBTable.
        Set the primary key as id (String type).
    Use this table to store your items for CRUD operations.

3. Configure API Gateway

    Go to the API Gateway Console and create a REST API.
    Define methods for GET, POST, PUT, and DELETE requests.
    Link each method to the Lambda function created in Step 1.

4. Automate Deployment with CloudFormation

    Upload the template.yaml file in AWS CloudFormation.
    Create a new CloudFormation stack and deploy the API Gateway, Lambda functions, and DynamoDB table automatically.
    After the deployment, note the API Gateway Invoke URL for testing.

Deployment
Using CloudFormation:

    Go to CloudFormation in the AWS Console.
    Click Create Stack.
    Upload template.yaml and click Next.
    Complete the stack creation wizard and wait for the resources to be deployed.

API Endpoints

The API exposes the following endpoints:

    GET /items?id=<id>: Fetches an item from the DynamoDB table based on the provided id.
    POST /items: Adds a new item to the DynamoDB table. Requires a JSON body with the id and item data.
    PUT /items: Updates an existing item in the DynamoDB table. Requires the id and updated data in the request body.
    DELETE /items?id=<id>: Deletes an item from the DynamoDB table based on the id.

Testing the API

You can test the API using curl or Postman.
Example POST Request (Using curl):

curl --header "Content-Type: application/json" \
     --request POST \
     --data '{"id": "1", "name": "Item Name"}' \
     https://<API-Invoke-URL>/items

Example GET Request (Using curl):

curl --request GET "https://<API-Invoke-URL>/items?id=1"

Example DELETE Request (Using curl):

curl --request DELETE "https://<API-Invoke-URL>/items?id=1"

Example PUT Request (Using curl):

curl --header "Content-Type: application/json" \
     --request PUT \
     --data '{"id": "1", "name": "Updated Name"}' \
     https://<API-Invoke-URL>/items

For Postman, create a new request and fill in the appropriate details (method, URL, headers, and body).
Monitoring

CloudWatch automatically collects metrics for Lambda, API Gateway, and DynamoDB:

    Lambda Metrics:
        Invocation count, duration, and error rates.
    API Gateway Metrics:
        Latency, number of requests, and error responses.
    DynamoDB Metrics:
        Read/write capacity usage, throttling, and errors.

To view these metrics:

    Go to CloudWatch in the AWS Console and filter metrics for the relevant services.

Security Best Practices

    IAM Roles:
        Ensure your Lambda function has the least-privileged IAM role to access DynamoDB and CloudWatch.

    API Gateway Authorization:
        Implement API key or IAM Authorization for your API Gateway to restrict unauthorized access.

    DynamoDB Encryption:
        Enable server-side encryption for your DynamoDB table to ensure data security.

Conclusion

This project showcases how to build a fully serverless CRUD API using AWS services like Lambda, API Gateway, and DynamoDB. By leveraging CloudFormation for automation, you can easily deploy the necessary infrastructure. The API is monitored using CloudWatch, and IAM roles provide the security needed for production environments.

Feel free to fork this repository or contribute improvements!

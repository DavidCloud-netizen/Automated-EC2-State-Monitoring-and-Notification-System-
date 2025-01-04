# Automated-EC2-State-Monitoring-and-Notification-System-
The purpose of this project is to create a serverless application that monitors the states of AWS EC2 instances and s3 buckets. 
## Objective  
The purpose of this project is to create a serverless application that monitors the states of AWS EC2 instances and sends timely email notifications to stakeholders. By automating instance state checks, the system improves operational efficiency and ensures critical updates are delivered every 12 hours.  

## Features  
- **Automated Monitoring**: Periodically checks the state of EC2 instances every 12 hours.  
- **Email Notifications**: Sends automated alerts using Amazon Simple Email Service (SES) to notify stakeholders of instance states.  
- **Error Handling**: Integrated with Amazon CloudWatch for detailed logging and debugging, ensuring high reliability.  
- **Serverless Architecture**: Fully serverless solution utilizing AWS Lambda, removing the need for manual monitoring.  

## Technologies Used  
- **AWS Lambda**: Executes the monitoring logic and handles notifications.  
- **Amazon SES**: Delivers email notifications efficiently and securely.  
- **Boto3**: AWS SDK for Python to interact with AWS services programmatically.  
- **Amazon CloudWatch**: Monitors application logs, tracks performance metrics, and provides debugging support.  

## How It Works  
1. **Lambda Function**:  
   - Written in Python, it queries the current state of EC2 instances using the Boto3 SDK.  
   - Executes every 12 hours using a CloudWatch Event Rule trigger.  

2. **Amazon SES**:  
   - Configured to send email alerts to a predefined list of recipients, informing them of EC2 instance statuses.  

3. **Error Handling and Logging**:  
   - Errors during execution are logged in CloudWatch for quick identification and resolution.  

## Setup Instructions  
1. **AWS Lambda**:  
   - Deploy the Lambda function code using the AWS Management Console or CLI.  
   - Ensure the function has appropriate permissions via an IAM role (e.g., `ec2:DescribeInstances`, `ses:SendEmail`).  

2. **Amazon SES**:  
   - Verify email addresses to be used for sending and receiving notifications.  
   - Set up an SES configuration within the same AWS region as the Lambda function.  

3. **CloudWatch Event Rule**:  
   - Schedule a rule to trigger the Lambda function every 12 hours.  

4. **CloudWatch Logs**:  
   - Enable logging to monitor the function's execution and troubleshoot issues.  

## Key Achievements  
- Automated state monitoring of EC2 instances, reducing manual effort and human error.  
- Ensured reliable email notifications for real-time awareness of instance statuses.  
- Improved system transparency and operational responsiveness with serverless design.  

## Challenges  
- Configuring SES for email alerts while adhering to AWS SES sandbox restrictions.  
- Balancing detailed logging in CloudWatch with cost considerations.  

## Future Improvements  
- Expand the notification system to include SMS or Slack alerts.  
- Implement customizable monitoring intervals based on user preferences.  
- Add a user interface for easier management and reporting of instance statuses.  

## Author  
This project was developed as a personal learning initiative to enhance serverless and cloud computing skills.  
Feel free to reach out for questions or collaboration opportunities!  
Email: david.osaik@yahoo.co.uk  
Linkedln: www.linkedin.com/in/david-osaikhuiwu-7b0652235

---

Let me know if you'd like further customization!  

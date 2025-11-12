# 🧩 Problems & Solutions — Website Uptime Monitor

This document records all major issues encountered during the project, their causes, and how they were fixed.

---

## ❌ 1. Error: “No module named 'requests'”

**Cause:**  
The Lambda runtime doesn’t include the external Python `requests` library by default.

**Solution:**  
Replaced `requests` with **urllib3**, which is built into the Lambda Python runtime and doesn’t need manual packaging.

**Code Change:**
```python
# Old
import requests

# New
import urllib3
http = urllib3.PoolManager()
⚠️ 2. Lambda Role Permission Error

Error Message:

AccessDeniedException: User is not authorized to perform dynamodb:PutItem


Cause:
The IAM role used by Lambda didn’t have permissions to access DynamoDB and SNS.

Solution:
Attached the following managed policies to the Lambda execution role:

AmazonDynamoDBFullAccess

AmazonSNSFullAccess

CloudWatchLogsFullAccess

💤 3. No Scheduled Runs Detected

Problem:
EventBridge rule was created but didn’t trigger the Lambda.

Cause:
Rule target was not linked properly to the Lambda function.

Solution:
Reconfigured the rule target:

Open EventBridge → Rules → WebsiteMonitorSchedule

Select Lambda function as the target

Save changes

Test by checking CloudWatch logs after 5 minutes — confirmed success.

📭 4. SNS Alert Not Received

Cause:
The email subscription to the SNS topic wasn’t confirmed.

Solution:
Checked inbox for AWS SNS confirmation email → clicked Confirm Subscription.

⚡ 5. Lambda Timeout During URL Check

Cause:
Lambda default timeout was too short (3 seconds).

Solution:
Increased timeout to 15 seconds under Lambda → Configuration → General settings.

✅ Final System Status
Component	Status	Notes
Lambda	✅ Working	Uses urllib3 for requests
DynamoDB	✅ Working	Logs uptime every run
SNS	✅ Working	Sends alerts instantly
EventBridge	✅ Working	Runs every 5 minutes
CloudWatch	✅ Working	Shows logs for every run
💡 Lessons Learned

Always use built-in libraries (urllib3) when possible in Lambda.

Proper IAM permissions are essential for service communication.

CloudWatch is the best place to debug AWS Lambda issues.

Serverless architecture = fast setup + zero maintenance.

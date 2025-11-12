# 🌐 Website Uptime Monitor (AWS Cloud Project)

## 📖 Overview
The **Website Uptime Monitor** is a serverless AWS project that automatically checks if a website is up and running every 5 minutes.  
If the site goes down, the system instantly sends an alert via **Amazon SNS (Simple Notification Service)**.

This project uses a combination of **AWS Lambda**, **EventBridge**, and **SNS** — all under the **Free Tier**.

---

## 🏗️ Architecture Diagram


[ EventBridge Rule (Every 5 mins) ]
│
▼
[ AWS Lambda Function ]
│
┌─────────┴─────────┐
▼                   ▼
Website Check     SNS Alert (Email)

---

## ⚙️ Components Used

| AWS Service | Purpose |
|--------------|----------|
| **AWS Lambda** | Runs the Python code to check website uptime |
| **Amazon EventBridge** | Triggers the Lambda every 5 minutes automatically |
| **Amazon SNS** | Sends alerts when the website is down |
| **GitHub Pages (or any website)** | The monitored target URL |

---

## 💻 Lambda Function Code (`lambda_function.py`)

```python
import json
import urllib3
import boto3

# Initialize AWS SNS client
sns = boto3.client('sns')

# Built-in HTTP manager (no need for 'requests' library)
http = urllib3.PoolManager()

def lambda_handler(event, context):
    url = "https://haneeo3.github.io/olajobihaneef/#contact"  # target website
    sns_arn = "arn:aws:sns:us-east-1:770854396539:Websitedownalert"

    try:
        response = http.request('GET', url)
        status = response.status

        if status == 200:
            print(f"✅ Website is up! Status: {status}")
        else:
            message = f"⚠️ Website might be down! Returned status code: {status}"
            sns.publish(TopicArn=sns_arn, Message=message, Subject="Website Down Alert")
            print(message)

    except Exception as e:
        error_message = f"❌ Website check failed: {e}"
        sns.publish(TopicArn=sns_arn, Message=error_message, Subject="Website Down Alert")
        print(error_message)

    return {
        'statusCode': 200,
        'body': json.dumps('Website uptime check complete.')
    }

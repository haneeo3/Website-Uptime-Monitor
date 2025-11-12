
---

### 🐍 **lambda_function.py**
```python
import urllib3
import boto3
import time

# Initialize clients
http = urllib3.PoolManager()
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('WebsiteStatus')
sns = boto3.client('sns')

def lambda_handler(event, context):
    url = "https://haneeo3.github.io/olajobihaneef/#contact"
    sns_arn = "arn:aws:sns:us-east-1:770854396539:Websitedownalert"

    try:
        response = http.request('GET', url, timeout=5.0)
        status = response.status
    except Exception as e:
        status = 0
        sns.publish(
            TopicArn=sns_arn,
            Message=f"❌ Website check failed: {str(e)}"
        )

    # Save result to DynamoDB
    table.put_item(Item={
        'URL': url,
        'Timestamp': int(time.time()),
        'Status': status
    })

    # Send alert if site is down
    if status != 200:
        sns.publish(
            TopicArn=sns_arn,
            Message=f"🚨 Website is DOWN! Status code: {status}"
        )
    else:
        print(f"✅ Website is UP! ({status})")

    return {"status": status}

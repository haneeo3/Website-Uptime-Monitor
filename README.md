# 🌐 Website Uptime Monitor — AWS Serverless Project

![AWS](https://img.shields.io/badge/AWS-Lambda-orange)
![Status](https://img.shields.io/badge/Status-Live-brightgreen)
![License](https://img.shields.io/badge/License-MIT-blue)

## 📖 Overview
The **Website Uptime Monitor** is a serverless cloud-based system that automatically checks if a website is online every 5 minutes.

If the site goes down, it immediately sends an **email alert via SNS** and logs the event in **DynamoDB** for tracking uptime history.

This project demonstrates **real-time cloud monitoring automation** using AWS Free Tier services.

---

## 🧱 Architecture

```text
┌──────────────────────────────┐
│  EventBridge (Scheduler)     │
│  Triggers every 5 minutes    │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│       AWS Lambda             │
│  - Checks website status     │
│  - Stores result in DynamoDB │
│  - Sends alert via SNS       │
└──────────────┬───────────────┘
               │
       ┌───────┴────────┐
       │                │
       ▼                ▼
┌────────────┐    ┌──────────────┐
│ SNS Topic  │    │ DynamoDB     │
│ Email Alert│    │ Uptime Log   │
└────────────┘    └──────────────┘

| Service                | Purpose                                     |
| ---------------------- | ------------------------------------------- |
| **AWS Lambda**         | Runs the uptime check logic                 |
| **Amazon EventBridge** | Triggers Lambda every 5 minutes             |
| **Amazon DynamoDB**    | Stores uptime logs (URL, status, timestamp) |
| **Amazon SNS**         | Sends alerts when a site is down            |
| **Amazon CloudWatch**  | Logs Lambda execution results               |

⚙️ Step-by-Step Setup
1️⃣ Create SNS Topic

Go to AWS Console → SNS → Topics → Create topic

Type: Standard

Name: Websitedownalert

Add a subscription → Email → enter your email

Confirm subscription in your email

2️⃣ Create DynamoDB Table

Go to DynamoDB → Create table

Table name: WebsiteStatus

Partition key: URL (String)

Sort key: Timestamp (Number)

Create table

3️⃣ Create Lambda Function

Go to Lambda → Create function

Runtime: Python 3.12

Name: WebsiteUptimeMonitor

Create or use IAM role with:

DynamoDBFullAccess

SNSFullAccess

CloudWatchLogsFullAccess

Paste the code from lambda_function.py

Deploy → Test (You should see ✅ UP or 🚨 DOWN logs)

4️⃣ Schedule Automatic Checks

Go to EventBridge → Rules → Create rule

Rule type: Schedule

Expression:

rate(5 minutes)


Target: your Lambda function

Create rule

Lambda now runs every 5 minutes automatically.

🔍 Verify It Works
Check	Where	Expected Result
Lambda Logs	CloudWatch → Logs	“✅ Website is UP! (200)”
DynamoDB Table	Explore table items	New status entries every 5 mins
Email Alerts (SNS)	Inbox	Alert when site is DOWN
🧠 Why I Built It

✅ Automate website uptime monitoring

📩 Get instant alerts when my site goes down

🧾 Store uptime history for analytics

🧠 Learn & apply AWS serverless architecture

💼 Strengthen my Cloud Engineering portfolio

🚧 Problems Faced

See detailed report in PROBLEMS_AND_SOLUTIONS.md

🚀 Future Improvements

Add multiple URLs to monitor via DynamoDB

Build a web dashboard (API Gateway + HTML/JS)

Track response time (ms)

Send daily uptime summaries

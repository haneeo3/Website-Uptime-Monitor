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

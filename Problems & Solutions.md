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

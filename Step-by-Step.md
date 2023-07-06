# Introduction
This project is intended to demonstrate a real-world use-case for leveraging the [Azure cost management API](https://learn.microsoft.com/en-us/rest/api/cost-management/).

In this post, we will create and/or leverage the following:
- An Azure Web App & Assign an RBAC Role
- AppID
- Password
- TenantID
- SubscriptionID
- Assign Cost Management Reader Privileges to Subscription
- Generate a secrets.py file
- Deploy Circuit Python locally & Connect to Azure cost management API
- Connect a battery and magnets so it can run on any magnetic surface (whiteboard, fridge, etc.) completely wirelessly
- Be awesome

# Create Azure Web App & Assign RBAC Role

1. Login to the [Azure Portal](www.portal.azure.com)
2. Select the CloudShell button illustrated below:
![](1)

3. Run these commands in the Azure Command Line Interface (CLI):
```sql
az ad sp create-for-rbac --name azure-cost-monitor
```

4. Note the following from the output:
```sql
- AppID
- Password
- TenantID
```

5. Navigate to "Subscriptions" in the top search bar, illustrated below:
![](next)

- Select your Subscription and note the SubscriptionID



  

# References/Notes:
# Hardware
- [Adafruit MagTag - 2.9" Grayscale E-Ink WiFi Display (ESP32)](https://www.adafruit.com/product/4800)
- [Lithium Ion Polymer Battery with Short Cable - 3.7V 420mAh](https://www.adafruit.com/product/4236)
- [Mini Magnet Feet for RGB LED Matrices (Pack of 4)](https://www.adafruit.com/product/4631)

# Azure Pre-Requisites
- AppID
- Password
- TenantID
- SubscriptionID
- secrets.py

# Firmware Pre-Requisites
- Install Circuit Python 


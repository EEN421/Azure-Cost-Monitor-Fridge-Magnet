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
- *_Be awesome_*

# Create Azure Web App & Assign RBAC Role

1. Login to the [Azure Portal](www.portal.azure.com)

2. Select the CloudShell button illustrated below: <br/>

![](/img/CLI.png)

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
<br/>

![](/img/az_creds.png)

5. Navigate to "Subscriptions" in the top search bar, illustrated below:
<br/>

![](/img/subs.png)

- Select your Subscription and navigate to the _Overview_ Blade
- Grab your _SubscriptionID_
<br/>

# Build your secrets.py File
- Take the information you just gathered and enter it into the [secrets.py file](https://github.com/EEN421/Azure-Cost-Monitor-Fridge-Magnet/blob/Main/Code/secrets.py) like this: 

```sql
secrets = {
  "ssid" : "Your-WiFi-SSID",
  "password" : "Your-WiFi-PSK",
  "appId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
  "clientSecret": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
  "tenant": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
  "subscription": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
}
```

<br/>

![](/img/subID.png)

# Assign Cost Management Reader Role
Next we have to give our web app permissions to read the cost management information:

1. Navigate to your Subscription and select the _Identity & Access Management (IAM)_ Blade:
<br/>

![](/img/Sub_IAM.png)

2. Click on _+ Add_ then _Add Role Assignment_:
<br/>

![](/img/Role_Assignments.png)

3. Search for, and select _Cost Management Reader_:
<br/>

![](/img/cost_management_reader.png)

4. Search for, and select the _Azure-Cost-Monitor_ entity we created earlier, then click Next/Save:
<br/>

![](/img/Select_Memebers.png)

<br/>



# Program the MagTag
1. Plug your MagTag into your computer using a USB-C cable _capable of transmitting data and not just charging!_
2. Launch UF2 boot loader by double-clicking the Reset button (the one next to the USB C port). You may have to try a few times to get the timing right.
3. You will see a new disk drive appear called MAGTAGBOOT or CIRCUITPY (depending on your hardware model)
4. Copy [these files](https://github.com/EEN421/Azure-Cost-Monitor-Fridge-Magnet/tree/Main/Code) to your device:
- azure.py
- code.py
- secrets.py
- lib folder

5. It should look something like this:
<br/>

![](/img/contents.png)

<br/>

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


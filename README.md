# Product Stock Checker

This Python script is designed to help me secure a pair of pants (which seem incredibly warm and comfy) that are always out of stock. It automates the process of regularly checking the availability of the pants on the website and sends an email notification when the pants become available.

## Features

- Checks the availability of a specific item.
- Sends an email notification if the item is back in stock.
- Uses Selenium WebDriver for web scraping.
- Continuously runs the check every 30 minutes.

## Installation and Setup

1. Install the required Python libraries.
2. Set up the necessary environment variables in a `.env` file in the same directory as the script. The necessary variables are:
- URL: The URL of the product page.
- COLOR_XPATH: The XPath of the color selection element on the page.
- SIZE_XPATH: The XPath of the size selection element on the page.
- FROM_ADDR: The email address from which the notification will be sent.
- TO_ADDR: The email address to which the notification will be sent.
- PASSWORD: The password for the email account from which the notification will be sent.

Please note that this script uses Gmail's SMTP server to send the notification email, so the `FROM_ADDR` and `PASSWORD` should be valid Gmail account credentials.

## Disclaimer
This script should be used responsibly. Make sure you have the rights and permissions to access and interact with the website. Respect the site's `robots.txt` file and terms of service. Please use this tool ethically and responsibly.

Also, note that the tool is currently set up to check the product page every 30 minutes. This frequency was chosen to not overwhelm the server of the product page. If you wish to change this, you can modify the `time.sleep(1800)` line. However, be aware that checking the page too frequently could be perceived as a denial of service attack and may get your IP address banned from the site.

That's all! Happy shopping!
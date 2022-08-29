# nextdns-blacklist-bot
Add blacklist domains Selenium Automation Bot for NextDNS
<h3> Requierements </h3>

 - Firefox WebDriver (geckodriver)
 
 - Selenium
 
 - NextDNS Account

<h3> Usage </h3>

 - Install Selenium
<code> pip install selenium </code>

 - Edit denylist.txt file, type what you want to add to the NextDNS blacklist.

 - Start Python File
<code> py main.py </code>

<h3> Limitations / Issues </h3>

- It waits 20 seconds on every 10 domains. (Because NextDNS uses HTTP request limitation)

- When some domains are incorrect, the next domain is being added incorrectly.

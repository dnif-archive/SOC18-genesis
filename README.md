  
## **Project Name: Genesis**  
________________________________________  


**Project Description**

Genesis is a 'DNIF Open Source' project which aims at exhibiting a detailed process of ingesting large volumes of real-time data inside DNIF and performing operations on it and generating alerts. DNIF also serves as analytics tool to be able to query our data to look for a specific item or chain of events.
The main objective of this project is to work on real-time dataset, parse the data , store the data in the DNIF platform and perform analysis and provide the users the result in a form of Dashboard

**Selection of the Datasource**

The datasource which was chosen was based on thorough discussion and based on real-world test cases. Upon discussion we were able to understand that upon multiple type of attacks in the present cyberworld, bruteforce attacks / dictionary attacks are one of the most troublesome and most puny attack in front of the cyberworld.
Hence, we have chosen the database : http://bruteforcers.net
as our database. This datasource simply provides us data based on the bruteforce attacks which has been made to the specific network.

 
**Need**

Rapid communication of threats, attacks and cyber security alerts helps to quickly detect, respond and contain cyber-attacks. In-depth analysis can be also performed on the attacks and vulnerabilities to prevent future attack and provide a solution.
*Detecting Brute Force Attacks*

Brute force attacks are difficult to stop, but they aren’t difficult to spot. Some of the methods to detect the attacks are as follows:

--Each failed login attempt records an HTTP 401 status code, so monitoring log files can let you know if you’re under attack.</br>

--Several failed login attempts from the same IP address</br>

--Logins with multiple username attempts from the same IP address</br>

--Logins for a single account from many different IP addresses</br>

--Failed login attempts from alphabetically sequential usernames and passwords</br>

--Logins with a referring URL of someone’s mail</br>

--Excessive bandwidth consumption over the course of a single session</br>

--A large number of authentication failures</br>


*Prevention Methods*

The simplest defense for Brute Force attacks is to maintain cyber hygiene like:

--Users should have complex passwords that are long and use a combination of letters, special characters, numbers and upper- and lower-case letters.</br>

From an IT perspective, prevention measures include </br>
> Locking a login page for a certain amount of time after failed logins,</br>
> Extending the time between two logins when a wrong password is entered,</br>
> Two-factor authentication, </br>
> Using CAPTCHA to prevent automated attacks,</br>
> Locking out an IP address with multiple failed logins.</br>
> Using pattern of attacks and allocate control based resources likewise so as to avoid the attempts of attack</br>
> Implementation of web application based and multi layered firewall would help to avoid such attacks</br>


Though these steps may hinder some attacks, for persistent hackers, it may just slow down their efforts, not stop them. And more sophisticated hackers—particular those using botnets—can circumvent some of these measures.In fact, some prevention methods, such as locking accounts, can backfire. Perpetrators can abuse the security measure and lock out hundreds of user accounts and launch a denial of service (DoS) attack.

While not all cyber attacks can be thwarted, we can make it more difficult for them to follow through with malicious activity.

Hence we can concur that, the best way to detect a bruteforce attack is by proper analysis and user sensitivity or attentiveness towards cyber hygiene.


**Platform**
As mentioned earlier , the project is based on DNIF platform. But the platform had certain dependencies and certain other tools as belows:

•	Virtual Box </br>
•	JetBrains: PyCharm Community Edition</br>
•	Ubuntu 16.04 or above</br>
•	Docker</br>



**Tools**

All kinds of tools for parsing, creating and editing can be used for Threat Intelligence.
But in this project we used simple Python based code to parse the data out of the data source. This helped us to use Python based libraries like Beautiful Soup ver 4.0 in our code. Using the same we were also free to store the data in the required format i.e., the xls/json/csv formats to store the data and further post the data to the platform used (DNIF). 
As per the need of posting the data we also used certain tools like Postman to POST the data but parallelly same functionality using the code.



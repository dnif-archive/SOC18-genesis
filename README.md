  
<h1> Genesis </h1>


**Project Description**

Genesis is a ['DNIF](https://dnif.it/how-it-works.html) Open Source' project which aims at exhibiting a detailed process of ingesting large volumes of [real-time data inside DNIF](https://dnif.it/how-it-works.html) and performing operations on it and generating alerts. DNIF also serves as analytics tool to be able to query our data to look for a specific item or chain of events.
The main objective of this project is to work on real-time dataset, parse the data , store the data in the DNIF platform and perform analysis and provide the users the result in a form of Dashboard.


<p align="center"> <a href="https://www.youtube.com/watch?v=05JhwxznOmg" target="_blank"><img src="http://img.youtube.com/vi/05JhwxznOmg/0.jpg" 
alt="Roadmap-Team Genesis" width="360" height="280" border="10" align="center" /></a></p>

Please refer https://github.com/dnif/SOC18-genesis/wiki to understand the step by step process carried out during each phase of the project in detail for a better understanding.

**Selection of the Datasource**

The datasource which was chosen was based on thorough discussion and based on [real-world test cases](https://github.com/dnif/SOC18-genesis/wiki/Research-on-Various-Datasets-Static-and-Dynamic-Datasets). Upon discussion we were able to understand that upon multiple type of attacks in the present cyberworld, bruteforce attacks / dictionary attacks are one of the most troublesome attack in front of the cyberworld.
Hence, we have chosen the datsource : http://bruteforcers.net </br>
as our database. This datasource simply provides us data based on the bruteforce attacks which has been made to the specific network. 

<p align="center"> <a href="https://www.youtube.com/watch?v=BM45k0meXkE" target="_blank"><img src="http://img.youtube.com/vi/BM45k0meXkE/0.jpg" 
alt="Bruteforce" width="360" height="280" border="10" align="center" /></a></p>


***Need***

Rapid communication of threats, attacks and cyber security alerts helps to quickly detect, respond and contain cyber-attacks. In-depth analysis can be also performed on the attacks and vulnerabilities to prevent future attack and provide a solution.
*Detecting Brute Force Attacks*

Brute force attacks are difficult to stop, but they aren’t difficult to spot. Some of the methods to detect the attacks are as follows:

> •Each failed login attempt records an HTTP 401 status code, so monitoring log files can let you know if you’re under attack.</br>
> •Several failed login attempts from the same IP address</br>
> •Logins with multiple username attempts from the same IP address</br>
> •Logins for a single account from many different IP addresses</br>
> •Failed login attempts from alphabetically sequential usernames and passwords</br>
> •Logins with a referring URL of someone’s mail</br>
> •Excessive bandwidth consumption over the course of a single session</br>
> •A large number of authentication failures</br>


***Prevention Methods***

The simplest defense for Brute Force attacks is to maintain cyber hygiene like:

> •Users should have complex passwords that are long and use a combination of letters, special characters, numbers and upper- and lower-case letters.</br>

From an IT perspective, prevention measures include </br>
> •Locking a login page for a certain amount of time after failed logins,</br>
> •Extending the time between two logins when a wrong password is entered,</br>
> •Two-factor authentication, </br>
> •Using CAPTCHA to prevent automated attacks,</br>
> •Locking out an IP address with multiple failed logins.</br>
> •Using pattern of attacks and allocate control based resources likewise so as to avoid the attempts of attack</br>
> •Implementation of web application based and multi layered firewall would help to avoid such attacks</br>


Though these steps may hinder some attacks, for persistent hackers, it may just slow down their efforts, not stop them. And more sophisticated hackers—particular those using botnets—can circumvent some of these measures.In fact, some prevention methods, such as locking accounts, can backfire. Perpetrators can abuse the security measure and lock out hundreds of user accounts and launch a denial of service (DoS) attack.

While not all cyber attacks can be thwarted, we can make it more difficult for them to follow through with malicious activity.

Hence we can concur that, the best way to detect a bruteforce attack is by proper analysis and user sensitivity or attentiveness towards cyber hygiene.


**Platform**

As mentioned earlier , the project is based on [DNIF platform](https://github.com/dnif/SOC18-genesis/wiki/Installation-Process-of-DNIF). But the platform had certain dependencies and certain other tools as belows:

•	Virtual Box </br>
•	JetBrains: PyCharm Community Edition</br>
•	Ubuntu 16.04 or above</br>
•	Docker</br>



**Tools**

All kinds of tools for parsing, creating and editing can be used for Threat Intelligence.
But in this project we used simple [Python based code](https://github.com/dnif/SOC18-genesis/wiki/Choose-a-real-time-data-set-(csv,-excel-or-json)-or-fetch-it-using-web-scraping-code-%5BCODE-Explanation%5D) to parse the data out of the data source. This helped us to use Python based libraries like Beautiful Soup ver 4.0 in our code. Using the same we were also free to store the data in the required format i.e., the xls/json/csv formats to store the data and further post the data to the platform used (DNIF). 
As per the need of posting the data we also used certain tools like [Postman to POST the data](https://github.com/dnif/SOC18-genesis/wiki/Static) but parallelly same [functionality using the code](https://github.com/dnif/SOC18-genesis/wiki/Dynamic).

[**Identification of Key Indicators for the selected Dataset**](https://github.com/dnif/SOC18-genesis/wiki/Identification-of-Key-Indicators)

<table class="tg">
  <tr>
    <th class="tg-baqh" colspan="3">Key Indicators</th>
  </tr>
  <tr>
    <th class="tg-baqh">Sr No.</th>
    <th class="tg-baqh">Key Indicators</th>
    <th class="tg-baqh">Description</th>
  </tr>
  <tr>
    <td class="tg-baqh">1.</td>
    <td class="tg-baqh">Internal ID</td>
    <td class="tg-baqh">	Indicates a unique identification for each bruteforce attack in the network originating from a given IP Address from a specific location.</td>
  </tr>
  <tr>
    <td class="tg-baqh">2.</td>
    <td class="tg-baqh">Date</td>
    <td class="tg-baqh">Indicates  Current Date of the originated attack.</td>
  </tr>
  <tr>
    <td class="tg-baqh">3.</td>
    <td class="tg-baqh">IP Address</td>
    <td class="tg-baqh">Source IP Address for the Identified attack on the network.</td>
  </tr>
  <tr>
    <td class="tg-baqh">4.</td>
    <td class="tg-baqh">Type</td>
    <td class="tg-baqh">Type of the server in the Network.</td>
  </tr>
  <tr>
    <td class="tg-baqh">5.</td>
    <td class="tg-baqh">Country</td>
    <td class="tg-baqh">Country from which the attack originated.</td>
  </tr>
  <tr>
    <td class="tg-baqh">6.</td>
    <td class="tg-baqh">Organization</td>
    <td class="tg-baqh">Organization from which the attack originated.</td>
  </tr>
</table>


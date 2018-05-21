  
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

**Identification of Key Indicators for the selected Dataset**

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

<p align="center"> <a href="https://www.youtube.com/watch?v=LpgrAo6DI8A" target="_blank"><img src="http://img.youtube.com/vi/LpgrAo6DI8A/1.jpg" 
alt="Bruteforce" width="360" height="280" border="10" align="center" /></a></p>

## Analysis using DQL and Dashboard

### 1. Analysis according to Country
Query Used

`_fetch * from bruteforcenew limit 1000`
`>>_aggcount_unique $Country`
 
 ![image](https://user-images.githubusercontent.com/37012140/40331608-8ea8c37c-5d6e-11e8-9c0b-404e099c0353.png)
 
 ![image](https://user-images.githubusercontent.com/37012140/40331616-92f64cec-5d6e-11e8-9e41-2dfbb776253e.png)
 
 
According to this report we can identify the origin of the attack and create a more preventive environment. From the report Brazil is the origin of most attacks so if an request from that location arrives on network we divert it to a reCAPTCHA page so that we examine if the request is automated or not if it’s an automated request then it would be blocked.  So Top 5 countries on the list get diverted to preventive environment.

### 2. Analysis according to Organisation attacked using Wordpress script
Query Used

`_fetch * from bruteforcenew where $Type=Wordpress limit 100`
`>>_aggcount_unique $Organization`
 
 ![image](https://user-images.githubusercontent.com/37012140/40331624-9887ec42-5d6e-11e8-9bda-76493e3ec655.png)
 
 ![image](https://user-images.githubusercontent.com/37012140/40331630-9cff6ca0-5d6e-11e8-97ec-49750d0dc0c4.png)
 
From this report we can establish that from which organization most Wordpress brute force script attack occurs. So if a request from Top 10 organisation comes it would get blocked or it would be taken to the preventive environment like reCAPTCHA. So to mitigate the attack. If an organization continuously increases its attacks then all the request from that website would get blocked until it is resolved. 
### 3. Analysis of attack density from a region
Query Used

`_fetch * from bruteforcenew limit 100`
`>>_aggcount_unique $Country`

Chart Type : Geo Map </br>

Country_CodeFields : $Country  </br>

Value :Count_Unique </br>
 
![image](https://user-images.githubusercontent.com/37012140/40331633-a1a4877c-5d6e-11e8-9d91-d893859fcee5.png)


![image](https://user-images.githubusercontent.com/37012140/40331641-a5539af2-5d6e-11e8-8434-3a6eef9080d4.png)

 
From above data we can conclude the region from which most attacks originates so requests from South Asia, South and North America  are more likely to be monitored and go through reCAPTCHA page then the request originated from Oceanic region. Multilayer firewall are applied for the request originated from risky location.









### 4.Analysis of SSH brute force attack from a country on a specific date
Query Used

`_fetch * from bruteforcenew where Date=18-05-2018 AND $Type=SSH limit 1000`
`>>_aggcount_unique $Country`
 </br>
 
Pie Chart

![image](https://user-images.githubusercontent.com/37012140/40331649-aa996f46-5d6e-11e8-843f-12d56040c7c2.png)

![image](https://user-images.githubusercontent.com/37012140/40331654-aef68af6-5d6e-11e8-9de4-74aa648c5424.png)

This data allow us to analyse amount of SSH attack originated from a particular country on a specific date. So from this data we can block all the request originated from China on 18/05/2018 as 9 brute force ssh attack happed only on 18/05/2018 so all the request originating from China would be blocked until further preventions are taken. Requests originates from U.S.A. are diverted to reCAPTCHA page for detecting Automation attacks or script attack.  

### 5. Most attack originating from a Organisation
Query Used


`_fetch * from bruteforcenew limit 1000`
`>> _agg max $Organisation`
 </br>
 
Result: netvision

![image](https://user-images.githubusercontent.com/37012140/40331662-b43487fc-5d6e-11e8-9a41-5b68d09ebbaf.png)

![image](https://user-images.githubusercontent.com/37012140/40331669-b81e4678-5d6e-11e8-9bb8-0a5a8ce19b9e.png)
 
From this data we determine which Organisation generates most brute force attack. So that we can block all the request originated from that Organisation.




### 6. Most attack originating from a Country
Query Used


`_fetch * from bruteforcenew limit 100`
`>> _agg max $Country`

 </br>
Result : n/a
 
![image](https://user-images.githubusercontent.com/37012140/40331674-bd30534a-5d6e-11e8-97a2-081db9825ffc.png)

![image](https://user-images.githubusercontent.com/37012140/40331681-c29fc838-5d6e-11e8-8ffa-bc7d3a24729d.png)
 
From above data we can determine which country producing most attacks from which we can block the entire request originating from a country or using preventive measures like Multilayer firewall and reCAPTCHA test for determining automation attacks.






### 7. Analysing attacks originated from a specific IP Address
Query used

`_fetch $IPAddress , $Country  , $Organization from bruteforcenew where $Country=India AND $Type=Wordpress AND $Date=18-05-2018 limit 100>>_aggcount_unique $IPAddress , $Organization`

![image](https://user-images.githubusercontent.com/37012140/40331687-c7e14f06-5d6e-11e8-9e04-f24e6c00fc21.png)

![image](https://user-images.githubusercontent.com/37012140/40331696-cbf2f356-5d6e-11e8-8837-43d4f9b1fbf8.png)
 
From this data we can examine each IP Address and amount of attack it generates so that it can be blocked and strictly prohibit any further connection with most attacks generated from a specific IP Address. From above data we can see that 223.189.229.208 which is from Airtel Organisation.  


### 8. Analysing attacks according to its  type
Query used

`_fetch * from bruteforcenew limit 1000>>_aggcount_unique $Type`
 
![image](https://user-images.githubusercontent.com/37012140/40331704-d1273206-5d6e-11e8-8948-1e3333f25ed5.png)

![image](https://user-images.githubusercontent.com/37012140/40331710-d54a44a4-5d6e-11e8-8113-1bcadd3b1738.png)
 
From this information we can examine that which brute force attack happens and it amount. So from this information we can conclude WORDPRESS type has most attack and can set up mitigation techniques like reCAPTCHA and Multilayered Firewall for blocking any request with this and also create new techniques to mitigate it. 




### 9. Analysis of Most specific type of attack on a day
Query Used  </br>


` _fetch * from bruteforcenew limit 1000 `
`>>_aggcount_unique $Date,$Type`

![image](https://user-images.githubusercontent.com/37012140/40331717-d9415a34-5d6e-11e8-8f9e-e219a7d7b1ca.png)
![image](https://user-images.githubusercontent.com/37012140/40331722-dd19eb6c-5d6e-11e8-9773-73b40e3c5ea6.png)

 
 
From this information we can determine type of attack happened on a specific date and according to that we can create an model to predict which type of attack most likely to happen on specific date using time series analysis.


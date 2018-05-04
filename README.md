# SOC18-genesis
Summer Of Code (SOC) - 2018, Genesis.  
**Project Name: Genesis**  
________________________________________  
**Project Description**

Genesis is a 'DNIF Open Source' project which aims at exhibiting a detailed process of ingesting large volumes of real-time data inside DNIF and performing operations on it and generating alerts. DNIF also serves as analytics tool to be able to query our data to look for a specific item or chain of events.  
 
**Need**

Rapid communication of threats, attacks and cyber security alerts helps to quickly detect, respond and contain cyber-attacks. In-depth analysis can be also performed on the attacks and vulnerabilities to prevent future attack and provide a solution.

**Platform**

DNIF is an Open Big Data Analytics Platform that can ingest, parse, enrich large volumes of data each day and bounce back with actions using complex rules, profilers and machine learning models. 
Visit https://dnif.it to know more.
Dependencies
```
We run DNIF using:
•	Virtual Box
•	JetBrains: PyCharm Community Edition
•	Ubuntu 16.04 or above
•	Docker
```

**Sources**

Most of the resources listed below provide lists and/or APIs to obtain (hopefully) up-to-date information with regards to threats/attacks. Some consider these sources as threat intelligence, opinions differ however. A certain amount of (domain- or business-specific) analysis is necessary to create true threat intelligence.

**Frameworks and Platforms**
Frameworks, platforms and services for collecting, analyzing, creating and sharing Threat Intelligence.

**Tools**
All kinds of tools for parsing, creating and editing Threat Intelligence. Mostly IOC based.

**Research, Standards and Books**

All kinds of reading material about Threat Intelligence, data analysis, cyber analytics; includes (scientific) research and whitepapers.

Data Driven Security
Uncover hidden patterns of data and respond with countermeasures. Security professionals need all the tools at their disposal to increase their visibility in order to prevent security breaches and attacks. This careful guide explores two of the most powerful data analysis and visualization. You'll soon understand how to gather feedback, measure the effectiveness of your security methods, and make better decisions.
	







________________________________________



**Project Execution**

The project will be executed in 2 phases:

**Phase 1**

**Step 1:**  
Understand DNIF platform and how it works: https://dnif.it/how-it-works.html
Installing and getting started with DNIF: https://dnif.it/docs/guides/getting-started/  
**Step 2:**  
Research different data-sets available and choose a data-set from area of interest.	For testing purpose, choose a static data set and it should have required parameters and should follow json, csv or excel format or can be fetched using web scrapping code.  
**Step 3:**  
Upload the data-set to the data store of DNIF; refer the guidelines mentioned on the website.  
**Step 4**  
Identify key parameters for the uploaded data-sets, perform queries to raise the alerts specific to domain of business and create dash board.  
In order to raise alerts you need to configure SMTP server details: https://dnif.it/docs/guides/tutorials/configuring-smtp-in-docker.html  
 





**Phase 2**

**Step 1:**  
Select a data-set that provides real time exchange of threat data for cyber-attacks. Choose a real-time data-set (csv, excel or json) or fetch it using web-scraping code.  
**Step 2:**  
The real-time data should be fed to DNIF. Connector/API code is required while uploading the data-set to DNIF.  
**Step 3:**  
Identify key parameters to raise alerts on the dashboard by performing queries and data analysis.  
 

# Introduction

This project aims to visualize, map, and analyze crime trends in Tunisia based **only** on text data scraped from online news media articles. Having timely and accurate information about crime incidence are important to the average citizen who wants to visit or move to a new city or town; as well as to public officials, policy makers, urban planners, civil society, researchers, etc. Such information can be found on government and independent aggregation websites such as macrotrends.net, but exists only in coarse-grain form (annual at the country level). On the other hand, online news media stories are a rich source of such information, albeit hidden in unstructured text form. We will use tools of natural language processing and machine learning to extract this information, and make it available to the public via an interactive dashboard-like tool. The user will be able to browse and visualize this information by crime type, geographic location, and time frame.

# Data

The data for this project consists of news articles automatically scraped from about popular Tunisian news websites and portals from the past few years. A sample of around 8000 such articles scraped from the society pages of 2 popular daily newspapers, "Assarih" (http://assarih.com/) and "Essada" (https://essada.net/), are available in the data folder.


# Methodology

At a high level, the main tasks of this project are to extract geographical patterns of crime (distribution of crime by location; 
identifying crime hot spots at the city and national levels), and temporal trends (how crime evolves over time; identifying seasonal 
patterns and exceptional spikes).Extracting such patterns from raw text data will require various natural text processing and machine 
learning tasks, mainly information extraction, aggregation, clustering, and time series analysis.

It is worth mentioning that working with Arabic language text adds an extra level of difficulty to this project because there are far 
less advanced NLP resources and tools for the Arabic than English.

# Bibliography

1. Rexy Arulanandam Bastin, Tony Roy, Savarimuthu Maryam, A. Purvis, "Extracting Crime Information from Online Newspaper Articles", Proceedings of the Second Australasian Web Conference (AWC 2014), Auckland, New Zealand, 2014.

2. Hitesh Kumar Reddy ToppiReddy, Bhavna Saini, Ginika Mahajan, "Crime Prediction & Monitoring Framework Based on Spatial Analysis", International Conference on Computational Intelligence and Data Science (ICCIDS 2018), 2018.

3. Isuru Jayaweera, Chamath Sajeewa, Sampath Liyanage, Tharindu Wijewardane, Indika Perera, "Crime Analytics: Analysis of Crimes Through Newspaper Articles", Moratuwa Engineering Research Conference (MERCon), 2015.


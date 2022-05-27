# Synopsis
## Context
"I’m an avid bike commuter and I recently moved to Austin. I reviewed all the bike-related crashes from Texas DOT’s Crash Records Information System."

This is the quote as in the source of data.

## Objectives

Discover meaningful relationship between variables

## Question to be answered/ Problem to be solved

1. Is the dataset valuable?
2. What are the variables related to each other?
3. How are the crash accident distributed across the place?

## Content & Data Description
The scope of data is in the city Austin (county Travis) whose population is above 250000. The person type filed all are "pedal cyclist". The file "Austin Bicycle Crashes 2010-2017 revised subset.csv" will be used in analysis. There are at least 40 variables in the raw dataset, but only subset of it will be used. 

Most of the used data field in the analysis are self-explanatory, here are the description of integer attributes that used in data analysis.

| Data                                   |                                                  Description |
| -------------------------------------- | -----------------------------------------------------------: |
| Crash ID                               |                                                  Primary Key |
| Crash time                             |                                              24h time format |
| Crash Death Count                      |                           discrete number, range between 0,1 |
| Crash Incapacitating  Injury Count     |                          discrete number, range between 0,14 |
| Crash  Non-incapacitating Injury Count |                           discrete number, range between 0,4 |
| Crash Not Injured  Count               |                           discrete number, range between 0,9 |
| Crash Possible Injury  Count           |                           discrete number, range between 0,3 |
| Crash Total Injury  Count              | sum of non-incapacitating injury, incapacitating injury , range between 0,15 |
| Crash Unknown Injury  Count            |                           discrete number, range between 0,4 |
| MercatorX                              |                                     Transform from Longitude |
| MercatorY                              |                                      Transform from Latitude |

## Sources

Texas DOT’s Crash Records Information System

## Reference

 Austin Bicycle - https://data.world/acertz/austin-bicycle-crashes-from-2010-2017/workspace/project-summary?agentid=acertz&datasetid=austin-bicycle-crashes-from-2010-2017

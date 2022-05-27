# Summary of Dataset
## Context
"I’m an avid bike commuter and I recently moved to Austin. I reviewed all the bike-related crashes from Texas DOT’s Crash Records Information System."

This is the quote as in the source of data.

## Content & Data Description
The scope of data is in the city Austin (county Travis) whose population is above 250000. The person type filed all are "pedal cyclist". The file "Austin Bicycle Crashes 2010-2017 revised subset.csv" will be used in analysis.

| Data                                   |                                                  Description |
| -------------------------------------- | -----------------------------------------------------------: |
| Crash time                             |                                              24h time format |
| Crash Death Count                      |                           discrete number, range between 0,1 |
| Crash Incapacitating  Injury Count     |                          discrete number, range between 0,14 |
| Crash  Non-incapacitating Injury Count |                           discrete number, range between 0,4 |
| Crash Not Injured  Count               |                           discrete number, range between 0,9 |
| Crash Possible Injury  Count           |                           discrete number, range between 0,3 |
| Crash Total Injury  Count              | sum of non-incapacitating injury, incapacitating injury , range between 0,15 |
| Crash Unknown Injury  Count            |                           discrete number, range between 0,4 |
|                                        |                                                              |

Excerpt from python notebook

| Crash Death Count | Crash Incapacitating Injury Count | Crash Non-incapacitating Injury Count | Crash Not Injured Count | Crash Possible Injury Count | Crash Total Injury Count | Crash Unknown Injury Count |             |
| ----------------: | --------------------------------: | ------------------------------------: | ----------------------: | --------------------------: | -----------------------: | -------------------------: | ----------- |
|             count |                       2467.000000 |                           2467.000000 |             2467.000000 |                 2467.000000 |              2467.000000 |                2467.000000 | 2467.000000 |
|              mean |                          0.006486 |                              0.191731 |                0.636400 |                    1.208350 |                 0.262262 |                   1.090393 | 0.158897    |
|               std |                          0.080288 |                              1.161059 |                0.564872 |                    0.931757 |                 0.486358 |                   1.208050 | 0.416466    |
|               min |                          0.000000 |                              0.000000 |                0.000000 |                    0.000000 |                 0.000000 |                   0.000000 | 0.000000    |
|               25% |                          0.000000 |                              0.000000 |                0.000000 |                    1.000000 |                 0.000000 |                   1.000000 | 0.000000    |
|               50% |                          0.000000 |                              0.000000 |                1.000000 |                    1.000000 |                 0.000000 |                   1.000000 | 0.000000    |
|               75% |                          0.000000 |                              0.000000 |                1.000000 |                    1.000000 |                 0.000000 |                   1.000000 | 0.000000    |
|               max |                          1.000000 |                             14.000000 |                4.000000 |                    9.000000 |                 5.000000 |                  15.000000 | 4.000000    |

## Sources

Texas DOT’s Crash Records Information System

## Reference

 Austin Bicycle - https://data.world/acertz/austin-bicycle-crashes-from-2010-2017/workspace/project-summary?agentid=acertz&datasetid=austin-bicycle-crashes-from-2010-2017

# iHomie API Server Web App

**Team Members:**

Boning Zhang (bz1189)

Mingjun Tang (mt4145)

Yi Guo (yg2173)

Wanrong Zhu (wz1576)

<br/>

## Project Proposal

### Contents

1.	Overview
2.	Technology Stack	
3.	Endpoints	
4.	Deliverables	
5.	Implementation Plan	

<br/>

### 1. Overview

Our project is defined and designed using the core principles and tools of DevOps (Development Operations). Our web application iHomie is targeted against people who need to find housing information. Our web application should provide users with different interfaces to find all the housing information. Particularly, users are able to look for housing information (in New York City for the time being) based on user-defined criteria and retrieve detailed information. Users can also update and delete housing information. Housing information entails housing names, addresses, descriptions, prices, housing unit type, facilities, and so forth.

<br/>

### 2. Technology Stack

**Front end:**

- React

**Primary Developing Primary Programming Language:**

- Python
- Javascript

**Back end:**

- Flask-RestX

**Devops tools used:**

- Slack
- GitHub
- Jest
- flake8/eslint
- Travis CI
- Docker

<br/>

### 3. Endpoints

**GET:**

- home page (user login page)
- retrieve all housing information
- search for particular housing information
- retrieve all functions
- outsourcing web link transportation 

**POST:**

- add housing information	
- update housing information

**PUT:**

- user sign up

**DELETE:**

- delete housing information

<br/>

### 4. Deliverables

- elementary API server
- project execution automation - Makefile
- unit testers
- project pipelining processes
- docker container

<br/>

### 5. Implementation Plan

**09/15/2020 – 09/18/2020**  Set up Slack channel, GitHub repository and Kanban board

**09/18/2020 – 09/22/2020**  Formulate project proposal

**09/23/2020 – 09/29/2020**  Set up primary Devops tools (including Flask-RestX API)

**09/30/2020 – 10/06/2020**  Implement local makefile for automation processes

**10/07/2020 – 10/20/2020**  Come up with test cases and implement unit testing

**10/21/2020 – 11/03/2020**  Set up project CI/CD pipelining

**11/04/2020 – 11/17/2020**  Create Docker image, deploy project to cloud service and monitoring 

**11/18/2020 – 12/06/2020**  Fine-tuning


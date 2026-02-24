🎓 Admission Management & CRM System (Minimal BRS)
==================================================

📌 Overview
-----------

This project is a simple web-based Admission Management & CRM system designed for educational institutions to manage programs, applicants, seat allocation, admission confirmation, and dashboards while ensuring quota validation and preventing seat overbooking.

The system follows the minimal BRS provided in the assessment and focuses on core admission workflow automation.

🚀 Features
-----------

### ✅ Master Setup

*   Institution creation
    
*   Program creation with intake
    
*   Seat matrix configuration with quota control
    

### ✅ Applicant Management

*   Applicant creation with basic details
    
*   Category and quota mapping
    
*   Document status tracking
    

### ✅ Seat Allocation Engine

*   Real-time quota validation
    
*   Seat allocation blocking when quota full
    
*   Seat counter auto-update
    

### ✅ Admission Confirmation

*   Fee status validation
    
*   Unique admission number generation
    
*   Immutable admission record
    

### ✅ Dashboard APIs

*   Total intake vs admitted
    
*   Quota-wise seat utilization
    
*   Remaining seats
    
*   Pending documents
    
*   Fee pending list
    

🛠 Tech Stack
-------------

*   **Backend:** Flask
    
*   **Database:** MySQL
    
*   **ORM:** SQLAlchemy
    
*   **API Testing:** Postman
    

⚙️ Setup Instructions
---------------------

### 1\. Clone repository

git clone   cd admission-crm   

### 2\. Create virtual environment

python -m venv venv  

Activate:

Windows:

venv\Scripts\activate  

Mac/Linux:

source venv/bin/activate  

### 3\. Install dependencies

pip install -r requirements.txt 

### 4\. Create MySQL database

CREATE DATABASE admission_crm; 

### 5\. Update DB credentials

Edit config.py

### 6\. Run application

 python app.py 

📡 API Endpoints
----------------

### Master

*   POST /institution
    
*   POST /program
    
*   POST /seat
    

### Applicant

*   POST /applicant
    

### Allocation

*   POST /allocate
    

### Fee

*   PUT /fee/
    

### Confirmation

*   PUT /confirm/
    

### Dashboard

*   GET /dashboard
    
*   GET /quota-status
    
*   GET /pending-docs
    
*   GET /pending-fees
    

🔐 System Rules Implemented
---------------------------

*   Quota seats cannot exceed intake
    
*   Allocation blocked when quota full
    
*   Admission number generated once
    
*   Admission confirmed only if fee paid
    
*   Real-time seat counter update
    

🤖 AI Usage Disclosure
----------------------

AI tools were used for guidance in:

*   Initial project structuring
    
*   Boilerplate generation
    
*   Debugging support
    
*   Explanation of design decisions
    

All logic understanding, customization, and integration were performed manually.

👨‍💻 Author
------------

Varun Sharma

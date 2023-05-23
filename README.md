# PLACEMENET MANAGEMENT SYSTEM

> DBMS Project (course work)

### Team

- [Atharva Parkhe](https://github.com/atharvparkhe) - Django (Backend Developer)
- [Medam Greeshma](https://github.com/Greeshma2903/) - HTML, Bootstrap (Frontend Developer)
- [Maheshwari Terse](https://github.com/maheshwari0310) - Django (Backend)

## Motivation
The main objective of the placement management system is to reduce manual work and time. The purpose of this system is to automate the existing manual system with the help of computer software and store the data entered for a longer time with ease of access. 

## Approach
Our solution provides a web-based platform, where students of the college can register once and then get unique dashboards. The system will have different types of accounts for different types of users such as Admin, Student, and placement secretary. Hence this provides different access levels and makes sure the data is in the right hands. 

The system intends to do user-friendly operations which may resolve ambiguity. The project is total management and informative system which provides up-to-date placement information on all the students in the college. The project facilitates a friendly, reliable and fast management system.

## ER Diagram
![ER Diagram](https://github.com/Greeshma2903/placement-management-project/assets/70336930/6c094e12-f203-474e-b805-3becae943e47)

**SCHEMA:**
1. Teacher (id, Name, Email, Phone, Password)
2. Student (id, Name, Email, Phone, Password, Roll No, Bio, Skills, Resume,  Profile Pic, LinkedIn Link, GitHub Link)
3. Company (id,Company Name, Description, Address, Website Link)
4. Job (id, Position, Company, Job Description, Requirements, Pay Rate, Last Date to Apply, Max. Applicants, Currents Applicants Count)
5. JobApplication (id, Job, Applicant, Status)


## Tech Stack
- Frontend: HTML, CSS (Bootstrap)
- Backend: Django
- Database: SQLite

## Screenshots

<details>
  <summary>click here to see</summary>


![login screen](https://github.com/Greeshma2903/placement-management-project/assets/70336930/5363c0d4-aa7f-4916-8985-23200f997ca0)
![companies list](https://github.com/Greeshma2903/placement-management-project/assets/70336930/24ca3e14-135b-4ba1-888f-41d0f1792b99)
![student login](https://github.com/Greeshma2903/placement-management-project/assets/70336930/77f6d1e6-5919-4ed0-9d7f-555769d70281)
![placement officer login](https://github.com/Greeshma2903/placement-management-project/assets/70336930/1d3e12c2-8cc2-4628-9f34-1cadf4537f4d)
![job listing](https://github.com/Greeshma2903/placement-management-project/assets/70336930/e7118236-b5de-420a-af11-339f9273e82c)
![uploading details of students](https://github.com/Greeshma2903/placement-management-project/assets/70336930/6a007295-d4e3-4067-ade9-9d41fed16310)
</details>

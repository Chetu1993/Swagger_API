# Swagger Petstore API Automation Project

This project demonstrates **API automation testing** using the **Swagger Petstore API**.  
It covers **CRUD operations (Create, Read, Update, Delete)** on the `/pet` endpoint along with **negative test scenarios** to validate API error handling and real-world behavior.

---

## 🛠️ Tools & Technologies
- Python
- Requests library
- REST API
- Swagger Petstore API
- Random & UUID-based test data generation

---

## 🌐 API Information

**Base URL**
https://petstore.swagger.io/v2/pet


**Request Headers**
```json
{
  "Content-Type": "application/json"
}

📂 Project Structure
swagger_API/
│
├── swagger_tests.py        # CRUD API automation
├── negative_cases.py      # Negative test scenarios
└── README.md

## 📊 Sample Execution Output

- POST: 200  
- GET: 200  
- PUT: 200  
- DELETE: 200  

- GET non-existent pet status: 404  
- DELETE non-existent pet status: 404  
- POST invalid data status: 200

## ⭐ Key Highlights

- Complete CRUD automation using REST APIs  
- Dynamic test data generation to avoid data conflicts  
- Positive and negative test coverage for robust validation  
- Real-world API behavior handling and observation


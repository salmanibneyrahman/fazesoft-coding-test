# Web Development — Task Management API

A lightweight RESTful API for a Task Management System using an in-memory data store.

## 1. Language and Framework
* **Language:** JavaScript (Node.js)
* **Framework:** Express.js
* **Storage:** In-memory array

## 2. Installation and Running Locally

### Install Dependencies
Navigate to the `Web/` directory and run:
```bash
npm install
```

### Run the Server
Start the local server:
```bash
npm start
```
The server will start listening at `http://localhost:3000`.

## 3. Endpoints

* **POST /api/tasks**
  * Headers: `Content-Type: application/json`
  * Body: `{"title": "Complete assessment", "category": "work"}`
  * Status: `201 Created` with task object, or `400 Bad Request` if validation fails.

* **GET /api/tasks**
  * Optional Query: `?category=work` (or `personal`, `study`)
  * Status: `200 OK` with JSON array of matching tasks (or `[]` if no match).

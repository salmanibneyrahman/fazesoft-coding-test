# FazeSoft Junior Web Developer — Coding Test Solutions

Completed solutions for the FazeSoft Junior Web Developer Assessment.

## Repository Structure

```
fazesoft-coding-test/
│
├── README.md                # Main repository documentation
│
├── DSA/
│   └── solution.py          # Question 1: Jump Game 
│
├── SQL/
│   └── solution.sql         # Question 2: Customer 
│
└── Web/
    ├── package.json         # Project metadata and dependencies
    ├── server.js            # Task Management RESTful API
    └── README.md            # Web API instructions
```

---

##  Question 1 — DSA (Jump Game)
* **File:** `DSA/solution.py`
* **Approach:** Greedy Algorithm tracking the furthest reachable index (`maxReach`).
* **Time Complexity:** O(n)
* **Space Complexity:** O(1) auxiliary space
* **Execution:**
  ```bash
  node DSA/solution.py
  ```

---

## Question 2 — SQL (Customer Spending Analysis)
* **File:** `SQL/solution.sql`
* **Compatibility:** PostgreSQL / MySQL 8.0+
* **Key Highlights:**
  * Filters only completed orders (`status = 'completed'`).
  * Only includes customers who placed at least 2 completed orders (`HAVING COUNT(o.id) >= 2`).
  * Computes total spend (`total_spent`) and completed order count (`order_count`).
  * Uses `DENSE_RANK()` window function partitioned by registration year.
  * Filters top 2 ranked customers per year.
  * Gracefully excludes customers with 0 orders or only non-completed orders.

---

## Question 3 — Web Development (Task Management API)
* **Directory:** `Web/`
* **Technology:** Node.js, Express.js
* **Data Store:** In-memory array
* **Endpoints:**
  * `POST /api/tasks` — Creates a task with title and category validation (`work`, `personal`, `study`). Returns `201 Created` or `400 Bad Request`.
  * `GET /api/tasks` — Retrieves tasks; supports optional category filtering (`?category=work`). Returns `200 OK`.
* **Execution:**
  ```bash
  cd Web
  npm install
  npm start
  ```

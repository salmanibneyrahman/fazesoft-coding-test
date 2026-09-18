const express = require('express');

const app = express();
const PORT = 3000;

app.use(express.json());

// In-memory data store
const tasks = [
    { id: 1, title: "Complete FazeSoft assessment", category: "work", status: "pending" },
    { id: 2, title: "Review SQL query", category: "study", status: "pending" }
];
let nextId = 3;

const ALLOWED_CATEGORIES = ['work', 'personal', 'study'];

// 1. POST /api/tasks — Create a new task
app.post('/api/tasks', (req, res) => {
    const { title, category } = req.body || {};

    // Validate title: required, string, cannot be empty or whitespace
    if (!title || typeof title !== 'string' || title.trim() === '') {
        return res.status(400).json({
            error: "Field 'title' is required and cannot be empty or whitespace."
        });
    }

    // Validate category: required, string, must be one of: 'work', 'personal', 'study'
    if (!category || typeof category !== 'string' || !ALLOWED_CATEGORIES.includes(category.trim().toLowerCase())) {
        return res.status(400).json({
            error: "Field 'category' is required and must be one of: 'work', 'personal', 'study'."
        });
    }

    // Create task with unique id and default status 'pending'
    const newTask = {
        id: nextId++,
        title: title.trim(),
        category: category.trim().toLowerCase(),
        status: 'pending'
    };

    tasks.push(newTask);

    return res.status(201).json(newTask);
});

// 2. GET /api/tasks — Retrieve tasks (with optional query filter)
app.get('/api/tasks', (req, res) => {
    const { category } = req.query;

    if (category) {
        const filteredTasks = tasks.filter(
            (task) => task.category.toLowerCase() === category.trim().toLowerCase()
        );
        return res.status(200).json(filteredTasks);
    }

    return res.status(200).json(tasks);
});

app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
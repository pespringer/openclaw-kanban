const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
const { Pool } = require('pg');

const app = express();
const port = 5000;

// Middleware
app.use(bodyParser.json());
app.use(cors());

// Database connection
const pool = new Pool({
  user: 'postgres',
  host: 'localhost',
  database: 'kanban',
  password: 'yourpassword',
  port: 5432,
});

// API Routes
app.get('/', (req, res) => {
  res.send('Hello from the Kanban backend!');
});

app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}/`);
});
const express = require('express');

const app = express();

// Route for /
app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

// Start server
app.listen(1245);

module.exports = app;

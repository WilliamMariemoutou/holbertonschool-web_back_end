const express = require('express');
const fs = require('fs');

const app = express();
const database = process.argv[2];

// Route: /
app.get('/', (req, res) => {
  res.type('text');
  res.send('Hello Holberton School!');
});

// Route: /students
app.get('/students', (req, res) => {
  res.type('text');
  res.write('This is the list of our students\n');

  fs.readFile(database, 'utf-8', (err, data) => {
    if (err) {
      res.end('Cannot load the database');
      return;
    }

    const lines = data.split('\n').filter((line) => line.trim() !== '');
    const students = lines.slice(1);

    res.write(`Number of students: ${students.length}\n`);

    const fields = {};

    students.forEach((student) => {
      const studentData = student.split(',');
      const firstName = studentData[0];
      const field = studentData[3];

      if (!fields[field]) {
        fields[field] = [];
      }

      fields[field].push(firstName);
    });

    for (const field in fields) {
      if (Object.prototype.hasOwnProperty.call(fields, field)) {
        const names = fields[field];
        res.write(`Number of students in ${field}: ${names.length}. List: ${names.join(', ')}\n`);
      }
    }

    res.end();
  });
});

// Start server
app.listen(1245);

module.exports = app;

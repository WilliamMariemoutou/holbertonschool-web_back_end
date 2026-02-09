const fs = require('fs');

function countStudents(path) {
  let data;

  // Try to read the file
  try {
    data = fs.readFileSync(path, 'utf-8');
  } catch (error) {
    throw new Error('Cannot load the database');
  }

  // Split file into lines and remove empty lines
  const lines = data.split('\n').filter((line) => line.trim() !== '');

  // Remove the header line
  const students = lines.slice(1);

  console.log(`Number of students: ${students.length}`);

  const fields = {};

  // Group students by field
  students.forEach((student) => {
    const studentData = student.split(',');
    const firstName = studentData[0];
    const field = studentData[3];

    if (!fields[field]) {
      fields[field] = [];
    }

    fields[field].push(firstName);
  });

  // Print number of students per field
  for (const field in fields) {
    if (Object.prototype.hasOwnProperty.call(fields, field)) {
      const names = fields[field];
      console.log(
        `Number of students in ${field}: ${names.length}. List: ${names.join(', ')}`,
      );
    }
  }
}

module.exports = countStudents;

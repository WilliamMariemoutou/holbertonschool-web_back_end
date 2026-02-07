const http = require('http');

const app = http.createServer((req, res) => {
  // Set status code and content type
  res.writeHead(200, { 'Content-Type': 'text/plain' });
  // Write the response body
  res.end('Hello Holberton School!');
});

// Listen on port 1245
app.listen(1245);

module.exports = app;

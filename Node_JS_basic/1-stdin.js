console.log('Welcome to Holberton School, what is your name?');

process.stdin.setEncoding('utf-8');

process.stdin.on('data', (input) => {
  console.log(`Your name is: ${input.trim()}`);
});

process.stdin.on('end', () => {
  console.log('This important software is now closing');
});

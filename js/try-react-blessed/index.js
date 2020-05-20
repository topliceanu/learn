require('@babel/register')({
  presets: [
    ["@babel/preset-env"],
    ["@babel/preset-react"]
  ]
});
const argv = process.argv.slice(2);
const example = argv[0];
const examples = [
  'demo',
  'dashboard',
];

if (examples.indexOf(example) === -1) {
  console.warn(
    'Invalid example "%s" provided. Must be one of:\n  *',
    example,
    examples.join('\n  * ')
  );
  process.exit(0);
}

require('./examples/' + example);

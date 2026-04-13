const path = require('path');

module.exports = {
  darkMode: 'media',
  content: [
    path.resolve(__dirname, '..', '..', 'templates/**/*.html'),
  ],
};

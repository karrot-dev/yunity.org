var sanitizeHtml = require('sanitize-html');
var toMarkdown = require('to-markdown');
var fs = require('fs');
var args = process.argv.slice(2);
var dirty = fs.readFileSync(args[0]);
var clean = sanitizeHtml(dirty, {
  allowedTags: [
    'p', 'img', 'em', 'a', 'blockquote',
    'h1', 'h2', 'h3', 'h4', 'h5', 'h6',
    'hr',
    'ul', 'ol', 'li'
  ],
  allowedAttributes: {
    'a': ['href'],
    'img': ['src', 'title']
  }
});

var markdown = toMarkdown(clean, {
  gfm: true,
  converters: [
    {
      filter: ['h1', 'h2', 'h3', 'h4', 'h5', 'h6'],

      replacement: function(innerHTML, node) {
        var hLevel = parseInt(node.tagName.charAt(1), 10) + 1;
        var hPrefix = '';
        for(var i = 0; i < hLevel; i++) {
          hPrefix += '#';
        }
        return '\n' + hPrefix + ' ' + innerHTML + '\n\n';
      }
    }

  ]
});

console.log(markdown);

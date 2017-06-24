---
title: Heartbeat
blog_url: heartbeat
metadata:
    'og:site_name': yunity
    'og:title': Heartbeat
    'og:type': website
    'og:url': 'https://yunity.org/en/heartbeat'
    'og:image': 'https://yunity.org/user/themes/twentyfifteen/images/yunity-orange.svg'
    'og:description': 'The biweekly summary of what happens inside the yunity network'
menu: Heartbeat
menu_description: The heartbeat is a biweekly summary of what happens in yunity
routes:
  aliases:
    - '/blog'

sitemap:
    changefreq: weekly

content:
    items: @self.children
    order:
        by: date
        dir: desc
    limit: 10
    pagination: true

feed:
    description: yunity heartbeat
    limit: 10

pagination: true
---

# Our Blog

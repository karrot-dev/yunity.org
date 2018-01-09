---
title: Heartbeat
blog_url: heartbeat
metadata:
    description: 'The fortnightly summary of what happens inside the yunity network'
menu: Heartbeat
menu_description: The heartbeat is a fortnightly summary of what happens in yunity
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

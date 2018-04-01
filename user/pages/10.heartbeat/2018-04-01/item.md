---
title: "yunity heartbeat 2018-03-18"
date: "2018-03-18"
continue_link: true
taxonomy:
    category: blog
    tag: [heartbeat]
published: true
---

**The yunity heartbeat** - news from the world of sharing, fresh every two weeks.

## [Kanthaus](https://kanthaus.online)

## [Karrot](https://karrot.world)

## [Foodsaving Worldwide](https://foodsaving,world)

## [Foodsharing.de](https://foodsharing.de)

For a long time we had been thinking how to handle the refactoring of the frontend JavaScript, and it's a kinda big topic, so was easy to delay. However, I finally got
my head around it and pushed forward with a webpack-based setup.

We deployed the first webpack'd pages (the logged out homepage, and the logged in dashboard page), and not too many errors arrived! Seems to work :) It'll still be a lot of work to roll out the new style to the rest of the site though. Wanna help?

Matthias did an amazing job switching over to using [Symfony Forms](https://symfony.com/doc/current/forms.html) (on just one form for now). In general we are trying to use standardised library components instead of custom implementations and form handling is one of the big topics for web applications.

With the new approach we get much improved validation and error handling and remove a lot of the existing code once the transition is complete (again, wanna help?).

_by Nick_

## About the heartbeat.
The heartbeat is a fortnightly summary of what happens in yunity. It is meant to give an overview over our currents actions and topics.

### How to contribute?
Talk to us in [#heartbeat](https://yunity.slack.com/messages/heartbeat/) on [Slack](https://slackin.yunity.org) if you want to add content, change the layout or any other heartbeat related issues and ideas! We are also happy about any kind of feedback! ^_^

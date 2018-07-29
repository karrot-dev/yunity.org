---
title: "yunity heartbeat 2018-07-29"
date: "2018-07-29"
continue_link: true
taxonomy:
    category: blog
    tag: [heartbeat]
published: true
---

**The yunity heartbeat** - news from the world of sharing, fresh every two weeks.

## [foodsharing.de](https://foodsharing.de)-dev


## [Kanthaus](https://kanthaus.online)


## [Karrot](https://karrot.world)

The Summer of Karrot continues! Our group of four spent most of their time at Kanthaus discussing and coding features for Karrot. The group application frontend gets into shape (find out more in this [forum post](https://community.foodsaving.world/t/new-group-application-feature-coming-up/92)), the [new proposed user levels](https://community.foodsaving.world/t/new-user-levels-proposed-for-karrot-newcomers-and-editors/95) were discussed a lot and we updated the [Karrot roadmap](https://github.com/yunity/karrot-frontend/blob/master/ROADMAP.md) in a concise meeting.

Nick and Tilmann implemented replies to wall messages (also known as conversation threads). You can already try them out on https://dev.karrot.world. To reduce the number of unwanted emails, we had discussions about better notification settings, but didn't come to a final conclusion yet. We did implement merged notification emails though: if messages are being sent in quick succession, then only send one email containing all messages. Also, we don't send emails anymore if the message was already marked as seen.

Some smaller features landed too: a button to show directions between user and store has been added, external links in Markdown text are marked now, internal links open in the same window and new posts from our [community forum](https://community.foodsaving.world/) get highlighted in the topbar.

![](karrot-notifications.png)
_Stay updated about new posts in our community forum_

![](karrot-markdown-links.png)
_Recognize the link type in Markdown_

And now the most important bit: improvements to the Karrot developer experience! After some days of fiddling, Nick managed to build our frontend with webpack 4 and babel 7. He also upgraded our backend to shiny new [Django Channels 2](https://github.com/django/channels), which uses async Python to handle websocket communication. And we use [yapf](https://github.com/google/yapf) now to nicely format out backend code!

_by Tilmann_

## [Foodsaving Worldwide](https://foodsaving.world)


## [Auerworld Festival](http)

## About the heartbeat.
The heartbeat is a fortnightly summary of what happens in yunity. It is meant to give an overview over our currents actions and topics.

### How to contribute?
Talk to us in [#heartbeat](https://yunity.slack.com/messages/heartbeat/) on [Slack](https://slackin.yunity.org) if you want to add content, change the layout or any other heartbeat related issues and ideas! We are also happy about any kind of feedback! ^\_^

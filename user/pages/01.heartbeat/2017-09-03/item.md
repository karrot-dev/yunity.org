---
title: "yunity heartbeat 2017-09-03"
date: "2017-09-03"
continue_link: true
taxonomy:
    category: blog
    tag: [heartbeat]
---

**The yunity heartbeat** - news from the world of sharing, fresh every two weeks.

## [foodsaving.world](https://foodsaving.world)

### Rails Girls Success

https://blog.foodsaving.world/2017/09/01/railsgirls-fairy-tale.html

### Latest development activity

Since the last changelog in [Heartbeat 2017-08-06](2017-08-06), a lot of things happened! I'm going to highlight relevant discussions and changes.

#### Discussions

- Kristijan clarified that the ["terms before you can join a group"](https://github.com/yunity/foodsaving-frontend/issues/324) should be marked explicitly as user-provided, see also the discussion in ["minimal admin roles"](https://github.com/yunity/foodsaving-backend/issues/350)
- Nick and Tilmann are working hard to [evaluate frontend framework candidates](https://github.com/yunity/foodsaving-frontend/issues/593). So far, they looked at Angular4, React and Vue.JS. The latter is the current favourite, pending a more formal evalution and consensus among the development team. It also became clear that a library of pre-made UI components is the most critical piece of software for us, as we are lacking designers.
- We came to the conclusion that we need to create a proper [project info website](https://github.com/yunity/foodsaving-frontend/issues/601) that should be visible on foodsaving.world. Nick already finished the initial setup, now it needs to be decided what content we want to have on it.
- As part of the previous point, we considered renaming the foodsaving tool to a more abstract name, like _karrott_ (inspired by the logo)
- Kristijan proposed an [out-of-the-box solution to handle newcomers](https://github.com/yunity/foodsaving-frontend/issues/546#issuecomment-326497599) while the feature is not yet implemented
- Kristijan published his thoughts on [a legal entity for foodsaving.world](https://github.com/yunity/foodsaving-frontend/issues/606) and a [data privacy statement](https://github.com/yunity/foodsaving-frontend/issues/607), partly inspired by the struggles that foodsharing.de has nowadays
- The discussion on [store teams](https://github.com/yunity/foodsaving-frontend/issues/360) was fueled by a comment from Stefan who wished to manage his foodsavers with one group per store. Much of the conversation can be found in the #foodsaving-tool Slack channel.


#### Coding progress

- New: Ines and Marie implemented [user feedback for pick-ups](https://github.com/yunity/foodsaving-backend/pull/342)
- Changed: Finished pick-up dates [are now kept in the database](https://github.com/yunity/foodsaving-backend/pull/344) to make feedback possible (Tilmann)
- Changed: Pick-up series modifications [don't modify a dependent pick-up if a user has joined it](https://github.com/yunity/foodsaving-backend/pull/346) (Tilmann)
- New: [Push notification infrastructure](https://github.com/yunity/foodsaving-backend/pull/356), using Google FCM
- @azzang, a new contributor, created a [common front-end service to determine the screen size](https://github.com/yunity/foodsaving-frontend/pull/599)
- Nick is looking for solutions on how to implement [a rules and permissions system](https://github.com/yunity/foodsaving-backend/issues/353) in Django.
- Back-end refactoring and code cleanup, code coverage now reaches 99%! 
- On Kristijan's request, Nick provided a graphic schema overview of the foodsaving tool database:
![](https://user-images.githubusercontent.com/31616/29941736-7018ec8c-8e8b-11e7-943c-09ff1448b7a4.png)
- New: [Conversations](https://github.com/yunity/foodsaving-backend/pull/333) backend, including [significant changes to the deployment](https://github.com/yunity/foodsaving-backend/pull/340)
- In progress: [User interface for conversations](https://github.com/yunity/foodsaving-frontend/pull/597)
![](https://user-images.githubusercontent.com/16825880/29294325-2b659872-814f-11e7-8f9d-f4f65aacf7dd.png)

_by Tilmann_

## Wurzen


---

## About the heartbeat.

The heartbeat is a biweekly summary of what happens in yunity. It is meant to give an overview over our currents actions and topics.

### When and how does it happen?

Every other weekend we collect information on a wiki page and publish it on Sunday or the following Monday as a wiki blog article.

Afterwards we add a nice abstract and share it on [facebook](https://www.facebook.com/yunity.org/).

### How to contribute?

Talk to us in [#heartbeat](https://yunity.slack.com/messages/heartbeat/) on [Slack](https://slackin.yunity.org) about the content, the layout or any other heartbeat related issues and ideas!

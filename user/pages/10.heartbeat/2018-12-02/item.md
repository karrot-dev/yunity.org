---
title: "yunity heartbeat 2018-12-02"
date: "2018-12-02"
continue_link: true
taxonomy:
    category: blog
    tag: [heartbeat]
published: true
---

**The yunity heartbeat** - news from the world of sharing, fresh every two weeks.

## [Karrot](https://karrot.world)

[New Karrot release](https://github.com/yunity/karrot-frontend/blob/master/CHANGELOG.md#627---2018-11-28) with improvements for Android app, it should have less problems going to the right page when the user taps on push notifications. The way how it refreshes data has been slightly improved and should cause less failures.

Tilmann and Janina [discussed changes to recurring pickups](https://community.foodsaving.world/t/better-change-handling-for-recurring-pickups/174) in the community forum. The current implementation has problems with more advanced use cases, for example moving pickups around that are part of a series. We're looking for ways to change that without breaking other use cases. Tricky business!

Nick [enabled a stricter Content Security Policy](https://github.com/yunity/yuca/pull/16) for dev.karrot.world. It tries to make sure that no unexpected code is being executed in the browser and no data from insecure connections are being loaded, for example images from non-https connections that users embedded in their custom descriptions. We'll continue to test this on our development site and eventually deploy it to karrot.world too.

Bruno [reported from the Bike Kitchen trial](https://community.foodsaving.world/t/test-karrot-for-bike-kitchen/120/10) with positive feedback and feature suggestions. A store wall and store subscriptions would be especially helpful for them.

What's up next?
There might be more Karrot coding activity in the next weeks. We are also looking forward to holding a talk about Karrot and related topics at the end of December at [35C3](https://events.ccc.de/2018/09/11/35c3-call-for-participation-and-submission-guidelines/), an international congress held at Leipzig. Finally, there will be a _Winter of Karrot_ at Kanthaus in January - stay tuned!

_by Tilmann_

## [Harzgerode / Haus X](http://freiefeldlage.de/)

## [Kanthaus](https://kanthaus.online)

## [Foodsaving Worldwide](https://foodsaving.world)

## [foodsharing.de](https://foodsharing.de)-dev

## About the heartbeat.
The heartbeat is a fortnightly summary of what happens in yunity. It is meant to give an overview over our currents actions and topics.

### How to contribute?
Talk to us in [#heartbeat](https://yunity.slack.com/messages/heartbeat/) on [Slack](https://slackin.yunity.org) if you want to add content, change the layout or any other heartbeat related issues and ideas! We are also happy about any kind of feedback! ^\_^

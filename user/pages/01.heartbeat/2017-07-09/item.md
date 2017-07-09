---
title: "yunity heartbeat 2017-07-09"
date: "2017-07-09"
continue_link: true
taxonomy:
    category: blog
    tag: [heartbeat]
---

**The yunity heartbeat** - news from the world of sharing, fresh every two weeks.

## [Berlin Hackathon plannings](https://yunity.org/en/events/2017-06-14-hackathon)

As announced in the [last heartbeat](../2017-06-25), our hackathon will take place next weekend. According to the attendance sheet, we are expecting

- 3 devs to work on [foodsharing.de](https://foodsharing.de) and the new [_foodsharing light_](https://github.com/foodsharing-dev/foodsharing-light) code
- 4 devs to work on [foodsaving.world](https://foodsaving.world) code
- 4 devs to work on [trustroots.org](http://trustroots.org) code.

Additionally, there will be people who are interested in having a look at the projects or will support the hackathon with food deliveries and cooking. Speaking of food: we will pick up food from lots of [foodsharing.de](https://foodsharing.de) cooperations in Berlin and made an agreement with [Wilmersburger](https://www.wilmersburger.de), who will send us a packet of vegan cheese.

For further promotion of the foodsaving tool at the hackathon, Laurina converted the logo into a stencil. Now we can print on shirts and other surfaces :)

![](0.fsworld_stencil.jpg?resize=400,400)

We are looking forward to meeting you in the evening of July 14th!

## [foodsharing.de](https://foodsharing.de)

Next steps towards converting foodsharing.de PHP backend code into the Laravel framework have been done by Raphael W. He created a new Laravel project to try out a possible code structure. After feedback from Nick he plans to use the gained knowledge to integrate those ideas into the main foodsharing.de repository. It is unclear yet how Laravel's _Eloquent_ ORM will relate to the recently introduced [foodsharing-api](https://github.com/foodsharing-dev/foodsharing-api), which uses the _Doctrine_ ORM. 

## [foodsaving.today](https://foodsaving.today)

We got a new article about [Foodsharing Bilbao](https://foodsaving.today/en/blog/2017/06/30/foodsharing-bilbao-the-beginning) on foodsaving.today, written by Unai, one of the founders.

> We have weekly foodshare events at Karmela and Bilbiko Kultur Etxea. We have contacted big supermarkets such as Lidl and ALDI. We are going to present Foodsharing Bilbao and prepare food in an event organised by the Space Exchange Network and at a neighbourhood assembly. We have been invited to organise a Disco Soup in Sarean that might take place soon or after this summer. We will be live on air soon in a local radio station. We are active!

## [foodsaving.world](https://foodsaving.world)

![](fsworld_logo.png?resize=200,200)

There have been a lot of discussions in the last two weeks revolving around the next steps of the foodsaving tool. Nick, Tilmann, Lars and Janina had [a pad-discussion](https://yunity.atlassian.net/wiki/display/FSINT/2017-06-30+Planning+meeting), followed by a call with Ines and Marie. We decided to prioritize a list of features for the [RGSoC internship](https://railsgirlssummerofcode.org/), including feedback for finished pickups and roles for rights distribution.

In a later meeting, the [roadmap](https://github.com/yunity/foodsaving-frontend/blob/master/ROADMAP.md) was restructured and updated. We categorized the issues into _current development_, _current discussion_ (higher and lower priority) and _ideas / brainstorming_.

- Pick-up dates can hold additional information text, so do series ([details](https://github.com/yunity/foodsaving-frontend/pull/549))
![](fstool-commentfield.png)
- Explicit history message if a pick-up was missed. Showed up as _done_ before ([details](https://github.com/yunity/foodsaving-frontend/pull/540))
- The "text you see before joining the group" a.k.a `public_description` does now support formatting with markdown
- The time zone setting of the group shows suggestions for valid names
- Design fixes for the group pop-up and the toolbars ([details](https://github.com/yunity/foodsaving-frontend/pull/533))
- History API got a parameter to filter by date ([details](https://github.com/yunity/foodsaving-backend/commit/562919221c95be8ccc6fcb335dc22b79f769b254))
- Backend supports sending notifications for upcoming pickups to a Slack channel (webhook-based)
- The development infrastructure was extended with end-to-end tests, that means we can verify successful interaction between frontend and backend in an automated manner.
- `npm` has problems with the newly introduced `package-lock.json`, so we decided to remove it for the time being

## WuppHaus Wurzen

After some doubts regarding specific phrasings in the contract could be cleared, the two houses in Wurzen are finally being bought! The first yuniteers will go there next week already and after the hackathon work on the houses will really start! 

## Harzgerode

A lot of things are happening in Harzgerode: A plant-based sewage plant is in the process of being built, so is the outdoor kitchen, that will be used for the [und jetzt?! conference](http://www.undjetzt-konferenz.de/). Since there is so much work to do an [invitation to a work camp](https://www.youtube.com/watch?v=UTtHYLnnLxs) was issued and everybody is welcome to join the team!
Also, Harzgerode still is the place to be to meet with yunity people and many come by for some days to enjoy the group spirit.

---

## About the heartbeat.

The heartbeat is a biweekly summary of what happens in yunity. It is meant to give an overview over our currents actions and topics.

### When and how does it happen?

Every other weekend we collect information on a wiki page and publish it on Sunday or the following Monday as a wiki blog article.

Afterwards we add a nice abstract and share it on [facebook](https://www.facebook.com/yunity.org/).

### How to contribute?

Talk to us in [#heartbeat](https://yunity.slack.com/messages/heartbeat/) on [Slack](https://slackin.yunity.org) about the content, the layout or any other heartbeat related issues and ideas!

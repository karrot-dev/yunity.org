---
title: "yunity heartbeat 2018-07-15"
date: "2018-07-15"
continue_link: true
taxonomy:
    category: blog
    tag: [heartbeat]
published: true
---

**The yunity heartbeat** - news from the world of sharing, fresh every two weeks.

## [foodsharing.de](https://foodsharing.de)-dev

We finished our hackweek with some really great outcomes:
1. All JavaScript moved into es6/webpack environment - thanks to Matthias
1. The first [VueJS](https://vuejs.org/) component (using [BootstrapVue](https://bootstrap-vue.js.org/) for UI components) - thanks to Chandi
1. The first RESTful API endpoint - thanks to Theo
1. One of the large classes in the Model hierarchy refactored into more logical places - thanks to Tilmann
1. Emoji reactions added to forum posts - thanks to Matthias

It wasn't quite possible to get all this working in beta by the end of the week - and then Matthias left for a well-earned break. He has returned again now though and energised to fix all the bugs again! Phew!

So after fixing the bugs in beta, we're aiming for a production deployment next week (before Matthias leaves again).

We were enthusiastic to start planning the next hackweek (maybe as far away as January 2019 though...).

We had another great milestone though, whilst Matthias was away we had the need to change the penis picture on the homepage, and we managed a very collaborative deployment to production: Michi made the changes, Chandi fixed the git branch target, Tilmann approved the changes, and I fixed a secondary error. All without Matthias!

![](pica_foodporn.png)
_The controversial homepage picture_

_by Nick_

## [Kanthaus](https://kanthaus.online)

![](bodhis-bum.jpg)
_Bodhi slides along the wet slidey thing_

## [Karrot](https://karrot.world)

@taistadam and @djahnie started their *Summer of Karrot* to learn programming whilst contributing to karrot. @nicksellen and @alangecker are teaching the basics of JavaScript, Vue.JS and Git, guiding them step by step towards being independent contributors.

@tiltec summarized the need for user trust levels in a [Github issue](https://github.com/yunity/karrot-frontend/issues/1062) and the first outcome was to (finally) implement a process where users can apply for becoming a group member. At the initiative of @nicksellen we held a _wireframing session_ that gave us [enough input](https://github.com/yunity/karrot-frontend/issues/894#issuecomment-404173085) to start implementing.

![](karrot-wireframes-bright.jpg)
_Contrived picture of the wireframing session_

Besides that, @nicksellen is looking into improving navigation user experience in karrot. The work is still in a very experimental phase, but big changes in the mid-term future aren't unlikely.

![](https://user-images.githubusercontent.com/31616/41812190-7f311414-7716-11e8-8263-3d6e6dedd107.png)
_Playing with the karrot navigation UI_

@tiltec added proper statistics to the store page, based on pickup feedback given by users. The calculation method is currently quite simple, to keep the numbers predictable. However, there's a discussion going on in our new [Community forum](https://community.foodsaving.world/t/statistics-about-the-amount-of-saved-food/85) about ideas for better statistics calculation.

![](karrot-statistics.png)
_Store statistics view on the feedback page_

As a last note, markdown formatting is now possible in feedback comments!

_by Tilmann_

## [Foodsaving Worldwide](https://foodsaving.world)

Currently the last steps are being take to replace our info page with a new one. For visitors of the site the difference will be small, but for people adding or changing content it will be huge and awesome! That means that this could very well lead to more frequent updates and generally more maintenance.

The overall structure is already starting to change and in the future [foodsaving.world](https://foodsaving.world) should be a very lean, concise page that only gives an overview; all the template texts and guides from [yunity's confluence wiki]() is to be transferred into our new [community forum](https://community.foodsaving.world) and directly sorted by language.

That's right, we have language-specific sub-forums and we'd love you to use them for your foodsaving group's topics!

_by Janina_

## [Ukuvota](https://gitlab.com/yunity/ukuvota)

The past weeks were consumed by getting used to F# and figuring out how things work with the fable - the compiler that turns F# into Js.

Ukuvota has a new navigation bar and can now parse markdown files! The next task is to create the interface for a Group view and possibly add some input fields.

![](ukuvota-progress.png)

_by Wolfi_

## About the heartbeat.
The heartbeat is a fortnightly summary of what happens in yunity. It is meant to give an overview over our currents actions and topics.

### How to contribute?
Talk to us in [#heartbeat](https://yunity.slack.com/messages/heartbeat/) on [Slack](https://slackin.yunity.org) if you want to add content, change the layout or any other heartbeat related issues and ideas! We are also happy about any kind of feedback! ^\_^

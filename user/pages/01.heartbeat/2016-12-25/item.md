---
title: "yunity heartbeat 2016-12-25"
date: "2016-12-25"
continue_link: true
taxonomy:
    category: blog
    tag: [heartbeat]
published: true
---

The yunity heartbeat - what has each team done, what are they doing and what do they need help with.

* * *

### WuppHouse Bad Dürrenberg.

So much is happening in Badue, as always! See this bullet-point list for details:

Building and repairing:

*   getting rid of even more rubble and dirt.
*   breaking down the rotten material in between the beams.
*   improving insulation by closing holes in the floors.
*   reorganizing the rooms.
*   fixing some windows.

Community and networking:

*   holding a reflection circle together with locals
*   having conversations with locals coming by
*   teaching English
*   holding contact with local newspapers (next article in the coming days)

Organization:

*   setting up a new tool for organizing and contacting people
*   contacting rocket.chat, and now waiting to get an instance for Badue

Recently a lot of yuniteers started to find a passion for video making and editing and began documenting the exciting WuppHaus project and the lifestyles behind it. After the launch of [Selina Camile](https://yunity.atlassian.net/wiki/display/~Selina) and [Lara Earthling](https://yunity.atlassian.net/wiki/display/~rose+earthling) 's channel [Gedankengänge und Gefühlswelten](https://www.youtube.com/channel/UCxLKmSQALimZhePtY9NVtFw) , and [Philip Engelbutzeder](https://yunity.atlassian.net/wiki/display/~Philip) 's videos about [active locals](https://www.youtube.com/watch?v=hEObasAKIe4) and [teatime in the WuppHaus](https://www.youtube.com/watch?v=xkpVFhjP_Qg) , now [Paul Free](https://yunity.atlassian.net/wiki/display/~Paul+Free) also started experimenting with film and created a montage of existing as well as new material, music, interviews and pictures. You will see that it is the outcome of a learning process, but if you are interested in the project and the people, you will enjoy it anyways... ![](/user/themes/twentyfifteen/images/emoticons/wink.png)

* * *

![](2016-12-25/image2016-12-25_19-24-11.png)

### Foodsaving Tool.

Code: [https://github.com/yunity/foodsaving-frontend](https://github.com/yunity/foodsaving-frontend)

Try it out: [http://fstool.yunity.org/](http://fstool.yunity.org/)

![](2016-12-25/image2016-12-25_19-15-24.png)

![](2016-12-25/image2016-12-25_19-18-22.png)

#### Done

*   [Release 1](https://github.com/yunity/foodsaving-frontend/pull/225) , including a [list of features](https://github.com/yunity/foodsaving-frontend/blob/master/CHANGELOG.md)
*   [First draft of the roadmap](https://github.com/yunity/foodsaving-frontend/blob/5e12632bc57cfc7eb8d9e4e2fc802533cf8ee6e9/ROADMAP.md) , a rough plan of coming features
*   [New logo!](https://github.com/yunity/foodsaving-frontend/pull/222)
*   Formatting using [Markdown](https://en.wikipedia.org/wiki/Markdown) for descriptions of group, store and user page ( [implementation #1](https://github.com/yunity/foodsaving-frontend/pull/203) , [#2](https://github.com/yunity/foodsaving-frontend/pull/207) , [#3](https://github.com/yunity/foodsaving-frontend/pull/235) )
*   [Link to your user profile page in topbar](https://github.com/yunity/foodsaving-frontend/pull/232) , with a side navigation bar for mobile users
*   Pickups are now [deletable](https://github.com/yunity/foodsaving-frontend/pull/219) , which requires [confirmation of the user](https://github.com/yunity/foodsaving-frontend/pull/240)
*   Statistics about user signups ( [implementation](https://github.com/yunity/foodsaving-backend/pull/225) ), can be accessed via [Grafana](https://grafana.yunity.org/dashboard/db/user-statistics) for members of the yunity GitHub organization

#### In Progress

Pursuing Release 2:

*   Password protection for groups ( [backend task](https://github.com/yunity/foodsaving-backend/pull/226) , [overview task](https://github.com/yunity/foodsaving-frontend/issues/212) )
*   E-Mail verification and password recovery ( [backend task](https://github.com/yunity/foodsaving-backend/pull/208) , [overview task](https://github.com/yunity/foodsaving-frontend/issues/239) )
*   and [much more...](https://github.com/yunity/foodsaving-frontend/milestone/6)

#### Challenges/help needed

*   Some users don't see their preferred language, even though it's translated. Who can [figure out why](https://github.com/yunity/foodsaving-frontend/issues/238) ?
*   Improving the navigation adding "breadcrumbs", setting the window title depending on the page content and adding explicit URLs to link to page content. This is a quite big task ( [#1](https://github.com/yunity/foodsaving-frontend/pull/242) , [#2](https://github.com/yunity/foodsaving-frontend/pull/237) ) and needs some refinement before it can go online.

* * *

### [Foodsharing.de](http://Foodsharing.de) Development.

#### In Progress

Raphael Wintrich is in the final round of the [https://prototypefund.de/projects/](https://prototypefund.de/projects/) which means that he will hopefully continue putting some effort in the [foodsharing.de](http://foodsharing.de) development over the next 6 months.

#### Challenges/help needed

The following topics are currently our focus:

*   Exchanging the current module routing with HTTPKernel/HTTPRouter from [Symfony Components](http://symfony.com/components) - or better directly use [Silex](http://silex.sensiolabs.org/) ? We don't have any experienced experts in those fields and welcome any help on architectural- and tooling decisions.
*   Integrating a basic data mapper ORM. [Doctrine](http://www.doctrine-project.org/) is the current suggestion, but as well we might consider alternatives if there are reasons. Main reason for chosing an ORM is reducing code footprint, gaining query performance, fundamentally easier test data generation as well as free migrations.
*   Writing integration tests - in the last deployments in October 2016, we fucked up some existing features as well as introduced bugs with new features. The goal is to get all new as well as recently introduced features and bugs tested. Currently, integration tests on different levels (Selenium/chromium for anything involving javascript, PHP-Browser for everything involving HTML selectors, API tests for simple HTML and json responses) are the best way as we still don't have unit-testable modules. [Codeception](http://codeception.com/) integrates very well so far.

The reason why I put all of this under "help needed" is because I feel that since I, [Matthias Larisch](https://yunity.atlassian.net/wiki/display/~matthias) , am focusing on the WuppHaus now and thus currently not contributing code myself, nothing happens on these goals and I would really appreciate more contributions on that level, e.g. more than introducing new, untested, simple features ![](/user/themes/twentyfifteen/images/emoticons/smile.png)

* * *

### Future WuppDays.

#### In Progress

*   planning of another hackathon, this time in Barcelona and/or Valencia, for the time around end of January to mid-February 2017
*   planning of WuppDays XXL in Berlin in late April 2017. [Philip Engelbutzeder](https://yunity.atlassian.net/wiki/display/~Philip) is already in contact with someone offering a great location for lots of people to come by over the course of three weeks. Stay tuned for more specifics or join us in the planning in [#wuppdays_xxl_berlin](https://yunity.slack.com/messages/wuppdays_xxl_berlin/) on Slack!.

* * *

### IT-Service.

#### Done

*   Registered [wupphaus.de](http://wupphaus.de) as a better, separated communication channel for our WuppHaus network.

#### In Progress

*   Trying onlyoffice CRM to better manage communication and contact handling - actively used for WuppHaus-related communication.
*   Researching and documenting open source software alternatives for collective work. [Paul Free](https://yunity.atlassian.net/wiki/display/~Paul+Free)

* * *

### Translation.

#### Done

*   Lots of new subtitles have been added to our videos on Youtube:
    *   Italian, French and Spanish for the [Drawing Story](https://www.youtube.com/watch?v=BPwyHEsIAMc)
    *   Improved English ones for the [Hackathon Presentation](https://www.youtube.com/watch?v=MLWccmvhIlU)
    *   Spanish ones for [Kirchheim started](https://www.youtube.com/watch?v=xU7eDQIs19Y)

#### In Progress

*   Translation of [wupphaus.yunity.org](https://wupphaus.yunity.org/) via [Zanata](https://translate.zanata.org/project/view/wupphaus?dswid=877) by [Paul Free](https://yunity.atlassian.net/wiki/display/~Paul+Free) and [Janina Abels](https://yunity.atlassian.net/wiki/display/~Janina) .

#### Challenges/help needed

Who added all these subs? We know that [Sara Brunacci](https://yunity.atlassian.net/wiki/display/~brunaccisara) made the Italian ones, but the others are still mysterious... Thank you, anonymous Youtube user, for gifting subtitles to us! ![](/user/themes/twentyfifteen/images/emoticons/heart.png) If you were to give us subs in any language for all the [ new videos about the WuppHaus ](https://www.youtube.com/playlist?list=PLFQufeToSVxsoK8m4Tj4i82WjSrmn2dtA) , we'd be forever grateful! ![](/user/themes/twentyfifteen/images/emoticons/wink.png)

* * *

### Culture.

#### Done

*   A beautiful new poem in German by [Philip Engelbutzeder](https://yunity.atlassian.net/wiki/display/~Philip) was added to [yunity Poems](https://yunity.atlassian.net/wiki/display/YUCU/yunity+Poems) .
*   Launch of the [yunity book club](https://yunity.atlassian.net/wiki/display/YUCU/yunity+book+club) by [Cille](https://yunity.atlassian.net/wiki/display/~Cille) and [Douglas Webb](https://yunity.atlassian.net/wiki/display/~dmhwebb) .

#### In Progress

*   Lamâsching keeps being a somewhat controversial topic. Recent discussions in [#culture](https://yunity.slack.com/messages/culture/) on Slack show, that [the existing documentation](https://yunity.atlassian.net/wiki/pages/viewpage.action?pageId=41812082) needs to be reviewed, updated and adapted to describe, rather than prescribe, how lamâsching culture works and to make the humorous origin of the whole topic more clear.

#### Challenges/help needed

You have an opinion on lamâsching? You wrote a poem or recorded a song? Please share! We'd happily collect your thoughts on everything yunity related on the wiki! ![](/user/themes/twentyfifteen/images/emoticons/smile.png)

* * *

### Research.

#### In Progress

*   Creation of an internal survey to assess how people feel about their contributions and what is needed to facilitate further contributions to the project.

#### Challenges/help needed

The challenge will be to get people to fill out the survey ![](/user/themes/twentyfifteen/images/emoticons/smile.png)

* * *

### Public Relations.

#### In Progress

*   Creation of a Wikipedia article about yunity.

#### Challenges/help needed

Has anyone experience with creating Wikipedia articles? Get in touch with [Arno Döpper](https://yunity.atlassian.net/wiki/display/~Arno) ![](/user/themes/twentyfifteen/images/emoticons/smile.png)

* * *

### About the heartbeat.

The heartbeat is a biweekly summary of what happens in yunity. It is meant to give an overview over our currents actions and topics.

##### When and how does it happen?

Every other weekend we collect information on a wiki page and publish it the following Monday as a wiki blog article. Afterwards we add a nice abstract and share it on [facebook](https://www.facebook.com/yunity.org/) .

##### Past heartbeats:

##### Blog Posts

*   Blog: [yunity heartbeat 2017-04-30](https://yunity.atlassian.net/wiki/display/YUN/2017/05/02/yunity+heartbeat+2017-04-30) created by [Laurina](https://yunity.atlassian.net    /wiki/display/~laurina
    ) May 02, 2017 [yunity](https://yunity.atlassian.net/wiki/spaces/YUN)
*   Blog: [yunity heartbeat 2017-04-16](https://yunity.atlassian.net/wiki/display/YUN/2017/04/16/yunity+heartbeat+2017-04-16) created by [Tilmann](https://yunity.atlassian.net    /wiki/display/~tiltec
    ) Apr 16, 2017 [yunity](https://yunity.atlassian.net/wiki/spaces/YUN)
*   Blog: [yunity heartbeat 2017-04-02](https://yunity.atlassian.net/wiki/display/YUN/2017/04/03/yunity+heartbeat+2017-04-02) created by [Janina Abels](https://yunity.atlassian.net    /wiki/display/~Janina
    ) Apr 03, 2017 [yunity](https://yunity.atlassian.net/wiki/spaces/YUN)
*   Blog: [yunity heartbeat 2017-03-19](https://yunity.atlassian.net/wiki/display/YUN/2017/03/20/yunity+heartbeat+2017-03-19) created by [Janina Abels](https://yunity.atlassian.net    /wiki/display/~Janina
    ) Mar 20, 2017 [yunity](https://yunity.atlassian.net/wiki/spaces/YUN)
*   Blog: [yunity heartbeat 2017-03-05](https://yunity.atlassian.net/wiki/display/YUN/2017/03/07/yunity+heartbeat+2017-03-05) created by [Janina Abels](https://yunity.atlassian.net    /wiki/display/~Janina
    ) Mar 07, 2017 [yunity](https://yunity.atlassian.net/wiki/spaces/YUN)

##### How to contribute?

*   You find the template for the next heartbeat [here](https://yunity.atlassian.net/wiki/display/YUN/heartbeat) .
*   Edit it as you see fit and add everything you did, that you see relevant to yunity!
*   Talk to us in [#heartbeat](https://yunity.slack.com/messages/heartbeat/) on Slack about the content, the layout or any other heartbeat related issues and ideas!

---
title: "yunity heartbeat 2017-01-08"
date: "2017-01-08"
continue_link: true
taxonomy:
    category: blog
    tag: [heartbeat]
published: true
---

The yunity heartbeat - what has each team done, what are they doing and what do they need help with.

* * *

## WuppDays Bad Dürrenberg.

Apart from normal WuppHaus developments, this time we had internal WuppDays in Badue! Over Christmas and New Year's a lot of yuniteers gathered in the cold but friendly train station, which - by the way - now has a fully equipped kitchen, a comfy sleeping room with mattresses, a heatable living room with matching sofas and a compost toilet with detailed explanations... ![](/user/themes/twentyfifteen/images/emoticons/wink.png)

![](2017-01-08/00.IMG_20170104_201350.jpg)

Look at [these new pictures](https://yunity.atlassian.net/wiki/display/BADUE/2017-01-05) capturing the new look and feel of the rooms!

Other challenges, which turned out to be easily solvable contained the following:

*   The WiFi was enough for over 20 people with laptops and smartphones!
*   Thanks to almost everybody bringing food we even had _too much_ at some point!
*   The sleeping spaces got warmer and even more cozy with all those lovely people there!

During the Badue WuppDays we talked about tons of different topics and questions, including the following:

*   How can we make it easier for interested people to contribute?
*   How can we effectively encourage people to contribute more?
*   Which tools do we want to use to work together?
*   What is going to happen over the next months?

As you can probably imagine, there have been a lot of different answers to these pretty vague questions. The first three heavily touch our general organizational structure and how we communicate and there is not one simple answer to any of them. What enlivens the discussion is also the question if we should sacrifice a certain degree of user friendliness and the benefit of being used to the proprietary tools already in use (like Slack and Confluence) for the sake of supporting open source software, which - of course - would be truer to our values. More on this topic can be read further down in IT-service and Onboarding.

When it comes to the question of what is going to happen over the next months, there have been three topics governing the talks:

*   Going to Spain
*   Getting two houses in Wurzen
*   Planning WuppDays XXL in Berlin

![](2017-01-08/IMG_20170104_173400.jpg) Just to make it clear: We don't plan on abandoning the train station in Bad Dürrenberg! It's actually the contrary, because since we are so many people with different skills, interests and dreams, we think we now can do more than one project at once! Spain would be only temporary anyways - and as part of the [ FSINT/FSWW tours ](https://yunity.atlassian.net/wiki/display/TOUR/Foodsaving+Tours) it's not even new... - and it could replenish the energy of the people wupping in the first ever acquired WuppHaus with all the nice sunshine and Mediterranean flair it would provide. Wurzen is just as far from Leipzig as Badue is, just on the east instead of the west and could thus serve as a base for the people working on rebuilding the train station, too. Berlin WuppDays are always great opportunities to recruit people who are not too far away to also lend a hand in Badue... ![](/user/themes/twentyfifteen/images/emoticons/wink.png)

And to erase every last doubt that we love our first house, just watch this new - and pretty long - video collage that collects [snapshots from the WuppHaus](https://www.youtube.com/watch?v=hOX6JaAgwW8) for you to get a glimpse of the feel we enjoy there everyday. You can see the new order in the kitchen and food storage and the general spirit of communal living, that was established even further during these winterly WuppDays due to the big amount of people coming by.

Okay, now to the three above-mentioned points:

Spain: [Tilmann](https://yunity.atlassian.net/wiki/display/~tiltec) arrived in Barcelona some days ago and the idea of having a Hackathon there or - more probable - in Valencia has been discussed weeks ago already. Now with the cold weather and warm spirit in Bad Dürrenberg a lot of people expressed motivation to flee the German winter for some weeks to go to Spain together. It would be to either set up a foodsaving and -sharing project or to connect to an existing one or preferably both. And a bit of holiday, too... ![](/user/themes/twentyfifteen/images/emoticons/wink.png) So far nothing is fix, but we are working on finding a location for a bunch of yunity folks to stay at starting end of January. [ Cille ](https://yunity.atlassian.net/wiki/display/~Cille) already did some research and [ Marian Roselló Tomás ](https://yunity.atlassian.net/wiki/display/~marianrosello) also provides a lot of insights concerning Valencia, as she's a resident there!

Wurzen: Since Badue obviously is a long-term construction project and some of us feel the great urge to have a more functional, ready and - let's face it - clean WuppHouse at hand soon, the quest for other buildings had never stopped. Now we found [a great possibility in Wurzen](https://yunity.atlassian.net/wiki/display/WW/General+information) , where two houses are for sale. A handful of us are seriously considering using money to buy them and gift them to the movement. This would require setting up [a legal entity like a Verein](https://yunity.atlassian.net/wiki/pages/viewpage.action?pageId=79364097) and set out in writing how we want to live together. Preparations are already underway, stay tuned for more updates on this topic!

WuppDays XXL: In late April we have the opportunity to use a huge compound in eastern Berlin for an assembly of people who are interested in yunity and the general kind of change yunity stands for. The planning just started, so it's not too late for you to join in! Just [write us an email](https://yunity.atlassian.netmailto:mail@yunity.org) , if you're interested!

* * *

## Foodsaving Tool.

#### Done

Thanks to [Nick Sellen](https://yunity.atlassian.net/wiki/display/~nicksellen) , we now have the fancy [foodsaving.world](http://foodsaving.world/) domain, which currently redirects to [fstool.yunity.org](http://fstool.yunity.org) . If you have ideas on how to use this domain (e.g. more information, additional links), please write to [fstool@yunity.org](https://yunity.atlassian.netmailto:fstool@yunity.org) ![](/user/themes/twentyfifteen/images/emoticons/smile.png)

For a more general overview on other internet-based foodsharing projects, we have [foodsaving.tech](https://foodsaving.tech/) . This site is managed via GitHub, you can add content yourself by clicking on the "contribute" link. [Nick Sellen](https://yunity.atlassian.net/wiki/display/~nicksellen) or [Tilmann](https://yunity.atlassian.net/wiki/display/~tiltec) will merge pull requests as they come.

The foodsaving tool itself also got a series of improvements over the last two weeks:

*   Password reset: you can now get a new temporary password if you forgot yours. It will be sent to your verified mail address ( ![](2017-01-08/github.png) [ GitHub ](https://github.com/yunity/foodsaving-frontend/pull/253) )
*   Mail verification: to make sure that you enter the right mail address and can receive mails from the tool, we send you a verification code after creating a new account
*   Password change: you can change your password on your user profile page, by clicking the edit button (the pencil)
*   Groups can be protected via password. If someone wants to enter a protected group, they have to prove their secret knowledge first ![](/user/themes/twentyfifteen/images/emoticons/wink.png)
*   Groups have a public and an internal description. The public description is shown before joining the group and could contain a link to a community website, whereas the internal description should provide members with the most up-to-date information ( [![](2017-01-08/github.png) GitHub ](https://github.com/yunity/foodsaving-frontend/pull/251) )
*   Show a (big) loading bar when the page is exchanging data with the server ( ![](2017-01-08/github.png) [ GitHub ](https://github.com/yunity/foodsaving-frontend/pull/254) )
*   [Some](https://github.com/yunity/foodsaving-frontend/pull/236) [hotfixes](https://github.com/yunity/foodsaving-frontend/pull/249)

##### New features of the foodsaving Tool

![](2017-01-08/pass-change.png) ![](2017-01-08/public_desc.png) ![](2017-01-08/group-pass.png) ![](2017-01-08/reset.png) ![](2017-01-08/verify.png)
#### In Progress

*   Processing feedback from users to [fstool@yunity.org](https://yunity.atlassian.netmailto:fstool@yunity.org) ( [Janina Abels,](https://yunity.atlassian.net/wiki/display/~Janina) [Tilmann](https://yunity.atlassian.net/wiki/display/~tiltec) )
*   [Recurring pickups](https://github.com/yunity/foodsaving-backend/issues/170) ( [Tilmann](https://yunity.atlassian.net/wiki/display/~tiltec) , [Nick Sellen](https://yunity.atlassian.net/wiki/display/~nicksellen) )
*   [Private messages and group chat](https://github.com/yunity/foodsaving-frontend/pull/191) ( [Andreas Langecker](https://yunity.atlassian.net/wiki/display/~chandi) )

#### Challenges/help needed

*   [More translations!](https://github.com/yunity/foodsaving-frontend#translation)
*   Getting direct feedback on planned features. Have a look [at those issues](https://github.com/yunity/foodsaving-frontend/labels/product-question) , it's not necessary to understand any programming language to help us ![](/user/themes/twentyfifteen/images/emoticons/smile.png) .
*   Refinement of the color scheme. If you are a designer and would like to get involved, please drop us a mail at [fstool@yunity.org](https://yunity.atlassian.netmailto:fstool@yunity.org) !

* * *

## IT-Service.

#### Done

![](2017-01-08/taigaad.png)

We have [a project on Taiga](https://board.disroot.org/project/paulfree-wupphaus/) now!

There have been first meetings and talks about how to use Taiga and [a core group of Taiga users](https://board.disroot.org/project/paulfree-wupphaus/team) assembled around [Paul Free](https://yunity.atlassian.net/wiki/display/~Paul+Free) to organize the tasks popping up in Badue as well as [the revision of the onboarding process in yunity](https://board.disroot.org/project/paulfree-wupphaus/kanban?epic=3) via Taiga. More on the topic of onboarding can be read in the newfound chapter of the same name.

#### In Progress

Taiga is in the process of being implemented as an organizational tool in yunity. This task requires quite some creativity, since we need to figure out how to make use of its modules and features to fit the whole range of different tasks and topic present in yunity at the moment. Taiga makes extensive use of [Scrum](https://en.wikipedia.org/wiki/Scrum_%28software_development%29) language and we still don't know to which extent we want to keep it or what to change it to, but hey... it's all learning by doing, isn't it? ![](/user/themes/twentyfifteen/images/emoticons/wink.png)

#### Challenges/help needed

A tool can just be as good as the people using it, and therefore a tool that is not used at all by people cannot work. If you want to support our efforts to promote existing open source software and work together with us on yunity related tasks in an organized way, then let us know!

* * *

## Onboarding.

#### Done

*   An initial meeting was held in Bad Dürrenberg restarting the important topic of how to integrate interested people into the project.
*   [Paul Free](https://yunity.atlassian.net/wiki/display/~Paul+Free) , [Janina Abels](https://yunity.atlassian.net/wiki/display/~Janina) , [Philip Engelbutzeder](https://yunity.atlassian.net/wiki/display/~Philip) and [Arno Döpper](https://yunity.atlassian.net/wiki/display/~Arno) have commited to be accountable for this task.
*   [Big differences between online and offline onboarding](https://yunity.atlassian.net/wiki/display/YUN/Online+vs.+offline+onboarding) have been pointed out.
*   An epic (that's like a main topic) has been created [on Taiga](https://board.disroot.org/project/paulfree-wupphaus/kanban?epic=3) .
*   A [team page](https://yunity.atlassian.net/wiki/display/YUN/Onboarding+Team) has been created on this wiki.

#### In Progress

*   The automated mails will be updated, revised and the whole process improved.
*   The existing information will be restructured to make it easier accessible. This is mainly about the wiki.

#### Challenges/help needed

*   How to set up automatically sent out mails with links, that somehow let us know if and which of the links got clicked?
*   More people feeling responsible in this regard make it easier to not let anybody fall through the cracks... (Also for holiday replacements and the likes... ![](/user/themes/twentyfifteen/images/emoticons/wink.png) )

* * *

## Structure.

#### In Progress

Our team member [Joachim Thome](https://yunity.atlassian.net/wiki/display/YUN/2017/01/09/yunity+heartbeat+2017-01-08) has published his [Syscon full manual](https://slack-files.com/T0B6WCFM5-F3K90K741-ac6c9b932a) , version 0.1\. It already consists of 36 pages, full of examples and how-tos on group decision making and resistance voting. And the sub-zero version number indicates that he intends to add more!

Here's a quote from the introduction:

> Deciding, alone or together, is not a minor issue. We make around 20.000 decisions each day (Ernst Poeppel, 2008) and a lot of these decisions are made subconsciously out of habit. This means that the major decision making systems that we have learned, for example authoritarian decision making from our childhood and work environment and majority voting from our political education, have a major influence on how we decide in our daily routines and by that how we live our life. This includes how we communicate with the people in our lives and how we resolve differences and conflicts on the social level.

Feedback can be given via our Slack chat in #structure or via [mail@yunity.org](https://yunity.atlassian.netmailto:mail@yunity.org) .

* * *

## Translation.

#### Challenges/help needed

*   All the nice videos about the WuppHaus are currently German only, so any subs would be very welcome! You don't even need to join the team to help out with that, if you're very shy... Just [read here](https://yunity.atlassian.net/wiki/display/YUN/Subtitling+Youtube+Videos+and+Translating+Descriptions) how to go about it and [find out here](https://yunity.atlassian.net/wiki/display/YUN/WuppHaus+Badue+Youtube+Subs) , which videos can be subbed... ![](/user/themes/twentyfifteen/images/emoticons/wink.png)

* * *

## About the heartbeat.

The heartbeat is a biweekly summary of what happens in yunity. It is meant to give an overview over our currents actions and topics.

#### When and how does it happen?

Every other weekend we collect information on a wiki page and publish it on Sunday or the following Monday as a wiki blog article.

Afterwards we add a nice abstract and share it on [facebook](https://www.facebook.com/yunity.org/) .

#### How to contribute?

*   Talk to us in [#heartbeat](https://yunity.slack.com/messages/heartbeat/) on Slack about the content, the layout or any other heartbeat related issues and ideas!

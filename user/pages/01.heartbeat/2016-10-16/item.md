---
title: "yunity heartbeat 2016-10-16"
date: "2016-10-16"
continue_link: true
taxonomy:
    category: blog
    tag: [heartbeat]
published: true
---

The yunity heartbeat - what people in yunity have done, what they are doing and what they need help with.

* * *

### Hackathon

![](2016-10-16/IMAG2966.jpg)

The last two weeks were dominated by the [yunity Hackathon](https://yunity.atlassian.net/wiki/pages/viewpage.action?pageId=65241160) in Berlin, on the weekend from 7th to 9th of October. After weeks of preparation, the event was really well-organized and focused on productive work.

To get a feeling of the event, you can watch the [introduction video and task overview](https://yunity.atlassian.net/wiki/display/YUN/Getting+started+in+the+Hackathon) - here are the slides of [Nick's](https://docs.google.com/presentation/d/1GN4Jj8MhIcm7zK6aLn35t0x7TKJAzMvWjIi6ADIqD9o/edit#slide=id.p) and [Tais'](https://docs.google.com/presentation/d/1bDrrBtaEuwWjKiSS93C2Pe8EiGeUPQgXJwod7wmSuGo/) presentation . The [Hackathon Retrospective](https://yunity.atlassian.net/wiki/display/YUN/Hackathon+Retrospective) was generally positive, with the only downsides being the short duration of the event.

We also roughly specified a few of the side projects that would be helpful to yunity: [Mapping Existing Foodsharing Initiatives](https://yunity.atlassian.net/wiki/display/YUN/Mapping+Existing+Foodsharing+Initiatives) and [Contributor Map Calendar](https://yunity.atlassian.net/wiki/display/YUN/Contributor+Map+Calendar) . The [yunity glocal / kickstart](https://yunity.atlassian.net/wiki/pages/viewpage.action?pageId=65241309) project was already started, contact [Paul Free](https://yunity.atlassian.net/wiki/display/~Paul+Free) for more information. You can also read a more detailed [specification](https://yunity.atlassian.net/wiki/display/~Paul+Free/Glocall+yunity) in his wiki space.

### General

On 2016-10-07, [Robert Lipp](https://yunity.atlassian.net/wiki/display/~Diogenes) also held a presentation on yunity in Frankfurt a.M. - you can have a look [at the slides here.](https://docs.google.com/presentation/d/1haJpHpgsRzSCgld2snU1pSW3F-rg5J8448ZfCxOkTOQ/edit#slide=id.p)

### [Foodsharing.de](http://Foodsharing.de) Development.

A recent development within yunity: we are starting again with the development of foodsharing.de.

> Foodsharing was originally written almost exclusively by the lovely Raphael Wintrich. He put the best part of two years of hard work and dedication into building the site. Most people would run out of motivation before completing it. [...]
> 
> There are probably many theories why development has slowed, the only one that makes sense to me is that _this stuff is hard_ , over time I hope to learn exactly why. For now the task is breathe life into the development again.
> 
> ~ [Nick Sellen](https://yunity.atlassian.net/wiki/display/~nicksellen) on [the first post of the new foodsharing devblog](https://devblog.foodsharing.de/2016/10/10/introducing.html)

During the hackathon, we had a meeting on [upcoming and long-term tasks,](https://yunity.atlassian.net/wiki/display/YUN/2016-10-08+foodsharing.de+upcoming+and+long-term+tasks) which also included a discussion on open-sourcing the code. We will review this in the beginning of November. If you are interested in it, join [#foodsharing-chat](https://yunity.slack.com/messages/foodsharing-chat/) on our Slack.

[Matthias Larisch](https://yunity.atlassian.net/wiki/display/~matthias) also [wrote a statement](https://devblog.foodsharing.de/2016/10/13/development-continues.html) on why he will continue with coding on foodsharing.de

The latest changes to the website are documented on [this page in the foodsharing wiki](https://wiki.foodsharing.de/Foodsharing.de_Plattform:_%C3%84nderungshistorie#2016-10-10) , in German language. If you want to participate in the discussion, have look into our [public issue tracker on Gitlab](https://gitlab.com/groups/foodsharing-dev) , or request access to the group to code with us.

#### Challenges/help needed

many things - are you knowledgeable about PHP? Then you are more welcome to join us!

* * *

### Design Team.

#### Done

Legal clearance for using the Harabara font - [Chrisi](https://yunity.atlassian.net/wiki/display/~Chrisi) asked the author for permission and he gave it to us (look into the comments of [Design Guidelines proposal](https://yunity.atlassian.net/wiki/display/YUN/Design+Guidelines+proposal) for details)

#### In Progress

Discussion on the [Design Guidelines proposal](https://yunity.atlassian.net/wiki/display/YUN/Design+Guidelines+proposal) . This currently is the only well-formulated proposal for yunity design by [Manuele Carlini](https://yunity.atlassian.net/wiki/display/~manuelecarlini) , but there was some resistance back then when it was posted to Slack. Still, because of the (accepted) [Open design proposal](https://yunity.atlassian.net/wiki/display/YUN/Open+design+proposal) , it's fine for yunity members to use - or use a different design to their own liking. ( [Tilmann](https://yunity.atlassian.net/wiki/display/~tiltec) , [Chrisi](https://yunity.atlassian.net/wiki/display/~Chrisi) )

#### Challenges/help needed

[Design for Foodsaving Tours](https://yunity.atlassian.net/wiki/display/YUN/Design+for+Foodsaving+Tours)

* * *

### Foodsaving Tool.

#### Done

A brief high-level description about the [Foodsaving Tool](https://yunity.atlassian.net/wiki/display/YUN/Foodsaving+Tool) ( [Tilmann](https://yunity.atlassian.net/wiki/display/~tiltec) , [Tais Real](https://yunity.atlassian.net/wiki/display/~Tais) , [Lars Wolf](https://yunity.atlassian.net/wiki/display/~donpiano) )

We welcome [Konrad Becker](https://yunity.atlassian.net/wiki/display/~Xbaal) in the coding team!

A lot of services are ready to talk to the backend - though they will be modified [to a common style](https://github.com/yunity/foodsaving-frontend/issues/55) soon.

Over 94% of our code is [covered by tests](https://codecov.io/gh/yunity/foodsaving-frontend) - tendency increasing! Yay! ![](https://yunity.atlassian.net/wiki/s/-1408836000/6447/d896085db166e385ab4bc7cb5333a1125f67142a/_/images/icons/emoticons/smile.png "(smile)")

#### In Progress

We are kickstarting the frontend in AngularJS - look at our [Github issues](https://github.com/yunity/foodsaving-frontend/issues) to follow the process closely.

#### Challenges/help needed

Most of us still have to get familiar with AngularJS and figure out the best code architecture.

* * *

### Foodsharing/-saving International.

#### Done

[Management structure diagrams](https://yunity.atlassian.net/wiki/display/YUN/Internal+structure+diagrams) of Foodsharing Warsaw, DLC Nantes and [Foodsharing.de](http://Foodsharing.de) ( [Tais Real](https://yunity.atlassian.net/wiki/display/~Tais) , [Janina Abels](https://yunity.atlassian.net/wiki/display/~Janina) )

Writeup on Foodsharing Taipeh (Taiwan) on [Existing initiatives](https://yunity.atlassian.net/wiki/display/YUN/Existing+initiatives#Existinginitiatives-TAIWAN-Taipei-FoodsharingTaiwan) from [Stefan Simon](https://yunity.atlassian.net/wiki/display/~stefanintaipei) .

An example of the enormous waste at festivals is documented on [Foodsaving at festivals](https://yunity.atlassian.net/wiki/display/YUN/Foodsaving+at+festivals) . There's a video that will blow your mind, and maybe motivate you to get active and start a [foodsaving community](https://project.yunity.org/foodsaving-international) ! It's quite easy to save food and other things at those festivals if you have a few great activists.

[Graphics](https://yunity.atlassian.net/wiki/display/FSINT/Graphics) and [Drafts](https://yunity.atlassian.net/wiki/display/FSINT/Drafts) repository for visual things for spreading foodsaving - currently mostly drawings by Luisa from Copenhagen.

A new [facebook group for connecting foodsaving groups worldwide](https://www.facebook.com/groups/151180382009619/) . Many people are not active in our wiki or on Slack, so [Tilmann](https://yunity.atlassian.net/wiki/display/~tiltec) 's idea was to also gather people on facebook.

Two brainstorming meetings at the hackathon were organized by [Tais Real](https://yunity.atlassian.net/wiki/display/~Tais) , about the [reliability of foodsavers](https://yunity.atlassian.net/wiki/display/YUN/Brainstorming+-+Approaching+Businesses) and [approaching businesses](https://yunity.atlassian.net/wiki/display/YUN/Brainstorming+-+Approaching+Businesses) with the goal of starting foodsaving.

#### In Progress

A syscon on the [appropriate name for FSINT and the slack channel fs-international](https://business.konsensieren.eu/en/konsensierung/wyg3c9utr/anzeigen) has been started, the proposal phase is running until 2016-10-19 and the voting phase will start shortly afterwards.

* * *

### IT-Service.

#### Done

Open up the [Signup Autoresponder](https://yunity.atlassian.net/wiki/display/YUN/Signup+Autoresponder) - that's the mail that people automatically get after filling out the [join-the-team form](https://project.yunity.org/join-the-team) on [yunity.org](http://yunity.org) . The goal is to keep it up-to-date with general information how to get started in yunity. ( [Paul Free](https://yunity.atlassian.net/wiki/display/~Paul+Free) , [Janina Abels](https://yunity.atlassian.net/wiki/display/~Janina) , [Tilmann](https://yunity.atlassian.net/wiki/display/~tiltec) )

Updated the [events page on yunity.org](https://project.yunity.org/events) ( [Tilmann](https://yunity.atlassian.net/wiki/display/~tiltec) ) - please write in Slack #website if you want to add an event!

#### In Progress

Setting up a [Grafana](https://yunity.atlassian.net/wiki/display/YUN/Grafana) / [InfluxDB](https://yunity.atlassian.net/wiki/display/YUN/InfluxDB) analytics setup to get nicer statistics for yunity and [foodsharing.de](http://foodsharing.de) servers. It's a really powerful tool, which might also help us in getting more insight how we can improve our software. ( [Matthias Larisch](https://yunity.atlassian.net/wiki/display/~matthias) )

* * *

### Structure.

#### Done

[Tais Real](https://yunity.atlassian.net/wiki/display/~Tais) collected many [open tasks](https://yunity.atlassian.net/wiki/display/YUN/6.+Open+tasks) to make them visible for newcomers. Some examples: [Researching existing initiatives](https://yunity.atlassian.net/wiki/display/YUN/Researching+existing+initiatives) , [Organizing the Media-Kit](https://yunity.atlassian.net/wiki/display/YUN/Organizing+the+Media-Kit) , [Translation](https://yunity.atlassian.net/wiki/display/YUN/Translation) and [Contacting enthusiasts](https://yunity.atlassian.net/wiki/display/YUN/Contacting+enthusiasts)

A concise article about [Awesome Active Autonomy](https://yunity.atlassian.net/wiki/display/YUN/Awesome+Active+Autonomy) by [Douglas Webb](https://yunity.atlassian.net/wiki/display/~dmhwebb) - the basic working principle in yunity. Read it to get more insight in autonomous decision making!

Follow new applications in the [Who-am-I section](http://yunity.trydiscourse.com/c/welcome/who-am-i) of the discourse forum. You can also follow the new entries on Slack in the [#discourse](https://yunity.slack.com/messages/discourse/) channel.

#### In Progress

Collecting ideas how to [improve the yunity wiki accessibility](https://yunity.atlassian.net/wiki/display/IDEAS/Improve+yunity+wiki+accessibility) . [Janina Abels](https://yunity.atlassian.net/wiki/display/~Janina) created a proposal for a new [FSINT landing page](https://yunity.atlassian.net/wiki/display/%7EJanina/FSINT+landing+page) , and she really loves feedback on it ![](/user/themes/twentyfifteen/images/emoticons/smile.png) There's also a [ Slack channel #improve_wiki ](https://yunity.slack.com/messages/improve_wiki/) where you can participate in the process.

* * *

### Connections.

#### Done

[Nick Sellen](https://yunity.atlassian.net/wiki/display/~nicksellen) , [Matthias Larisch](https://yunity.atlassian.net/wiki/display/~matthias) and [Tilmann](https://yunity.atlassian.net/wiki/display/~tiltec) had a short informal meeting with [Raphael Fellmer](https://yunity.atlassian.net/wiki/display/~Raphael) and [Martin Schott](https://yunity.atlassian.net/wiki/display/~der.phobos) from [sharecy](http://sharecy.org/) . Read a short summary on [Collaboration possibilities](https://yunity.atlassian.net/wiki/display/YUN/Collaboration+possibilities) .

[Paul Free](https://yunity.atlassian.net/wiki/display/~Paul+Free) made a lot's of new connections during the freemarket in Berlin. Interviews with around 40 incl. gathering their contacts.

#### Challenges/help needed

...networking can be exausting. ( [Paul Free](https://yunity.atlassian.net/wiki/display/~Paul+Free) l)

* * *

### [Tour](https://yunity.atlassian.net/wiki/pages/viewpage.action?pageId=61898757) .

A [really extensive report](http://yunity.trydiscourse.com/t/marseille-information-report/131) about the situation in Marseille by [Anna O'Neill](https://yunity.atlassian.net/wiki/display/~aoneill11) . The city is one of the [first planned destinations](https://yunity.atlassian.net/wiki/pages/viewpage.action?pageId=62554235) of the yunity tour.

Some people plan to visit [Valencia (Spain) in January 2016](http://yunity.trydiscourse.com/t/valencia-jan-feb-2017/110) and spread foodsharing and -saving.

* * *

### Translation.

#### Done

Some ideas for [Grammar conventions](https://yunity.atlassian.net/wiki/display/YUN/Spelling+Conventions+and+Recurring+Terms#SpellingConventionsandRecurringTerms-Grammarconventions) (in which order adjective should appear), contributed by [Hans-Christian Eick](https://yunity.atlassian.net/wiki/display/~birke) .

A [video guide how to translate](https://slack-files.com/T0B6WCFM5-F2PEEN0LB-a1b8f64dc8) the [foodsharing dev blog](http://devblog.foodsharing.de/) , with an additional [written guide](https://yunity.slack.com/archives/translation/p1476461620000060) on Slack ( [Matthias Larisch](https://yunity.atlassian.net/wiki/display/~matthias) , [Tilmann](https://yunity.atlassian.net/wiki/display/~tiltec) )

Full German [foodsharing dev blog](https://devblog.foodsharing.de/index.de.html) ( [Fenja Jacobs](https://yunity.atlassian.net/wiki/display/~fenja.jacobs) , [Janina Abels](https://yunity.atlassian.net/wiki/display/~Janina) )

* * *

### WuppDays.

#### In Progress

Planning of the [Mini-Wuppdays in Chemnitz](https://yunity.atlassian.net/wiki/display/YUN/Mini-Wuppdays+in+Chemnitz) by [Anja Konhäuser](https://yunity.atlassian.net/wiki/display/~Anja+K.) and [fr4nk 0nf1r3](https://yunity.atlassian.net/wiki/display/~fr4nk0nf1r3) .

The [WuppDays#12 Witzenhausen](https://yunity.atlassian.net/wiki/display/YUN/WuppDays#WuppDays-10Witzenhausen) are planned by [Paul Free](https://yunity.atlassian.net/wiki/display/~Paul+Free) and are expected to happen in November. Join the [Slack channel #wuppdays_witzenhausen](https://yunity.slack.com/messages/wuppdays_witzenhausen/) to stay tuned!

[Pre-planning of December WuppDays](https://yunity.slack.com/archives/wuppdays/p1476696681000002) in Kirchheim by [Philip Engelbutzeder](https://yunity.atlassian.net/wiki/display/~Philip)

* * *

### Culture.

The [Lamâsching Availability](https://yunity.atlassian.net/wiki/pages/viewpage.action?pageId=53706783) page still gets occasional updates, which range from usual to sexually open to not-so-serious.

Slight ongoing controversy about the [Sadomâsching Culture](https://yunity.atlassian.net/wiki/pages/viewpage.action?pageId=60424204) , introduced by [Bodhi Neiser](https://yunity.atlassian.net/wiki/display/~Bodhi) and [Kaiser Mikato](https://yunity.atlassian.net/wiki/display/~nitram) . There are worries if this should be something that is publicly visible on the yunity wiki. There has been a proposal from [Douglas Webb](https://yunity.atlassian.net/wiki/display/~dmhwebb) to make it only visible to members of yunity (wiki-editors), but so far no decision making process was started.

* * *

### Glocal yunity.

#### (what is this? - ask [Paul Free](https://yunity.atlassian.net/wiki/display/~Paul+Free) !) Done

"not organized" a freemarket in Berlin. Made lots of local connections, including people interested in glocal foodsharing in Spain.

![](2016-10-16/14715622_1145263808901104_257314803153432851_o.jpg)

---
title: "yunity heartbeat 2016-10-30"
date: "2016-10-30"
continue_link: true
taxonomy:
    category: blog
    tag: [heartbeat]
published: true
---

The yunity heartbeat - what has each team done, what are they doing and what do they need help with.

* * *

### [Foodsharing.de](http://foodsharing.de/) Development.

#### Done

The [foodsharing.de](http://foodsharing.de/) development is reopened! To keep track of what is going on in that regard visit the new [foodsharing devblog](https://devblog.foodsharing.de/index.en.html) . For direct answers to pressing questions like 'What?! Why?! How?!" read [this blog entry](https://devblog.foodsharing.de/2016/10/13/development-continues.html) written by [Matthias Larisch](https://yunity.atlassian.net/wiki/display/~matthias) . Also taken from that blog post are these already completed achievements:

*   Having a development environment that is checked out, setup and running with 3 commands (using docker/docker compose)
*   Integration of Codeception for Acceptance, API and Unit tests
*   Local execution of all tests
*   Automated execution of tests in a CI system (Gitlab CI) for every push
*   Acceptance tests for a very little selection of pages, more to come
*   Open issue tracker to include the community in bug reporting and feature discussion
*   Having one contributor working on feature development
*   Having three contributors working on fixing (security) issues and refactoring the code

Some days later [Matthias Larisch](https://yunity.atlassian.net/wiki/display/~matthias) was motivated to move the w iki, Mumble and the media database on a new server to fix some security issues present before. More about this can be read in [this blog post](https://devblog.foodsharing.de/2016/10/16/wiki-and-mumble-on-new-server-en.html) .

#### In Progress

> _Most of the time is now spent to make contribution as easy as possible. That will include refactoring, means touching almost every single line of code in the code base (approx. 50000 of them are there). We made the decision to slowly move in some core components of [symfony](https://symfony.com/components) and hopefully end up with a workable, fully tested code base that can be deployed from a continuous integration system automatically when a core contributor approves the changes. Having the platform open sourced is a strong wish from most contributors as it fits the vision of sharing._
> 
> [Matthias Larisch](https://yunity.atlassian.net/wiki/display/~matthias) , foodsharing devblog

* * *

### Foodsaving Tool.

#### Done

Created an [open chatroom](https://riot.im/app/#/room/#foodsaving-tool:matrix.org) , linked in the README of the GitHub repository, bridged it to the Slack channel

Included more functionality & code structure:

*   Picker for groups in navigation bar
*   Added translation support, language picker in navigation bar
*   Unified templates for main pages (e.g. group, store) and splash pages (login, signup)
*   Signup & login page in directive-free style, using ng-click
*   Convention for partials (components which are using inside pages) - they now start with an underscore (_)

#### In Progress

Started discussing features on a product level - look at the [current questions here](https://github.com/yunity/foodsaving-frontend/labels/product-question) and contribute your ideas! (E.g. should users be required to enter first/last name, do we need a feature for trial pickups, how do we prevent abuse of powers)

[Planning](https://yunity.atlassian.net/wiki/display/YUN/Planning) the foodsaving tool. Started collecting [user requirements](https://yunity.atlassian.net/wiki/display/YUN/Requirements) in a written way - currently only Taiwan, more hopefully coming soon.

Looking for a logo ! Need to answer the basic questions: _"What is the message we want to communicate? Which emotion do we want to effect?"_ Proposals:

![](2016-10-30/save-carrot.png) ![](2016-10-30/fist-the-carrot.png)

Post your ideas [in GitHub](https://github.com/yunity/foodsaving-frontend/issues/110) or in Slack in [#foodsaving-tool-plan](https://yunity.slack.com/messages/foodsaving-tool-plan/) !

* * *

### Foodsaving worldwide.

#### Done

Finally we held a syscon about how to name the FSINT sections on the wiki and on Slack, which resulted in: [Foodsaving worldwide](https://business.konsensieren.eu/en/konsensierung/wyg3c9utr/ergebnis) ! (Hence the shortened title of this paragraph... ![](/user/themes/twentyfifteen/images/emoticons/wink.png) )

[Tilmann](https://yunity.atlassian.net/wiki/display/~tiltec) put the [graphics](https://yunity.atlassian.net/wiki/display/FSINT/Graphics) and drafts for logos on the wiki to make them accessible and editable for anybody interested.

#### In Progress

*   getting in contact with people using #foodsharing on twitter ( [Paul Free](https://yunity.atlassian.net/wiki/display/~Paul+Free) )
*   refining and renaming what used to be called the 'media kit' and is now ' [material to get started](https://yunity.atlassian.net/wiki/display/FSINT/Material+to+get+started) ' ( [Janina Abels](https://yunity.atlassian.net/wiki/display/~Janina) )
*   creating a new page collecting [existing platforms](https://yunity.atlassian.net/wiki/display/FSINT/Existing+platforms) ( [Janina Abels](https://yunity.atlassian.net/wiki/display/~Janina) , [Tilmann](https://yunity.atlassian.net/wiki/display/~tiltec) )
*   getting in contact with [OLIO](https://olioex.com/) after they made offers on their app moneyfree ( [Nick Sellen](https://yunity.atlassian.net/wiki/display/~nicksellen) , [Janina Abels](https://yunity.atlassian.net/wiki/display/~Janina) )

#### Challenges/help needed

*   more feedback and co-creation wanted with regards to the material to get started!
*   summary of the Russian foodsharing projects visible on [vk.com](http://vk.com/) is still missing

* * *

### IT-Service.

#### Done

*   setting up channels in matrix (via riot chat) incl. incoming and outgoing webhooks. (from matrix you can chat towards slack and other way around) ( [Tilmann](https://yunity.atlassian.net/wiki/display/~tiltec) , [Kaiser Mikato](https://yunity.atlassian.net/wiki/display/~nitram) )
*   rocket.chat and slack integration ( [Paul Free](https://yunity.atlassian.net/wiki/display/~Paul+Free) )

#### In Progress

*   importing slack data into rocket.chat ( [Paul Free](https://yunity.atlassian.net/wiki/display/~Paul+Free) )
*   research for hrm programs etc. ( [Nick Sellen](https://yunity.atlassian.net/wiki/display/~nicksellen) , [Tilmann](https://yunity.atlassian.net/wiki/display/~tiltec) )

#### Challenges/help needed

*   rocket.chat import freezing while doing so

* * *

### Structure.

#### Done

*   developing a [detailed plan of how to restructure the wiki](https://yunity.atlassian.net/wiki/display/IDEAS/Improve+yunity+wiki+accessibility) using spaces to make it more accessible ( [Tilmann](https://yunity.atlassian.net/wiki/display/~tiltec) , [Janina Abels](https://yunity.atlassian.net/wiki/display/~Janina) )
*   creating landing page proposals for the new [Culture](https://yunity.atlassian.net/wiki/display/~Janina/Culture+landing+page) and [WuppHouse](https://yunity.atlassian.net/wiki/display/~Janina/WuppHouse+landing+page) wikispaces ( [Janina Abels](https://yunity.atlassian.net/wiki/display/~Janina) )

#### In Progress

*   [writing and thinking](https://douginamug.gitbooks.io/a-systemic-consensus-manual-testing/content/) about decision making theory, autonomy etc. ( [Douglas Webb](https://yunity.atlassian.net/wiki/display/~dmhwebb) )
*   setting up [WuppDays Witzenhausen](https://yunity.atlassian.net/wiki/display/YUN/Wuppdays+%28%2312%29+Witzenhausen) ( [Hans-Christian Eick](https://yunity.atlassian.net/wiki/display/~birke) , [Paul Free](https://yunity.atlassian.net/wiki/display/~Paul+Free) )
*   discussing project identity based on [an article](https://yunity.atlassian.net/wiki/display/IDEAS/Project+identity+-+yunity%2C+foodsharing%2C+sharecy) written by [Janina Abels](https://yunity.atlassian.net/wiki/display/~Janina) ( [Philip Engelbutzeder](https://yunity.atlassian.net/wiki/display/~Philip) , [Tais Real](https://yunity.atlassian.net/wiki/display/~Tais) , [Paul Free](https://yunity.atlassian.net/wiki/display/~Paul+Free) , [Tilmann](https://yunity.atlassian.net/wiki/display/~tiltec) , [Matthias Larisch](https://yunity.atlassian.net/wiki/display/~matthias) , [Janina Abels](https://yunity.atlassian.net/wiki/display/~Janina) )
*   started thinking about [#community-guidelines](https://yunity.slack.com/messages/community-guidelines/) and how to handle destructive behaviors ( [Nick Sellen](https://yunity.atlassian.net/wiki/display/~nicksellen) , [Tilmann](https://yunity.atlassian.net/wiki/display/~tiltec) )

#### Challenges/help needed

*   what does yunity actually signify to its contributors individually?
*   how can we be open to everybody and still protect an atmosphere of trust if we encounter destructive and unreasonable behaviors?

* * *

### WuppHouse.

#### Done

*   [conference call with Bernd](https://yunity.atlassian.net/wiki/display/YUN/2016-10-19+Conference+call+with+Bernd+of+the+Gemeinschaftsstifter+project) from Gemeinschaftsstifter ( [Bodhi Neiser](https://yunity.atlassian.net/wiki/display/~Bodhi) , [Matthias Larisch](https://yunity.atlassian.net/wiki/display/~matthias) , [Arno Döpper](https://yunity.atlassian.net/wiki/display/~Arno) )
*   visited [Freiraum in Berlin Weissensee](http://www.kubiz-wallenberg.de/) ( [Philip Engelbutzeder](https://yunity.atlassian.net/wiki/display/~Philip) , [Axel Kalitzki](https://yunity.atlassian.net/wiki/display/~syrt) , [Paul Free](https://yunity.atlassian.net/wiki/display/~Paul+Free) , [Katia](https://yunity.atlassian.net/wiki/display/~piersonkatia) , ...)

#### In Progress

*   analyzing Mietshäusersyndikat principle and formal paper ( [Bodhi Neiser](https://yunity.atlassian.net/wiki/display/~Bodhi) )

#### Challenges/help needed

*   finding the right building
*   finding the right legal setup
*   developing a clear concept of how to live together in a WuppHouse

* * *

### Translation.

#### Done

*   [foodsharing devblog](https://devblog.foodsharing.de/index.en.html) translation via [gitlab](https://gitlab.com/foodsharing-dev/foodsharing-dev.gitlab.io/issues) ( [Fenja Jacobs](https://yunity.atlassian.net/wiki/display/~fenja.jacobs) )
*   [foodsharing devblog translation instructions](https://yunity.atlassian.net/wiki/display/YUN/Foodsharing+Devblog+Translation) ( [Tilmann](https://yunity.atlassian.net/wiki/display/~tiltec) , [Janina Abels](https://yunity.atlassian.net/wiki/display/~Janina) )

#### In Progress

*   foodsharing devblog translation via [gitlab](https://gitlab.com/foodsharing-dev/foodsharing-dev.gitlab.io/issues) (everybody can just work on an issue... ![](/user/themes/twentyfifteen/images/emoticons/smile.png) )
*   translation of the first strings of the foodsaving tool via [transifex](https://www.transifex.com/yunity-1/foodsaving-tool/dashboard/) ( [Tilmann](https://yunity.atlassian.net/wiki/display/~tiltec) , [Janina Abels](https://yunity.atlassian.net/wiki/display/~Janina) )

#### Challenges/help needed

*   French translation of the foodsharing devblog issued on gitlab

* * *

### Public Relations.

#### Done

*   contact with nomadbase ( [Philip Engelbutzeder](https://yunity.atlassian.net/wiki/display/~Philip) )
*   workshop in Bern about yunity with (Felix, [Katia](https://yunity.atlassian.net/wiki/display/~piersonkatia) , [fritz holscher](https://yunity.atlassian.net/wiki/display/~fritz) , [Arno Döpper](https://yunity.atlassian.net/wiki/display/~Arno) )
*   brochure and flyer for yunity inspired by [http://crimethinc.com/tce/](http://crimethinc.com/tce/) and glocal yunity dreaming sessions ( [Philip Engelbutzeder](https://yunity.atlassian.net/wiki/display/~Philip) , [Paul Free](https://yunity.atlassian.net/wiki/display/~Paul+Free) )
*   lonly warriors in [reddit/yunity](https://www.reddit.com/r/yunity/) ( [Arno Döpper](https://yunity.atlassian.net/wiki/display/~Arno) , [Paul Free](https://yunity.atlassian.net/wiki/display/~Paul+Free) , [Tilmann](https://yunity.atlassian.net/wiki/display/~tiltec) )
*   Key Note at the Stipendiaten machen Programm: Wirtschaftsmacht Europa ? (Studienstiftung des deutschen Volkes) - Thema: Selbstbestimmung, Vertrauen und Kollaboration als Grundpfeiler des europäischen Wirtschaftsmacht aus dem Blickwinkel der Gift Economy ( [Philip Engelbutzeder](https://yunity.atlassian.net/wiki/display/~Philip) )

#### Challenges/help needed

*   do we want to paper print? (by [Katia](https://yunity.atlassian.net/wiki/display/~piersonkatia) )

* * *

### Community Relations.

#### In Progress

*   reflecting on communication culture (especially within Slack) ( [Nick Sellen](https://yunity.atlassian.net/wiki/display/~nicksellen) , [Philip Engelbutzeder](https://yunity.atlassian.net/wiki/display/~Philip) , [Paul Free](https://yunity.atlassian.net/wiki/display/~Paul+Free) , [Kaiser Mikato](https://yunity.atlassian.net/wiki/display/~nitram) )
*   connecting to ecobytes and transformap during WuppDays Witzenhausen
*   visiting and experiencing [Projekt Werkstatt Saasen](http://www.projektwerkstatt.de/pwerk/saasen.html) ( [Douglas Webb](https://yunity.atlassian.net/wiki/display/~dmhwebb) , [Zed Redstone](https://yunity.atlassian.net/wiki/display/~inflector) , [Selina Camile](https://yunity.atlassian.net/wiki/display/~Selina) , [Lara Earthling](https://yunity.atlassian.net/wiki/display/~rose+earthling) , [Hans-Christian Eick](https://yunity.atlassian.net/wiki/display/~birke) , [Paul Free](https://yunity.atlassian.net/wiki/display/~Paul+Free) , [Bodhi Neiser](https://yunity.atlassian.net/wiki/display/~Bodhi) ....)
*   new people signing up on our different communication channels constantly! ![](https://yunity.atlassian.net/wiki/s/-705042133/6447/63284c861170530db9b4c8001df5e6777c89815a/_/images/icons/emoticons/biggrin.png "(big grin)")

* * *

### Future WuppDays.

#### In Progress

*   looking for a WuppSpace in Austria, close to Vienna ( [Chrisi](https://yunity.atlassian.net/wiki/display/~Chrisi) )

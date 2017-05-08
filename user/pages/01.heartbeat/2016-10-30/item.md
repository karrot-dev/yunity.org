---
title: "yunity heartbeat 2016-10-30"
date: "2016-10-30"
continue_link: true
taxonomy:
    category: blog
    tag: [heartbeat]
published: true
---

<div class="wiki-content">
 <div>
  <p>
   <strong>
    The yunity heartbeat
   </strong>
   - what has each team done, what are they doing and what do they need help with.
  </p>
  <hr/>
 </div>
 <h2 id="yunityheartbeat2016-10-30-Foodsharing.deDevelopment.">
  <span style="color: rgb(0,0,0);">
   <strong>
    <a class="external-link" href="http://foodsharing.de/" rel="nofollow">
     Foodsharing.de
    </a>
    Development.
   </strong>
  </span>
 </h2>
 <h3 id="yunityheartbeat2016-10-30-Done">
  <span style="color: rgb(0,0,0);">
   <span style="color: rgb(153,204,0);">
    Done
   </span>
  </span>
 </h3>
 <p>
  <span style="color: rgb(0,0,0);">
   The
   <a class="external-link" href="http://foodsharing.de/" rel="nofollow">
    foodsharing.de
   </a>
   development is reopened! To keep track of what is going on in that regard visit the new
   <a class="external-link" href="https://devblog.foodsharing.de/index.en.html" rel="nofollow">
    foodsharing devblog
   </a>
   .
   <br/>
   For direct answers to pressing questions like 'What?! Why?! How?!" read
   <a class="external-link" href="https://devblog.foodsharing.de/2016/10/13/development-continues.html" rel="nofollow">
    this blog entry
   </a>
   written by
   <a class="confluence-userlink user-mention" data-base-url="https://yunity.atlassian.net/wiki" data-linked-resource-id="2981927" data-linked-resource-type="userinfo" data-linked-resource-version="2" data-username="matthias" href="https://yunity.atlassian.net/wiki/display/~matthias">
    Matthias Larisch
   </a>
   . Also taken from that blog post are these already completed achievements:
  </span>
 </p>
 <ul>
  <li>
   <span style="color: rgb(0,0,0);">
    Having a development environment that is checked out, setup and running with 3 commands (using docker/docker compose)
   </span>
  </li>
  <li>
   <span style="color: rgb(0,0,0);">
    Integration of Codeception for Acceptance, API and Unit tests
   </span>
  </li>
  <li>
   <span style="color: rgb(0,0,0);">
    Local execution of all tests
   </span>
  </li>
  <li>
   <span style="color: rgb(0,0,0);">
    Automated execution of tests in a CI system (Gitlab CI) for every push
   </span>
  </li>
  <li>
   <span style="color: rgb(0,0,0);">
    Acceptance tests for a very little selection of pages, more to come
   </span>
  </li>
  <li>
   <span style="color: rgb(0,0,0);">
    Open issue tracker to include the community in bug reporting and feature discussion
   </span>
  </li>
  <li>
   <span style="color: rgb(0,0,0);">
    Having one contributor working on feature development
   </span>
  </li>
  <li>
   <span style="color: rgb(0,0,0);">
    Having three contributors working on fixing (security) issues and refactoring the code
    <br class="_mce_tagged_br"/>
   </span>
  </li>
 </ul>
 <p>
  <span style="color: rgb(0,0,0);">
   Some days later
   <a class="confluence-userlink user-mention" data-base-url="https://yunity.atlassian.net/wiki" data-linked-resource-id="2981927" data-linked-resource-type="userinfo" data-linked-resource-version="2" data-username="matthias" href="https://yunity.atlassian.net/wiki/display/~matthias">
    Matthias Larisch
   </a>
   was motivated to move the w
   <span style="color: rgb(17,17,17);">
    iki, Mumble and the media database on a new server to fix some security issues present before. More about this can be read in
    <a class="external-link" href="https://devblog.foodsharing.de/2016/10/16/wiki-and-mumble-on-new-server-en.html" rel="nofollow">
     this blog post
    </a>
    .
   </span>
  </span>
 </p>
 <h3 id="yunityheartbeat2016-10-30-InProgress">
  <span style="color: rgb(128,128,128);">
   In Progress
  </span>
 </h3>
 <blockquote>
  <p>
   <em>
    <span style="color: rgb(0,0,0);">
     <span style="color: rgb(17,17,17);">
      Most of the time is now spent to make contribution as easy as possible. That will include refactoring, means touching almost every single line of code in the code base (approx. 50000 of them are there). We made the decision to slowly move in some core components of
     </span>
     <a class="external-link" href="https://symfony.com/components" rel="nofollow">
      symfony
     </a>
     <span style="color: rgb(17,17,17);">
      and hopefully end up with a workable, fully tested code base that can be deployed from a continuous integration system automatically when a core contributor approves the changes. Having the platform open sourced is a strong wish from most contributors as it fits the vision of sharing.
     </span>
    </span>
   </em>
  </p>
  <p style="text-align: right;">
   <span style="color: rgb(0,0,0);">
    <span style="color: rgb(17,17,17);">
     <a class="confluence-userlink user-mention" data-base-url="https://yunity.atlassian.net/wiki" data-linked-resource-id="2981927" data-linked-resource-type="userinfo" data-linked-resource-version="2" data-username="matthias" href="https://yunity.atlassian.net/wiki/display/~matthias">
      Matthias Larisch
     </a>
     , foodsharing devblog
    </span>
   </span>
  </p>
 </blockquote>
 <p>
  <span style="color: rgb(0,0,0);">
   <strong>
    <br/>
   </strong>
  </span>
 </p>
 <hr/>
 <h2 id="yunityheartbeat2016-10-30-FoodsavingTool.">
  <span style="color: rgb(0,0,0);">
   <strong>
    Foodsaving Tool.
   </strong>
  </span>
 </h2>
 <h3 id="yunityheartbeat2016-10-30-Done.1">
  <span style="color: rgb(0,0,0);">
   <span style="color: rgb(153,204,0);">
    Done
   </span>
  </span>
 </h3>
 <p>
  <span style="color: rgb(0,0,0);">
   Created an
   <a class="external-link" href="https://riot.im/app/#/room/#foodsaving-tool:matrix.org" rel="nofollow">
    open chatroom
   </a>
   , linked in the README of the GitHub repository, bridged it to the Slack channel
  </span>
 </p>
 <p>
  <span style="color: rgb(0,0,0);">
   Included more functionality &amp; code structure:
  </span>
 </p>
 <ul>
  <li>
   <span style="color: rgb(0,0,0);">
    Picker for groups in navigation bar
   </span>
  </li>
  <li>
   <span style="color: rgb(0,0,0);">
    Added translation support, language picker in navigation bar
   </span>
  </li>
  <li>
   <span style="color: rgb(0,0,0);">
    Unified templates for main pages (e.g. group, store) and splash pages (login, signup)
   </span>
  </li>
  <li>
   <span style="color: rgb(0,0,0);">
    Signup &amp; login page in directive-free style, using ng-click
   </span>
  </li>
  <li>
   <span style="color: rgb(0,0,0);">
    Convention for partials (components which are using inside pages) - they now start with an underscore (_)
    <br/>
   </span>
  </li>
 </ul>
 <h3 id="yunityheartbeat2016-10-30-InProgress.1">
  <span style="color: rgb(128,128,128);">
   In Progress
  </span>
 </h3>
 <p>
  <span style="color: rgb(0,0,0);">
   Started discussing features on a product level - look at the
   <a class="external-link" href="https://github.com/yunity/foodsaving-frontend/labels/product-question" rel="nofollow">
    current questions here
   </a>
   and contribute your ideas! (E.g. should users be required to enter first/last name, do we need a feature for trial pickups, how do we prevent abuse of powers)
  </span>
 </p>
 <p>
  <span style="color: rgb(0,0,0);">
   <a href="https://yunity.atlassian.net/wiki/display/YUN/Planning" rel="nofollow">
    Planning
   </a>
   the foodsaving tool. Started collecting
   <a href="https://yunity.atlassian.net/wiki/display/YUN/Requirements" rel="nofollow">
    user requirements
   </a>
   in a written way - currently only Taiwan, more hopefully coming soon.
   <br/>
  </span>
 </p>
 <p>
  <span style="color: rgb(0,0,0);">
   <strong>
    Looking for a logo
   </strong>
   ! Need to answer the basic questions:
  </span>
  <em>
   "What is the message we want to communicate? Which emotion do we want to effect?"
   <br/>
  </em>
  Proposals:
 </p>
 <p>
  <span class="confluence-embedded-file-wrapper confluence-embedded-manual-size">
   <span class="confluence-embedded-file-wrapper confluence-embedded-manual-size">
    <span class="confluence-embedded-file-wrapper confluence-embedded-manual-size">
     <img class="confluence-embedded-image confluence-thumbnail" data-base-url="https://yunity.atlassian.net/wiki" data-image-src="https://yunity.atlassian.net/wiki/download/attachments/71761938/save-carrot.png?version=1&amp;modificationDate=1477925762462&amp;cacheVersion=1&amp;api=v2" data-linked-resource-container-id="71761938" data-linked-resource-container-version="2" data-linked-resource-content-type="image/png" data-linked-resource-default-alias="save-carrot.png" data-linked-resource-id="71761939" data-linked-resource-type="attachment" data-linked-resource-version="1" data-unresolved-comment-count="0" height="150" src="https://yunity.atlassian.net/wiki/download/thumbnails/71761938/save-carrot.png?width=108&amp;height=150" srcset="/wiki/download/thumbnails/71761938/save-carrot.png?width=216&amp;height=300 2x, /wiki/download/thumbnails/71761938/save-carrot.png?width=108&amp;height=150 1x"/>
    </span>
   </span>
  </span>
  <span class="confluence-embedded-file-wrapper confluence-embedded-manual-size">
   <span class="confluence-embedded-file-wrapper confluence-embedded-manual-size">
    <span class="confluence-embedded-file-wrapper confluence-embedded-manual-size">
     <img class="confluence-embedded-image confluence-thumbnail" data-base-url="https://yunity.atlassian.net/wiki" data-image-src="https://yunity.atlassian.net/wiki/download/attachments/71761938/fist-the-carrot.png?version=1&amp;modificationDate=1477925762998&amp;cacheVersion=1&amp;api=v2" data-linked-resource-container-id="71761938" data-linked-resource-container-version="2" data-linked-resource-content-type="image/png" data-linked-resource-default-alias="fist-the-carrot.png" data-linked-resource-id="71761940" data-linked-resource-type="attachment" data-linked-resource-version="1" data-unresolved-comment-count="0" height="150" src="https://yunity.atlassian.net/wiki/download/thumbnails/71761938/fist-the-carrot.png?width=170&amp;height=150" srcset="/wiki/download/thumbnails/71761938/fist-the-carrot.png?width=340&amp;height=300 2x, /wiki/download/thumbnails/71761938/fist-the-carrot.png?width=170&amp;height=150 1x"/>
    </span>
   </span>
  </span>
 </p>
 <p>
  <span style="color: rgb(0,0,0);">
   Post your ideas
   <a class="external-link" href="https://github.com/yunity/foodsaving-frontend/issues/110" rel="nofollow">
    in GitHub
   </a>
   or in Slack in
   <a class="external-link" href="https://yunity.slack.com/messages/foodsaving-tool-plan/" rel="nofollow">
    #foodsaving-tool-plan
   </a>
   !
   <br/>
  </span>
 </p>
 <p>
  <span style="color: rgb(0,0,0);">
   <br/>
  </span>
 </p>
 <hr/>
 <h2 id="yunityheartbeat2016-10-30-Foodsavingworldwide.">
  <span style="color: rgb(0,0,0);">
   <strong>
    Foodsaving worldwide.
   </strong>
  </span>
 </h2>
 <h3 id="yunityheartbeat2016-10-30-Done.2">
  <span style="color: rgb(0,0,0);">
   <span style="color: rgb(153,204,0);">
    Done
   </span>
  </span>
 </h3>
 <p>
  <span style="color: rgb(0,0,0);">
   Finally we held a syscon about how to name the FSINT sections on the wiki and on Slack, which resulted in:
   <a class="external-link" href="https://business.konsensieren.eu/en/konsensierung/wyg3c9utr/ergebnis" rel="nofollow">
    Foodsaving worldwide
   </a>
   ! (Hence the shortened title of this paragraph...
   <span class="confluence-embedded-file-wrapper">
    <span class="confluence-embedded-file-wrapper">
     <img alt="(wink)" class="confluence-embedded-image emoticon emoticon-wink confluence-external-resource" data-image-src="https://yunity.atlassian.net/wiki/s/-705042133/6447/63284c861170530db9b4c8001df5e6777c89815a/_/images/icons/emoticons/wink.png" src="https://yunity.atlassian.net/wiki/s/-705042133/6447/63284c861170530db9b4c8001df5e6777c89815a/_/images/icons/emoticons/wink.png"/>
    </span>
   </span>
   )
  </span>
 </p>
 <p>
  <span style="color: rgb(0,0,0);">
   <a class="confluence-userlink user-mention" data-base-url="https://yunity.atlassian.net/wiki" data-linked-resource-id="4227118" data-linked-resource-type="userinfo" data-linked-resource-version="3" data-username="tiltec" href="https://yunity.atlassian.net/wiki/display/~tiltec">
    Tilmann
   </a>
   put the
   <a href="https://yunity.atlassian.net/wiki/display/FSINT/Graphics" rel="nofollow">
    graphics
   </a>
   and drafts for logos on the wiki to make them accessible and editable for anybody interested.
  </span>
 </p>
 <h3 id="yunityheartbeat2016-10-30-InProgress.2">
  <span style="color: rgb(128,128,128);">
   In Progress
  </span>
 </h3>
 <ul>
  <li>
   <span style="color: rgb(0,0,0);">
    getting in contact with people using #foodsharing on twitter (
    <a class="confluence-userlink user-mention" data-base-url="https://yunity.atlassian.net/wiki" data-linked-resource-id="5177885" data-linked-resource-type="userinfo" data-linked-resource-version="2" data-username="Paul Free" href="https://yunity.atlassian.net/wiki/display/~Paul+Free">
     Paul Free
    </a>
    )
   </span>
  </li>
  <li>
   <span style="color: rgb(0,0,0);">
    refining and renaming what used to be called the 'media kit' and is now '
    <a href="https://yunity.atlassian.net/wiki/display/FSINT/Material+to+get+started" rel="nofollow">
     material to get started
    </a>
    ' (
    <a class="confluence-userlink user-mention" data-base-url="https://yunity.atlassian.net/wiki" data-linked-resource-id="4227489" data-linked-resource-type="userinfo" data-linked-resource-version="2" data-username="Janina" href="https://yunity.atlassian.net/wiki/display/~Janina">
     Janina Abels
    </a>
    )
   </span>
  </li>
  <li>
   <span style="color: rgb(0,0,0);">
    creating a new page collecting
    <a href="https://yunity.atlassian.net/wiki/display/FSINT/Existing+platforms" rel="nofollow">
     existing platforms
    </a>
    (
    <a class="confluence-userlink user-mention" data-base-url="https://yunity.atlassian.net/wiki" data-linked-resource-id="4227489" data-linked-resource-type="userinfo" data-linked-resource-version="2" data-username="Janina" href="https://yunity.atlassian.net/wiki/display/~Janina">
     Janina Abels
    </a>
    ,
    <a class="confluence-userlink user-mention" data-base-url="https://yunity.atlassian.net/wiki" data-linked-resource-id="4227118" data-linked-resource-type="userinfo" data-linked-resource-version="3" data-username="tiltec" href="https://yunity.atlassian.net/wiki/display/~tiltec">
     Tilmann
    </a>
    )
    <br/>
   </span>
  </li>
  <li>
   <span style="color: rgb(0,0,0);">
    getting in contact with
    <a class="external-link" href="https://olioex.com/" rel="nofollow">
     OLIO
    </a>
    after they made offers on their app moneyfree (
    <a class="confluence-userlink user-mention" data-base-url="https://yunity.atlassian.net/wiki" data-linked-resource-id="917513" data-linked-resource-type="userinfo" data-linked-resource-version="3" data-username="nicksellen" href="https://yunity.atlassian.net/wiki/display/~nicksellen">
     Nick Sellen
    </a>
    ,
    <a class="confluence-userlink user-mention" data-base-url="https://yunity.atlassian.net/wiki" data-linked-resource-id="4227489" data-linked-resource-type="userinfo" data-linked-resource-version="2" data-username="Janina" href="https://yunity.atlassian.net/wiki/display/~Janina">
     Janina Abels
    </a>
    )
   </span>
  </li>
 </ul>
 <h3 id="yunityheartbeat2016-10-30-Challenges/helpneeded">
  <span style="color: rgb(255,102,0);">
   Challenges/help needed
  </span>
 </h3>
 <ul>
  <li>
   <span style="color: rgb(0,0,0);">
    more feedback and co-creation wanted with regards to the material to get started!
    <strong>
     <br class="_mce_tagged_br"/>
    </strong>
   </span>
  </li>
  <li>
   <span style="color: rgb(255,102,0);">
    <span style="color: rgb(0,0,0);">
     summary of the Russian foodsharing projects visible on
     <a class="external-link" href="http://vk.com/" rel="nofollow">
      vk.com
     </a>
     is still missing
    </span>
   </span>
   <span style="color: rgb(0,0,0);">
    <br/>
   </span>
  </li>
 </ul>
 <p>
  <span style="color: rgb(0,0,0);">
   <br/>
  </span>
 </p>
 <hr/>
 <h2 id="yunityheartbeat2016-10-30-IT-Service.">
  <span style="color: rgb(0,0,0);">
   <strong>
    IT-Service.
   </strong>
  </span>
 </h2>
 <h3 id="yunityheartbeat2016-10-30-Done.3">
  <span style="color: rgb(0,0,0);">
   <span style="color: rgb(153,204,0);">
    Done
   </span>
  </span>
 </h3>
 <ul>
  <li>
   <span style="color: rgb(0,0,0);">
    setting up channels in
    <strong>
     matrix
    </strong>
    (via riot chat) incl. incoming and outgoing webhooks. (from matrix you can chat towards slack and other way around) (
    <a class="confluence-userlink user-mention" data-base-url="https://yunity.atlassian.net/wiki" data-linked-resource-id="4227118" data-linked-resource-type="userinfo" data-linked-resource-version="3" data-username="tiltec" href="https://yunity.atlassian.net/wiki/display/~tiltec">
     Tilmann
    </a>
    ,
    <a class="confluence-userlink user-mention" data-base-url="https://yunity.atlassian.net/wiki" data-linked-resource-id="55017502" data-linked-resource-type="userinfo" data-linked-resource-version="3" data-username="nitram" href="https://yunity.atlassian.net/wiki/display/~nitram">
     Kaiser Mikato
    </a>
    )
    <br/>
   </span>
  </li>
  <li>
   <span style="color: rgb(0,0,0);">
    rocket.chat and slack integration (
    <a class="confluence-userlink user-mention" data-base-url="https://yunity.atlassian.net/wiki" data-linked-resource-id="5177885" data-linked-resource-type="userinfo" data-linked-resource-version="2" data-username="Paul Free" href="https://yunity.atlassian.net/wiki/display/~Paul+Free">
     Paul Free
    </a>
    )
    <br/>
   </span>
  </li>
 </ul>
 <h3 id="yunityheartbeat2016-10-30-InProgress.3">
  <span style="color: rgb(128,128,128);">
   In Progress
  </span>
 </h3>
 <ul>
  <li>
   <span style="color: rgb(128,128,128);">
    <span style="color: rgb(0,0,0);">
     importing slack data into rocket.chat
    </span>
    (
    <a class="confluence-userlink user-mention" data-base-url="https://yunity.atlassian.net/wiki" data-linked-resource-id="5177885" data-linked-resource-type="userinfo" data-linked-resource-version="2" data-username="Paul Free" href="https://yunity.atlassian.net/wiki/display/~Paul+Free">
     Paul Free
    </a>
    )
   </span>
  </li>
  <li>
   <span style="color: rgb(0,0,0);">
    research for hrm programs etc. (
    <a class="confluence-userlink user-mention" data-base-url="https://yunity.atlassian.net/wiki" data-linked-resource-id="917513" data-linked-resource-type="userinfo" data-linked-resource-version="3" data-username="nicksellen" href="https://yunity.atlassian.net/wiki/display/~nicksellen">
     Nick Sellen
    </a>
    ,
    <a class="confluence-userlink user-mention" data-base-url="https://yunity.atlassian.net/wiki" data-linked-resource-id="4227118" data-linked-resource-type="userinfo" data-linked-resource-version="3" data-username="tiltec" href="https://yunity.atlassian.net/wiki/display/~tiltec">
     Tilmann
    </a>
    )
   </span>
  </li>
 </ul>
 <h3 id="yunityheartbeat2016-10-30-Challenges/helpneeded.1">
  <span style="color: rgb(255,102,0);">
   Challenges/help needed
  </span>
 </h3>
 <ul>
  <li>
   <span style="color: rgb(0,0,0);">
    rocket.chat import freezing while doing so
   </span>
  </li>
 </ul>
 <p>
  <br/>
 </p>
 <hr/>
 <h2 id="yunityheartbeat2016-10-30-Structure.">
  <span style="color: rgb(0,0,0);">
   <strong>
    Structure.
   </strong>
  </span>
 </h2>
 <h3 id="yunityheartbeat2016-10-30-Done.4">
  <span style="color: rgb(0,0,0);">
   <span style="color: rgb(153,204,0);">
    Done
   </span>
  </span>
 </h3>
 <ul>
  <li>
   developing a
   <a href="https://yunity.atlassian.net/wiki/display/IDEAS/Improve+yunity+wiki+accessibility" rel="nofollow">
    detailed plan of how to restructure the wiki
   </a>
   using spaces to make it more accessible (
   <a class="confluence-userlink user-mention" data-base-url="https://yunity.atlassian.net/wiki" data-linked-resource-id="4227118" data-linked-resource-type="userinfo" data-linked-resource-version="3" data-username="tiltec" href="https://yunity.atlassian.net/wiki/display/~tiltec">
    Tilmann
   </a>
   ,
   <a class="confluence-userlink user-mention" data-base-url="https://yunity.atlassian.net/wiki" data-linked-resource-id="4227489" data-linked-resource-type="userinfo" data-linked-resource-version="2" data-username="Janina" href="https://yunity.atlassian.net/wiki/display/~Janina">
    Janina Abels
   </a>
   )
  </li>
  <li>
   creating landing page proposals for the new
   <a href="https://yunity.atlassian.net/wiki/display/~Janina/Culture+landing+page" rel="nofollow">
    Culture
   </a>
   and
   <a href="https://yunity.atlassian.net/wiki/display/~Janina/WuppHouse+landing+page" rel="nofollow">
    WuppHouse
   </a>
   wikispaces (
   <a class="confluence-userlink user-mention" data-base-url="https://yunity.atlassian.net/wiki" data-linked-resource-id="4227489" data-linked-resource-type="userinfo" data-linked-resource-version="2" data-username="Janina" href="https://yunity.atlassian.net/wiki/display/~Janina">
    Janina Abels
   </a>
   )
  </li>
 </ul>
 <h3 id="yunityheartbeat2016-10-30-InProgress.4">
  <span style="color: rgb(128,128,128);">
   In Progress
  </span>
 </h3>
 <ul>
  <li>
   <a class="external-link" href="https://douginamug.gitbooks.io/a-systemic-consensus-manual-testing/content/" rel="nofollow">
    writing and thinking
   </a>
   about decision making theory, autonomy etc. (
   <a class="confluence-userlink user-mention" data-base-url="https://yunity.atlassian.net/wiki" data-linked-resource-id="917517" data-linked-resource-type="userinfo" data-linked-resource-version="8" data-username="dmhwebb" href="https://yunity.atlassian.net/wiki/display/~dmhwebb">
    Douglas Webb
   </a>
   )
  </li>
  <li>
   setting up
   <a href="https://yunity.atlassian.net/wiki/display/YUN/Wuppdays+%28%2312%29+Witzenhausen" rel="nofollow">
    WuppDays Witzenhausen
   </a>
   (
   <a class="confluence-userlink user-mention" data-base-url="https://yunity.atlassian.net/wiki" data-linked-resource-id="54198301" data-linked-resource-type="userinfo" data-linked-resource-version="2" data-username="birke" href="https://yunity.atlassian.net/wiki/display/~birke">
    Hans-Christian Eick
   </a>
   ,
   <a class="confluence-userlink user-mention" data-base-url="https://yunity.atlassian.net/wiki" data-linked-resource-id="5177885" data-linked-resource-type="userinfo" data-linked-resource-version="2" data-username="Paul Free" href="https://yunity.atlassian.net/wiki/display/~Paul+Free">
    Paul Free
   </a>
   )
  </li>
  <li>
   discussing project identity based on
   <a href="https://yunity.atlassian.net/wiki/display/IDEAS/Project+identity+-+yunity%2C+foodsharing%2C+sharecy" rel="nofollow">
    an article
   </a>
   written by
   <a class="confluence-userlink user-mention" data-base-url="https://yunity.atlassian.net/wiki" data-linked-resource-id="4227489" data-linked-resource-type="userinfo" data-linked-resource-version="2" data-username="Janina" href="https://yunity.atlassian.net/wiki/display/~Janina">
    Janina Abels
   </a>
   (
   <a class="confluence-userlink user-mention" data-base-url="https://yunity.atlassian.net/wiki" data-linked-resource-id="2162705" data-linked-resource-type="userinfo" data-linked-resource-version="1" data-username="Philip" href="https://yunity.atlassian.net/wiki/display/~Philip">
    Philip Engelbutzeder
   </a>
   ,
   <a class="confluence-userlink user-mention" data-base-url="https://yunity.atlassian.net/wiki" data-linked-resource-id="4227353" data-linked-resource-type="userinfo" data-linked-resource-version="2" data-username="Tais" href="https://yunity.atlassian.net/wiki/display/~Tais">
    Tais Real
   </a>
   ,
   <a class="confluence-userlink user-mention" data-base-url="https://yunity.atlassian.net/wiki" data-linked-resource-id="5177885" data-linked-resource-type="userinfo" data-linked-resource-version="2" data-username="Paul Free" href="https://yunity.atlassian.net/wiki/display/~Paul+Free">
    Paul Free
   </a>
   ,
   <a class="confluence-userlink user-mention" data-base-url="https://yunity.atlassian.net/wiki" data-linked-resource-id="4227118" data-linked-resource-type="userinfo" data-linked-resource-version="3" data-username="tiltec" href="https://yunity.atlassian.net/wiki/display/~tiltec">
    Tilmann
   </a>
   ,
   <a class="confluence-userlink user-mention" data-base-url="https://yunity.atlassian.net/wiki" data-linked-resource-id="2981927" data-linked-resource-type="userinfo" data-linked-resource-version="2" data-username="matthias" href="https://yunity.atlassian.net/wiki/display/~matthias">
    Matthias Larisch
   </a>
   ,
   <a class="confluence-userlink user-mention" data-base-url="https://yunity.atlassian.net/wiki" data-linked-resource-id="4227489" data-linked-resource-type="userinfo" data-linked-resource-version="2" data-username="Janina" href="https://yunity.atlassian.net/wiki/display/~Janina">
    Janina Abels
   </a>
   )
  </li>
  <li>
   started thinking about
   <a class="external-link" href="https://yunity.slack.com/messages/community-guidelines/" rel="nofollow">
    #community-guidelines
   </a>
   and how to handle destructive behaviors (
   <a class="confluence-userlink user-mention" data-base-url="https://yunity.atlassian.net/wiki" data-linked-resource-id="917513" data-linked-resource-type="userinfo" data-linked-resource-version="3" data-username="nicksellen" href="https://yunity.atlassian.net/wiki/display/~nicksellen">
    Nick Sellen
   </a>
   ,
   <a class="confluence-userlink user-mention" data-base-url="https://yunity.atlassian.net/wiki" data-linked-resource-id="4227118" data-linked-resource-type="userinfo" data-linked-resource-version="3" data-username="tiltec" href="https://yunity.atlassian.net/wiki/display/~tiltec">
    Tilmann
   </a>
   )
  </li>
 </ul>
 <h3 id="yunityheartbeat2016-10-30-Challenges/helpneeded.2">
  <span style="color: rgb(255,102,0);">
   Challenges/help needed
  </span>
 </h3>
 <ul>
  <li>
   what does yunity actually signify to its contributors individually?
  </li>
  <li>
   how can we be open to everybody and still protect an atmosphere of trust if we encounter destructive and unreasonable behaviors?
  </li>
 </ul>
 <p>
  <br/>
 </p>
 <hr/>
 <h2 id="yunityheartbeat2016-10-30-WuppHouse.">
  <strong>
   WuppHouse.
  </strong>
 </h2>
 <h3 id="yunityheartbeat2016-10-30-Done.5">
  <span style="color: rgb(0,0,0);">
   <span style="color: rgb(153,204,0);">
    Done
   </span>
  </span>
 </h3>
 <ul>
  <li>
   <span style="color: rgb(0,0,0);">
    <a href="https://yunity.atlassian.net/wiki/display/YUN/2016-10-19+Conference+call+with+Bernd+of+the+Gemeinschaftsstifter+project" rel="nofollow">
     conference call with Bernd
    </a>
    from Gemeinschaftsstifter (
    <a class="confluence-userlink user-mention" data-base-url="https://yunity.atlassian.net/wiki" data-linked-resource-id="4227125" data-linked-resource-type="userinfo" data-linked-resource-version="2" data-username="Bodhi" href="https://yunity.atlassian.net/wiki/display/~Bodhi">
     Bodhi Neiser
    </a>
    ,
    <a class="confluence-userlink user-mention" data-base-url="https://yunity.atlassian.net/wiki" data-linked-resource-id="2981927" data-linked-resource-type="userinfo" data-linked-resource-version="2" data-username="matthias" href="https://yunity.atlassian.net/wiki/display/~matthias">
     Matthias Larisch
    </a>
    ,
    <a class="confluence-userlink user-mention" data-base-url="https://yunity.atlassian.net/wiki" data-linked-resource-id="6553696" data-linked-resource-type="userinfo" data-linked-resource-version="2" data-username="Arno" href="https://yunity.atlassian.net/wiki/display/~Arno">
     Arno Döpper
    </a>
    )
   </span>
  </li>
  <li>
   <span style="color: rgb(0,0,0);">
    visited
    <a class="external-link" href="http://www.kubiz-wallenberg.de/" rel="nofollow">
     Freiraum in Berlin Weissensee
    </a>
    (
    <a class="confluence-userlink user-mention" data-base-url="https://yunity.atlassian.net/wiki" data-linked-resource-id="2162705" data-linked-resource-type="userinfo" data-linked-resource-version="1" data-username="Philip" href="https://yunity.atlassian.net/wiki/display/~Philip">
     Philip Engelbutzeder
    </a>
    ,
    <a class="confluence-userlink user-mention" data-base-url="https://yunity.atlassian.net/wiki" data-linked-resource-id="6553694" data-linked-resource-type="userinfo" data-linked-resource-version="1" data-username="syrt" href="https://yunity.atlassian.net/wiki/display/~syrt">
     Axel Kalitzki
    </a>
    ,
    <a class="confluence-userlink user-mention" data-base-url="https://yunity.atlassian.net/wiki" data-linked-resource-id="5177885" data-linked-resource-type="userinfo" data-linked-resource-version="2" data-username="Paul Free" href="https://yunity.atlassian.net/wiki/display/~Paul+Free">
     Paul Free
    </a>
    ,
    <a class="confluence-userlink user-mention" data-base-url="https://yunity.atlassian.net/wiki" data-linked-resource-id="65995188" data-linked-resource-type="userinfo" data-linked-resource-version="1" data-username="piersonkatia" href="https://yunity.atlassian.net/wiki/display/~piersonkatia">
     Katia
    </a>
    , ...)
   </span>
  </li>
 </ul>
 <h3 id="yunityheartbeat2016-10-30-InProgress.5">
  <span style="color: rgb(128,128,128);">
   In Progress
  </span>
 </h3>
 <ul>
  <li>
   <span style="color: rgb(0,0,0);">
    analyzing Mietshäusersyndikat principle and formal paper (
    <a class="confluence-userlink user-mention" data-base-url="https://yunity.atlassian.net/wiki" data-linked-resource-id="4227125" data-linked-resource-type="userinfo" data-linked-resource-version="2" data-username="Bodhi" href="https://yunity.atlassian.net/wiki/display/~Bodhi">
     Bodhi Neiser
    </a>
    )
   </span>
  </li>
 </ul>
 <h3 id="yunityheartbeat2016-10-30-Challenges/helpneeded.3">
  <span style="color: rgb(255,102,0);">
   Challenges/help needed
  </span>
 </h3>
 <ul>
  <li>
   <span style="color: rgb(0,0,0);">
    finding the right building
   </span>
  </li>
  <li>
   <span style="color: rgb(0,0,0);">
    finding the right legal setup
   </span>
  </li>
  <li>
   <span style="color: rgb(0,0,0);">
    developing a clear concept of how to live together in a WuppHouse
   </span>
  </li>
 </ul>
 <p>
  <span style="color: rgb(0,0,0);">
   <br/>
  </span>
 </p>
 <hr/>
 <h2 id="yunityheartbeat2016-10-30-Translation.">
  <span style="color: rgb(0,0,0);">
   <strong>
    Translation.
   </strong>
  </span>
 </h2>
 <h3 id="yunityheartbeat2016-10-30-Done.6">
  <span style="color: rgb(0,0,0);">
   <span style="color: rgb(153,204,0);">
    Done
   </span>
  </span>
 </h3>
 <ul>
  <li>
   <span style="color: rgb(0,0,0);">
    <a class="external-link" href="https://devblog.foodsharing.de/index.en.html" rel="nofollow">
     foodsharing devblog
    </a>
    translation via
    <a class="external-link" href="https://gitlab.com/foodsharing-dev/foodsharing-dev.gitlab.io/issues" rel="nofollow">
     gitlab
    </a>
    (
    <a class="confluence-userlink user-mention" data-base-url="https://yunity.atlassian.net/wiki" data-linked-resource-id="65241092" data-linked-resource-type="userinfo" data-linked-resource-version="2" data-username="fenja.jacobs" href="https://yunity.atlassian.net/wiki/display/~fenja.jacobs">
     Fenja Jacobs
    </a>
    )
   </span>
  </li>
  <li>
   <span style="color: rgb(0,0,0);">
    <a href="https://yunity.atlassian.net/wiki/display/YUN/Foodsharing+Devblog+Translation" rel="nofollow">
     foodsharing devblog translation instructions
    </a>
    (
    <a class="confluence-userlink user-mention" data-base-url="https://yunity.atlassian.net/wiki" data-linked-resource-id="4227118" data-linked-resource-type="userinfo" data-linked-resource-version="3" data-username="tiltec" href="https://yunity.atlassian.net/wiki/display/~tiltec">
     Tilmann
    </a>
    ,
    <a class="confluence-userlink user-mention" data-base-url="https://yunity.atlassian.net/wiki" data-linked-resource-id="4227489" data-linked-resource-type="userinfo" data-linked-resource-version="2" data-username="Janina" href="https://yunity.atlassian.net/wiki/display/~Janina">
     Janina Abels
    </a>
    )
   </span>
  </li>
 </ul>
 <h3 id="yunityheartbeat2016-10-30-InProgress.6">
  <span style="color: rgb(128,128,128);">
   In Progress
  </span>
 </h3>
 <ul>
  <li>
   foodsharing devblog translation via
   <a class="external-link" href="https://gitlab.com/foodsharing-dev/foodsharing-dev.gitlab.io/issues" rel="nofollow">
    gitlab
   </a>
   (everybody can just work on an issue...
   <span class="confluence-embedded-file-wrapper">
    <span class="confluence-embedded-file-wrapper">
     <img alt="(smile)" class="confluence-embedded-image emoticon emoticon-smile confluence-external-resource" data-image-src="https://yunity.atlassian.net/wiki/s/-786372947/6447/203c3decc339c304a74825a259bc1ed08d500c07/_/images/icons/emoticons/smile.png" src="https://yunity.atlassian.net/wiki/s/-786372947/6447/203c3decc339c304a74825a259bc1ed08d500c07/_/images/icons/emoticons/smile.png"/>
    </span>
   </span>
   )
  </li>
  <li>
   translation of the first strings of the foodsaving tool via
   <a class="external-link" href="https://www.transifex.com/yunity-1/foodsaving-tool/dashboard/" rel="nofollow">
    transifex
   </a>
   (
   <a class="confluence-userlink user-mention" data-base-url="https://yunity.atlassian.net/wiki" data-linked-resource-id="4227118" data-linked-resource-type="userinfo" data-linked-resource-version="3" data-username="tiltec" href="https://yunity.atlassian.net/wiki/display/~tiltec">
    Tilmann
   </a>
   ,
   <a class="confluence-userlink user-mention" data-base-url="https://yunity.atlassian.net/wiki" data-linked-resource-id="4227489" data-linked-resource-type="userinfo" data-linked-resource-version="2" data-username="Janina" href="https://yunity.atlassian.net/wiki/display/~Janina">
    Janina Abels
   </a>
   )
  </li>
 </ul>
 <h3 id="yunityheartbeat2016-10-30-Challenges/helpneeded.4">
  <span style="color: rgb(255,102,0);">
   Challenges/help needed
  </span>
 </h3>
 <ul>
  <li>
   <span style="color: rgb(0,0,0);">
    French translation of the foodsharing devblog issued on gitlab
   </span>
  </li>
 </ul>
 <p>
  <span style="color: rgb(0,0,0);">
   <br/>
  </span>
 </p>
 <hr/>
 <h2 id="yunityheartbeat2016-10-30-PublicRelations.">
  <span style="color: rgb(0,0,0);">
   <strong>
    Public Relations.
   </strong>
  </span>
 </h2>
 <h3 id="yunityheartbeat2016-10-30-Done.7">
  <span style="color: rgb(0,0,0);">
   <span style="color: rgb(153,204,0);">
    Done
   </span>
  </span>
 </h3>
 <ul>
  <li>
   <span style="color: rgb(0,0,0);">
    contact with nomadbase (
    <a class="confluence-userlink user-mention" data-base-url="https://yunity.atlassian.net/wiki" data-linked-resource-id="2162705" data-linked-resource-type="userinfo" data-linked-resource-version="1" data-username="Philip" href="https://yunity.atlassian.net/wiki/display/~Philip">
     Philip Engelbutzeder
    </a>
    )
   </span>
  </li>
  <li>
   <span style="color: rgb(0,0,0);">
    workshop in Bern about yunity with (Felix,
    <a class="confluence-userlink user-mention" data-base-url="https://yunity.atlassian.net/wiki" data-linked-resource-id="65995188" data-linked-resource-type="userinfo" data-linked-resource-version="1" data-username="piersonkatia" href="https://yunity.atlassian.net/wiki/display/~piersonkatia">
     Katia
    </a>
    ,
    <a class="confluence-userlink user-mention" data-base-url="https://yunity.atlassian.net/wiki" data-linked-resource-id="31391745" data-linked-resource-type="userinfo" data-linked-resource-version="1" data-username="fritz" href="https://yunity.atlassian.net/wiki/display/~fritz">
     fritz holscher
    </a>
    ,
    <a class="confluence-userlink user-mention" data-base-url="https://yunity.atlassian.net/wiki" data-linked-resource-id="6553696" data-linked-resource-type="userinfo" data-linked-resource-version="2" data-username="Arno" href="https://yunity.atlassian.net/wiki/display/~Arno">
     Arno Döpper
    </a>
    )
   </span>
  </li>
  <li>
   <span style="color: rgb(128,128,128);">
    <span style="color: rgb(0,0,0);">
     brochure and flyer for yunity inspired by
     <a class="external-link" href="http://crimethinc.com/tce/" rel="nofollow">
      <span style="color: rgb(0,0,0);">
       http://crimethinc.com/tce/
      </span>
     </a>
     and glocal yunity dreaming sessions (
    </span>
    <span style="color: rgb(0,0,0);">
     <a class="confluence-userlink user-mention" data-base-url="https://yunity.atlassian.net/wiki" data-linked-resource-id="2162705" data-linked-resource-type="userinfo" data-linked-resource-version="1" data-username="Philip" href="https://yunity.atlassian.net/wiki/display/~Philip">
      Philip Engelbutzeder
     </a>
     ,
    </span>
    <span style="color: rgb(0,0,0);">
     <a class="confluence-userlink user-mention" data-base-url="https://yunity.atlassian.net/wiki" data-linked-resource-id="5177885" data-linked-resource-type="userinfo" data-linked-resource-version="2" data-username="Paul Free" href="https://yunity.atlassian.net/wiki/display/~Paul+Free">
      Paul Free
     </a>
     )
    </span>
   </span>
  </li>
  <li>
   <span style="color: rgb(0,0,0);">
    lonly warriors in
    <a class="external-link" href="https://www.reddit.com/r/yunity/" rel="nofollow">
     reddit/yunity
    </a>
    (
    <a class="confluence-userlink user-mention" data-base-url="https://yunity.atlassian.net/wiki" data-linked-resource-id="6553696" data-linked-resource-type="userinfo" data-linked-resource-version="2" data-username="Arno" href="https://yunity.atlassian.net/wiki/display/~Arno">
     Arno Döpper
    </a>
    ,
    <a class="confluence-userlink user-mention" data-base-url="https://yunity.atlassian.net/wiki" data-linked-resource-id="5177885" data-linked-resource-type="userinfo" data-linked-resource-version="2" data-username="Paul Free" href="https://yunity.atlassian.net/wiki/display/~Paul+Free">
     Paul Free
    </a>
    ,
    <a class="confluence-userlink user-mention" data-base-url="https://yunity.atlassian.net/wiki" data-linked-resource-id="4227118" data-linked-resource-type="userinfo" data-linked-resource-version="3" data-username="tiltec" href="https://yunity.atlassian.net/wiki/display/~tiltec">
     Tilmann
    </a>
    )
   </span>
  </li>
  <li>
   <span style="color: rgb(0,0,0);">
    Key Note at the Stipendiaten machen Programm: Wirtschaftsmacht Europa ? (Studienstiftung des deutschen Volkes) - Thema: Selbstbestimmung, Vertrauen und Kollaboration als Grundpfeiler des europäischen Wirtschaftsmacht aus dem Blickwinkel der Gift Economy (
    <a class="confluence-userlink user-mention" data-base-url="https://yunity.atlassian.net/wiki" data-linked-resource-id="2162705" data-linked-resource-type="userinfo" data-linked-resource-version="1" data-username="Philip" href="https://yunity.atlassian.net/wiki/display/~Philip">
     Philip Engelbutzeder
    </a>
    )
   </span>
  </li>
 </ul>
 <h3 id="yunityheartbeat2016-10-30-Challenges/helpneeded.5">
  <span style="color: rgb(255,102,0);">
   Challenges/help needed
  </span>
 </h3>
 <ul>
  <li>
   <span style="color: rgb(255,102,0);">
    <span style="color: rgb(0,0,0);">
     do we want to paper print? (by
     <a class="confluence-userlink user-mention" data-base-url="https://yunity.atlassian.net/wiki" data-linked-resource-id="65995188" data-linked-resource-type="userinfo" data-linked-resource-version="1" data-username="piersonkatia" href="https://yunity.atlassian.net/wiki/display/~piersonkatia">
      Katia
     </a>
     )
    </span>
   </span>
  </li>
 </ul>
 <p>
  <span style="color: rgb(255,102,0);">
   <span style="color: rgb(0,0,0);">
    <br/>
   </span>
  </span>
 </p>
 <hr/>
 <h2 id="yunityheartbeat2016-10-30-CommunityRelations.">
  <span style="color: rgb(0,0,0);">
   <strong>
    Community Relations.
   </strong>
  </span>
 </h2>
 <h3 id="yunityheartbeat2016-10-30-InProgress.7">
  <span style="color: rgb(128,128,128);">
   In Progress
  </span>
 </h3>
 <ul>
  <li>
   <span style="color: rgb(0,0,0);">
    reflecting on communication culture (especially within Slack) (
    <a class="confluence-userlink user-mention" data-base-url="https://yunity.atlassian.net/wiki" data-linked-resource-id="917513" data-linked-resource-type="userinfo" data-linked-resource-version="3" data-username="nicksellen" href="https://yunity.atlassian.net/wiki/display/~nicksellen">
     Nick Sellen
    </a>
    ,
    <a class="confluence-userlink user-mention" data-base-url="https://yunity.atlassian.net/wiki" data-linked-resource-id="2162705" data-linked-resource-type="userinfo" data-linked-resource-version="1" data-username="Philip" href="https://yunity.atlassian.net/wiki/display/~Philip">
     Philip Engelbutzeder
    </a>
    ,
    <a class="confluence-userlink user-mention" data-base-url="https://yunity.atlassian.net/wiki" data-linked-resource-id="5177885" data-linked-resource-type="userinfo" data-linked-resource-version="2" data-username="Paul Free" href="https://yunity.atlassian.net/wiki/display/~Paul+Free">
     Paul Free
    </a>
    ,
    <a class="confluence-userlink user-mention" data-base-url="https://yunity.atlassian.net/wiki" data-linked-resource-id="55017502" data-linked-resource-type="userinfo" data-linked-resource-version="3" data-username="nitram" href="https://yunity.atlassian.net/wiki/display/~nitram">
     Kaiser Mikato
    </a>
    )
    <br/>
   </span>
  </li>
  <li>
   <span style="color: rgb(0,0,0);">
    connecting to ecobytes and transformap during WuppDays Witzenhausen
   </span>
  </li>
  <li>
   <span style="color: rgb(0,0,0);">
    visiting and experiencing
    <a class="external-link" href="http://www.projektwerkstatt.de/pwerk/saasen.html" rel="nofollow">
     Projekt Werkstatt Saasen
    </a>
   </span>
   (
   <a class="confluence-userlink user-mention" data-base-url="https://yunity.atlassian.net/wiki" data-linked-resource-id="917517" data-linked-resource-type="userinfo" data-linked-resource-version="8" data-username="dmhwebb" href="https://yunity.atlassian.net/wiki/display/~dmhwebb">
    Douglas Webb
   </a>
   ,
   <a class="confluence-userlink user-mention" data-base-url="https://yunity.atlassian.net/wiki" data-linked-resource-id="12222465" data-linked-resource-type="userinfo" data-linked-resource-version="3" data-username="inflector" href="https://yunity.atlassian.net/wiki/display/~inflector">
    Zed Redstone
   </a>
   ,
   <a class="confluence-userlink user-mention" data-base-url="https://yunity.atlassian.net/wiki" data-linked-resource-id="30572615" data-linked-resource-type="userinfo" data-linked-resource-version="3" data-username="Selina" href="https://yunity.atlassian.net/wiki/display/~Selina">
    Selina Camile
   </a>
   ,
   <a class="confluence-userlink user-mention" data-base-url="https://yunity.atlassian.net/wiki" data-linked-resource-id="62554274" data-linked-resource-type="userinfo" data-linked-resource-version="4" data-username="rose earthling" href="https://yunity.atlassian.net/wiki/display/~rose+earthling">
    Lara Earthling
   </a>
   ,
   <a class="confluence-userlink user-mention" data-base-url="https://yunity.atlassian.net/wiki" data-linked-resource-id="54198301" data-linked-resource-type="userinfo" data-linked-resource-version="2" data-username="birke" href="https://yunity.atlassian.net/wiki/display/~birke">
    Hans-Christian Eick
   </a>
   ,
   <a class="confluence-userlink user-mention" data-base-url="https://yunity.atlassian.net/wiki" data-linked-resource-id="5177885" data-linked-resource-type="userinfo" data-linked-resource-version="2" data-username="Paul Free" href="https://yunity.atlassian.net/wiki/display/~Paul+Free">
    Paul Free
   </a>
   ,
   <a class="confluence-userlink user-mention" data-base-url="https://yunity.atlassian.net/wiki" data-linked-resource-id="4227125" data-linked-resource-type="userinfo" data-linked-resource-version="2" data-username="Bodhi" href="https://yunity.atlassian.net/wiki/display/~Bodhi">
    Bodhi Neiser
   </a>
   ....)
  </li>
  <li>
   <span style="color: rgb(0,0,0);">
    new people signing up on our different communication channels constantly!
    <img alt="(big grin)" border="0" class="emoticon emoticon-laugh" src="https://yunity.atlassian.net/wiki/s/-705042133/6447/63284c861170530db9b4c8001df5e6777c89815a/_/images/icons/emoticons/biggrin.png" title="(big grin)"/>
   </span>
  </li>
 </ul>
 <p>
  <br/>
 </p>
 <hr/>
 <h2 id="yunityheartbeat2016-10-30-FutureWuppDays.">
  <strong>
   Future WuppDays.
  </strong>
 </h2>
 <h3 id="yunityheartbeat2016-10-30-InProgress.8">
  <span style="color: rgb(128,128,128);">
   In Progress
  </span>
 </h3>
 <ul>
  <li>
   <span style="color: rgb(0,0,0);">
    looking for a WuppSpace in Austria, close to Vienna (
    <a class="confluence-userlink user-mention" data-base-url="https://yunity.atlassian.net/wiki" data-linked-resource-id="32440366" data-linked-resource-type="userinfo" data-linked-resource-version="2" data-username="Chrisi" href="https://yunity.atlassian.net/wiki/display/~Chrisi">
     Chrisi
    </a>
    )
   </span>
  </li>
 </ul>
</div>

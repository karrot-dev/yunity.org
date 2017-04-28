---
title: "Developing from scratch"
date: "2015-10-03"
continue_link: true
taxonomy:
    category: blog
    tag: [development, old blog]
---
    

Ciao techies!

**TL:DR;** We are creating a global platform to share and save food, items, skills and resources using [AngularJS](https://angularjs.org/), [Bootstrap](http://getbootstrap.com/), [Django](https://www.djangoproject.com/),  [Elastic](https://www.elastic.co/) and [PostgreSQL](http://www.postgresql.org/)! Interested? Sign-up [here](http://project.yunity.org/join-the-team).

[WuppDays](http://wuppdays.foodsharing.de/) has so far been excellent. We are lucky to be hosted in a beautiful house in Malo, Italy where we've been dreaming, planning, celebrating and now a lot of doing. Here are some of our Macs and Thinkpads playing nicely with each other:

![](MALO_laptops.jpg)
    
A provisional name for the project is ['Yunity'](http://www.yunity.org/) - final name to be decided shortly. For the development team it's been overwhelmingly positive despite a a challenging start: At first it was decided to start writing a new platform, but a review of the existing PHP code-base for food-sharing led to a discussion about whether the time and resources at WuppDays would be better spent refactoring the existing code-base, or rewriting from scratch.

Points for refactoring included;
<ul> 
    <li>Large, used and usable code-base </li>
    <li><i>"Better to know your enemies [and fix them]"</i></li>
    <li>Current development team familiar with PHP and existing code-base</li>
    <li>More rapid improvements for existing foodsharing community in Germany</li>
</ul>
    
Points for rewriting included;
<ul>
    <li>Moving away from PHP has benefits (easier security, cleaner code)</li>
    <li>Refactoring could take a long time</li>
    <li>Starting from scratch could produce a clearer and better designed platform</li>
</ul>
    
In the end, a vote by [systemic consensus](http://systemicconsensus.blogspot.it/) decided in favour of rewriting over refactoring. A discussion of the potential options considered maintainability, security, extensibility, scalability and how enjoyable the project would be to contribute to. This led to the selection of;

<ul>
    <li><b>Front-end:</b><a href="https://angularjs.org/"> AngularJS</a> and <a href="http://getbootstrap.com/"> Bootstrap</a></li> 
    <li><b>Back-end:</b><a href="https://www.djangoproject.com/"> Django</a> (Python3) and <a href="https://www.elastic.co/"> Elastic</a></li>
    <li><b>Database:</b><a href="http://www.postgresql.org/"> PostgreSQL</a></li>
</ul>

Currently the development team are not prepared for remote developers - but we are working on it and will need people soon, so please get in touch if you are at all interested in getting involved! We have a sign-up form [here](http://wuppdays.foodsharing.de/#signupform). You can see what we're up to on our [yunity GitHub repository](https://github.com/yunity) and on our Waffle task boards for [yunity-core](https://waffle.io/yunity/yunity-core), [yunity-webapp](https://waffle.io/yunity/yunity-webapp) and [yunity-webbapp-mobile](https://waffle.io/yunity/yunity-webapp-mobile).

Best,<br>
WuppDevs x.
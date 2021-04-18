---
title: Developers
route: developers
menu: Developers
image: 'somecode.png'
---

# Developers

> An overview of the different software projects we work on and how to get involved

## The projects

### [foodsharing.de](https://foodsharing.de)

Helps over 150 thousand people to save and share food.

Made up of 3 codebases/projects:

#### Main site

The php app that powers [foodsharing.de](https://foodsharing.de).

**Code**: [gitlab.com/foodsharing-dev/foodsharing](https://gitlab.com/foodsharing-dev/foodsharing)
(ask in [#foodsharing-dev](https://slackin.yunity.org) for access)<br>
**Tech**: PHP / MySQL<br>
**Get involved**: join _#foodsharing-dev_ channel in [slack](https://slackin.yunity.org/)

#### New mobile-first frontend

A mobile-first frontend focused on the tasks you need to do _now_ -
e.g. see your next pickups, reply to messages, and contact the other people doing a pickup with you.

See [our writeup](https://devblog.foodsharing.de/2017/04/18/easter-foodsharing-hackathon.html) from the hackathon for details and screenshots.

**Code**: [github.com/foodsharing-dev/foodsharing-light](https://github.com/foodsharing-dev/foodsharing-light)<br>
**Tech**: ES6 / [Vue.js](https://vuejs.org/) / [Quasar](http://quasar-framework.org/)<br>
**Beta deployment**: [beta.light.foodsharing.de](https://beta.light.foodsharing.de)<br>
**Get involved**: join _#foodsharing-dev_ channel in [slack](https://slackin.yunity.org/)

#### Django API

A Django RESTful API that is the backend for the mobile-first frontend.

**Code**: [github.com/foodsharing-dev/foodsharing-django-api](https://github.com/foodsharing-dev/foodsharing-django-api)<br>
**Tech**: Python 3 / [Django](https://www.djangoproject.com/) / [Django REST Framework](http://www.django-rest-framework.org/)<br>
**Beta deployment**: [beta.light.foodsharing.de/docs/](https://beta.light.foodsharing.de/docs/) (swagger ui)<br>
**Get involved**: join _#foodsharing-dev_ channel in [slack](https://slackin.yunity.org/)

(note: _originally we built it as a php/Symfony app, but switched to Django later_)

### foodsaving tool

A new softwate platform to help foodsaving communities worldwide schedule food pickups. Currently being used by [a team in Gothenburg](https://foodsaving.today/en/blog/2017/04/27/foodsharing-gothenburg-part3), translated into 8+ languages.

It's a python + django-rest-framework API backend with an AngularJS frontend built using [Angular Material](https://material.angularjs.org/).

This summer (2017) it's in the [Rails Girls Summer of Code](https://teams.railsgirlssummerofcode.org/projects/129-foodsaving-and-foodsharing) programme.

**Code**: [github.com/yunity/foodsaving-frontend](https://github.com/yunity/foodsaving-frontend/) / [github.com/yunity/foodsaving-backend](https://github.com/yunity/foodsaving-backend/)<br>
**Tech**: Python 3 / [Django](https://www.djangoproject.com/) / [Django REST Framework](http://www.django-rest-framework.org/)<br>
**Get involved**: join _#foodsaving-tool_ channel in [slack](https://slackin.yunity.org/)<br>
**Main deployment**: [foodsaving.world](https://foodsaving.world)<br>
**Dev deployment**: [dev.foodsaving.world](https://dev.foodsaving.world)

## FAQ

### Why are there multiple projects?

You might wonder why we are building the foodsaving tool
when [foodsharing.de](https://foodsharing.de) already exists.

There are a few reasons why [foodsharing.de](https://foodsharing.de) cannot be used in some cases:
* it has a lot of features that may not be needed by new/smaller communities
* the codebase is hard to work with, so progress is slow and limited in scope
* it is not currently open source - we are [working on it](https://gitlab.com/foodsharing-dev/issues0/milestones/2) though :)
* the foodsharing organisation does not want legal responsibly for communities outside Germany, Austria, Switzerland

This is where the foodsaving tool comes in:
* modern well tested codebase (~98%)
* open source
* other communities can deploy it themselves (or use our hosted version)
* it is new and small and does not have to worry about the issues that come with a much larger organisation

### Why can't foodsharing.de use the foodsaving tool software?

The [foodsharing.de](https://foodsharing.de) users actually use the extra features :)

The organisation (of 150+ thousand users, or 25+ thousand more active users) rely on
the current operation of the site.

The foodsaving tool is not a clone of foodsharing.de, it has some of the same features, but
will probably never support all the features that foodsharing.de has.

As long as [foodsharing.de](https://foodsharing.de) has users it is worth maintaining.

### I thought _yunity_ was a piece of software?

This was the original plan actually, you can [view the original invitation video](https://www.youtube.com/watch?v=kTh24fueZNI).

It was planned that it would replace foodsharing.de with a new internationalized platform that would save/share not just food, but all kinds of items.

The goal turned out to be too big, and over the course of 2 years, yunity has morphed into a network of people/projects.

Some of the main people behind foodsharing.de and yunity (Raphael Fellmer, and Martin Schott) are now persuing their goals of _saving all the food_ with their latest project [SirPlus](https://sirplus.de).

**There is no yunity software!**

### What is the relationship between yunity and foodsharing.de?

There is no formal connection, just the people that work on the foodsharing.de
software are part of the yunity network.

In practical terms it means using some of the available/shared resources/people:
* the [yunity slack](https://slackin.yunity.org) for communication
* space and organisation for hackathons
* knowledge and wisdom shared across the projects

### What is foodsaving.world compared to the foodsaving tool?

The software is called **foodsaving tool** (or **fstool** for short),
the main site that is running the software is [foodsaving.world](https://foodsaving.world) -
this is a deployment that we manage so people can use the software without having to setup a server.

Self hosting is another option available for people who can manage a server.
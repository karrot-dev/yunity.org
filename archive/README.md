# archive

Create a static web archive of the yunity.org site.
The version of grav is too old for php 8, and upgrading caused template issues.
These tools should build you a static archive!

When you run the script it'll:
- build a docker image based on php 7
- install the required php extensions
- run a container
- install the grav dependencies
- run the php web server
- run wget --mirror to archive the content
- fix a few things with grep and sed
- stop the docker container

You'll need:
- docker runner
- wget on your local system
- grep and sed on your local system

That should be enough...

Run this from the project root, not this directory:

```bash
./archive/create
```

Then in `archive/out/localhost:8765` should be your site!

If you have caddy installed you can try it out with:

```bash
caddy run
```

Which will listen on http://localhost:9090

**Note**: it requires a webserver config that can serve up blah.html when you request blah

Assuming you have sufficient access, you can deploy it with:

```bash
./archive/deploy
```

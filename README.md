[![Stories in Ready](https://badge.waffle.io/torrenegra/ekratia.png?label=ready&title=Ready)](https://waffle.io/torrenegra/ekratia)
# ekratia
Ekratia is a new way of making democracy. Members of Ekratia use the Internet to vote directly for new ideas and laws. In case they are too busy to vote, members can delegate their vote to other members. Members can change their delegates on real time.

This is the GitHub repository of Ekratia. To learn more about the technical details of the platform, [view the technical readme](technical_readme.rst).

To learn more about Ekratia in general, visit [Ekratia.org](http://www.ekratia.org/).


## Gulp

The main tasks are:
``
gulp dev
``
This enables the watcher and complies js, scss. We are using browsersync with a proxy pointing to the Django at 0.0.0.0:8000


### Known issues

If you are getting errors like this:
``
events.js:85
      throw er; // Unhandled 'error' event
            ^
Error: watch ENOSPC
    at exports._errnoException (util.js:746:11)
    at FSWatcher.start (fs.js:1172:11)
    at Object.fs.watch (fs.js:1198:11)
    at createFsWatchInstance (/home/user/ekratia/node_modules/watchify/node_modules/chokidar/lib/nodefs-handler.js:24:15)
    at setFsWatchListener (/home/user/ekratia/node_modules/watchify/node_modules/chokidar/lib/nodefs-handler.js:47:19)
    at EventEmitter.NodeFsHandler._watchWithNodeFs (/home/user/ekratia/node_modules/watchify/node_modules/chokidar/lib/nodefs-handler.js:177:15)
    at EventEmitter.NodeFsHandler._handleFile (/home/user/ekratia/node_modules/watchify/node_modules/chokidar/lib/nodefs-handler.js:201:8)
    at EventEmitter.<anonymous> (/home/user/ekratia/node_modules/watchify/node_modules/chokidar/lib/nodefs-handler.js:353:12)
    at FSReqWrap.oncomplete (fs.js:95:15)

``
The command below solved this

``
echo fs.inotify.max_user_watches=524288 | sudo tee -a /etc/sysctl.conf && sudo sysctl -p
``
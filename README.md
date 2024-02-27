# meme_flask

**Meme Generator Website**

Meme Generator is a web application that displays a fresh meme image from Reddit automatically every 12 seconds.

→ Preview

![meme_generator.gif](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExcXlkdnVwemZpNjhiMzkxdTE2bmk4MHQ3NGZnMTJhYXRhd2U3NWN2dyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/rHgxJx7Z30vpOzDMHk/giphy.gif)

- It was coded on Python using Flask web framework. It’s a code that consumes this API ([Meme_Api](https://github.com/D3vd/Meme_Api)), gets the image from the JSON file obtained and provides it to a simple .html page using *render_template* library.

- It was done by following the tutorial from NetworkChuck - [make a WEBSITE with PYTHON!! (Flask Tutorial for Beginners)](https://learn.networkchuck.com/courses/take/ad-free-youtube-videos/lessons/38016146-make-a-website-with-python-flask-tutorial-for-beginners)

-It is set to refresh at every 12 seconds, but this can be changed on the .html refresh line:
<meta http-equiv="refresh" content="**12**”;>
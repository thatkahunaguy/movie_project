# [Movie Trailer Website Project](https://docs.google.com/document/d/1joDQNQl_4icYYm6tM_F9ch5hZEH_f157hlljSUGOLWs/pub?embedded=true)

This is an initial project creating a movie trailer website with python.  I created a movie class which stores a movie's title, storyline, trailer url, and poster art url and added 6 examples of favorite movies to the project.  Utilizing a slightly modified version of the provided fresh_tomatoes.py, an html page is generated with the poster art & titles. Hovering over the art provides the storyline summary above the art.  Clicking the art shows the trailer.



## Table of contents

* [Quick start](#quick-start)
* [Bugs and feature requests](#bugs-and-feature-requests)
* [Documentation](#documentation)
* [Contributing](#contributing)
* [Community](#community)
* [Versioning](#versioning)
* [Creators](#creators)
* [Copyright and license](#copyright-and-license)


## Quick start

To get started:

* Clone the repo: `git clone https://github.com/thatkahunaguy/movie_project.git`.
* This project requires python 2.7
* Run entertainment_center.py
* The file fresh_tomatoes.html will be generated/re-generated and open a browser window to display

### What's included

Within the download you'll find the following directories and files. You'll see the folowing:

```
movie_project/
├── entertainment_center.py   *run this to generate the html output*
├── fresh_tomatoes.py         *this  file generates the html output*
├── media.py                  *this file contains the movie instances*
├── fresh_tomatoes.html       *this is the output html*
├── README.md
```



## Bugs and feature requests
Note that the provided fresh_tomatoes.py was modified to show movie storylines on hover and to conform to the [google style guide section below](https://google.github.io/styleguide/pyguide.html?showone=Strings#Strings):
```
Avoid using the + and += operators to accumulate a string within a loop. Since strings are immutable, this creates unnecessary temporary objects and results in quadratic rather than linear running time. Instead, add each substring to a list and ''.join the list after the loop terminates (or, write each substring to a io.BytesIO buffer).
```
Have a bug or a feature request? Let me know.

## Documentation

This is the whole enchilada!

## Contributing

Sorry, only independent and web search work allowed at this point!

## Community

* Udacity discussions are [here](https://discussions.udacity.com/t/movie-website-mini-project-fs-feb/959).


## Versioning

Debut release

## Creators

**John Glancy**

* <https://github.com/thatkahunaguy>

**Udacity**
* <https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004>

## Copyright and license

Code released under [the MIT license](https://opensource.org/licenses/MIT). Docs released under [Creative Commons](http://creativecommons.org/licenses/by/4.0/).



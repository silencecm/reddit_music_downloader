#Subreddit Music Fetcher
Subreddit Music Fetcher - Downloads mp3s by scraping posts from a defined list of subreddits.
While currently functional this is an unreleased work in progress.

* [REQUIREMENTS](#requirements)
* [INSTALLATION](#installation)
* [USAGE](#usage)
* [TODO](#todo)
* [CONTRIBUTING](#contributing)

I wanted an automated utility to download a fresh batch of new (to me) music on demand.
Written in python the Subreddit Music Fetcher scrapes your favorite subreddits and
downloads external media (as audio only mp3). Downloaded urls are saved to avoid duplication 
Works best with "music" style subreddits where users mainly post media content urls from YouTube, 
Soundclound and the like.

# Requirements
* Unix / Bash prompt
* `wget` https://www.gnu.org/software/wget/.
* `pip` https://pypi.python.org/pypi/pip/.

# Installation
* Execute `sudo ./setup.sh` (make executable if necessary).
* Rename `subreddits.sample` to `subreddits`. Uncomment (by removing #) the desired subreddits. All uncommented
subreddits will be scraped for content.

# Usage
* Execute `python subreddit_music_fetcher.py`.

# TODO
* Add configuration file which can:
  * customize output directories.
  * change settings regarding the downloaders (quality, media file type, etc).
  * configure subreddit fetching (hot, new, top, etc). Currently defaults to new.
* Add warning for subreddit not found / 404.
* Add warning for empty subreddit file.
* Add support for sites other than just youtube (soundcloud (waiting for API key), bandcamp, etc.).
* Add versioning for releases
* Unit tests?
* Automatically add subreddits file. Instruct user to modify is no uncommented lines are found.

# Contributing
This is my first python project. Feel free to open an issue or pull request.

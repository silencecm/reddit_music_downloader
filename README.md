# Subreddit Music Fetcher
Subreddit Music Fetcher - Automatically downloads content posted to defined subreddits as mp3s.
While currently functional this is an unreleased work in progress.

* [REQUIREMENTS](#Requirements)
* [INSTALLATION](#Installation)
* [USAGE](#Usage)
* [TODO](#TODO)
* [CONTRIBUTING](#Contributing)

I wanted an automated utility to download a fresh batch of new unheard of music on demand.
Written in python the Reddit Music Downloader scrapes subreddits defined in [sources/subreddits](configuration/subreddits) and
downloads external media (currently as audio only (mp3)). Once media is downloaded the url is added to
[sources/downloaded](sources/downloaded) to avoid duplicate downloads. It's designed to be used with "music" style
subreddits where users mainly post media content urls from YouTube, Soundclound and the like.

#Requirements
* `wget` installed https://www.gnu.org/software/wget/.
* `pip` installed - https://pypi.python.org/pypi/pip/.

#Installation
* Execute `sudo ./setup.sh` (make executable if necessary).
* Rename `subreddits.sample` to `subreddits`. Uncomment (by removing #) the desired subreddits. All uncommented
subreddits will be scraped for content.

#Usage
* Execute `python fetch.py`.

## TODO
* Add configuration file which can:
  * customize output directories.
  * change settings regarding the downloaders (quality, media file type, etc).
  * configure subreddit fetching (hot, new, top, etc). Currently defaults to new.
* Add warning for subreddit not found / 404.
* Add support for sites other than just youtube (soundcloud (waiting for API key), bandcamp, etc.).
* Add versioning for releases

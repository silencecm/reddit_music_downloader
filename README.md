# Subreddit Music Downloader Utility
The utility is currently functional but requires some additional work for stability and support (see TODO).

I wanted an automated utility to download a fresh batch of new unheard of music on demand.
Written in python the Reddit Music Downloader scrapes subreddits defined in [sources/subreddits](sources/subreddits) and
downloads external media (currently as audio only (mp3)). Once media is downloaded the url is added to
[sources/downloaded](sources/downloaded) to avoid duplicate downloads. It's designed to be used with "music" style
subreddits where users mainly post media content urls from YouTube, Soundclound and the like.

## Prerequisites
* [https://github.com/rg3/youtube-dl](youtube-dl) required (until incorporated into this repository). Currently the
utility requires youtube-dl to be aliased. It also requires ffmpeg to be installed to convert media to mp3.
* Python 2.0+

## TODO
* Enhanced verbose output -- specifically display progress of downloads.
* Add configuration file which can.
⋅⋅* customize output file directory.
⋅⋅* change settings regarding the downloaders (quality, media file type, etc).
⋅⋅* configure subreddit fetching (hot, new, top, etc). Currently defaults to new.
* Add warning for empty sources/subreddits file.
* Add comment out support for sources/subreddits.
⋅⋅* Add every music subreddit known to man and comment most of them out. Users can then uncomment to easily add.
* Add support for sites other than just youtube (soundcloud, bandcamp, etc.).
* Put the downloads in a dated directory under fetched_media.
* Put the downloads in subreddit directories (under date (above)).
* Fork youtube-dl from github and run directly from this repository.
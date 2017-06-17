import json
import subprocess
import urllib2
import time
import datetime

from logger import Logger

# Used with resolve_redirects method. Sometimes urllib2.urlopen fails "Code 429: Too many requests.
redirect_timeout = 20

today = datetime.date.today()
formatted_date = str(today.day) + "_" + str(today.month) + "_" + str(today.year)

logger = Logger()
logger.smfprint_blue("Subreddit Music Fetcher by silencecm: http://github.com/silencecm")

def main():
    try:
        # Loop over defined subreddits (sources/subreddits)
        subreddits = open('configuration/subreddits')
        for subreddit in subreddits:
            # Ignore comments (lines that start with #) and empty lines
            if (subreddit[0] == "#" or subreddit == "\n"):
                continue

            json_object = get_json_from_subreddit_url(build_subreddit_url(subreddit))

            for children in json_object['data']['children']:
                media = children['data']
                url = media['url']

                try:
                    # Check if the url has been downloaded before
                    downloaded = open('downloaded/sources', 'r')
                    if url in downloaded.read():
                        logger.smfprint_warning("URL found in downloaded sources. Skipping.")
                    else:
                        if "youtube" in url:
                            process_youtube_download(subreddit, url)
                        # elif "soundcloud" in url:
                        #     process_soundcloud_download(subreddit, url)
                except IOError:
                    logger.smfprint_fail("Unable to find downloaded/sources. Please create downloaded/sources")
                    exit(0)
    except IOError:
        logger.smfprint_fail(str("[ERROR]: Unable to find configuration/subreddits. " +
        " Your probably need to rename configuration/subreddits.sample to configuration/subreddits" +
        " or create a new file named configuration/subreddits containing a list of subreddits to scrape from."))


def build_subreddit_url(subreddit):
    logger.smfprint_green("Building subreddit url for " + subreddit.strip())
    # Build a url for each subreddit found
    return "https://www.reddit.com/r/" + subreddit.rstrip() + "/new.json?sort=new"


def get_json_from_subreddit_url(subreddit_json_url):
    logger.smfprint_green("Processing json for: " + subreddit_json_url)
    # Fetch the json from the subreddit url
    request = urllib2.Request(subreddit_json_url)
    response = urllib2_workaround(request)
    return json.load(response)


# TODO waiting for soundcloud api key to implement soundcloud support
# def process_soundcloud_download(subreddit, url):
#     process_command('python soundcloud-dl/soundcloud-dl.py ' + url + '--dir ' + fetched_media_directory(subreddit), url)


def process_youtube_download(subreddit, url):
    process_download('/usr/local/bin/youtube-dl -o ' + fetched_media_directory(subreddit) +
                    '/%(title)s-%(id)s.%(ext)s --no-playlist --extract-audio --audio-format mp3 ' + url, url)


def fetched_media_directory(subreddit):
    return 'fetched_media/' + formatted_date + "/" + subreddit.strip() + "/"


def process_download(command, url):
    logger.smfprint_green("Processing download for " + url)
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output, error = process.communicate()

    try:
        dl = open('downloaded/sources', 'a')
        logger.smfprint_green("Appending URL to downloaded file.")
        dl.write(url + "\n")
    except IOError:
        logger.smfprint_fail("Unable to find downloaded/sources. Please create downloaded/sources")


# A bug with urllib2? Every so often it throws Code 429 and refuses to fetch.
def urllib2_workaround(request):
    try:
        return urllib2.urlopen(request)
    except urllib2.HTTPError as e:
        if e.code == 429:
            logger.smfprint_warning("[WARNING]: UrlLib2 Code 429: TOO MANY REQUESTS. Sleeping for " + str(redirect_timeout) + " seconds.")
            time.sleep(redirect_timeout)
            return urllib2_workaround(request)
        raise


if __name__ == '__main__':
    main()

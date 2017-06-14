import json
import subprocess
import urllib2
import time
import datetime

# Used with resolve_redirects method. Sometimes urllib2.urlopen fails "Code 429: Too many requests.
redirect_timeout = 20

today = datetime.date.today()
formatted_date = str(today.day) + "_" + str(today.month) + "_" + str(today.year)

def main():
    # Loop over defined subreddits (sources/subreddits)
    with open('configuration/subreddits') as subreddits:
        for subreddit in subreddits:
            # Ignore comments (lines that start with #) and empty lines
            if (subreddit[0] == "#" or subreddit == "\n"):
                continue

            # Build a url for each subreddit found
            subreddit_json_url = "https://www.reddit.com/r/" + subreddit.rstrip() + "/new.json?sort=new"
            print("Processing json for: " + subreddit.rstrip() + " using URL: " + subreddit_json_url)

            # Process the request, parse the json and fetch each source found
            request = urllib2.Request(subreddit_json_url)
            response = resolve_redirects(request)
            json_object = json.load(response)

            for children in json_object['data']['children']:
                media = children['data']
                url = media['url']

                # Check if the url has been downloaded before
                with open('downloaded/sources', 'r') as downloaded:
                    if url in downloaded.read():
                        print("URL found in downloaded sources. Skipping.")
                    else:
                        if "youtube" in url:
                            process_youtube_download(subreddit, url)
                        elif "soundcloud" in url:
                            process_soundcloud_download(subreddit, url)

def process_soundcloud_download(subreddit, url):
    process_command('python soundcloud-dl/soundcloud-dl.py ' + url + '--dir ' + fetched_media_directory(subreddit), url)

def process_youtube_download(subreddit, url):
    process_command('youtube-dl/bin/youtube-dl -o ' + fetched_media_directory(subreddit) +
                    '/%(title)s-%(id)s.%(ext)s --no-playlist --extract-audio --audio-format mp3 ' + url, url)

def fetched_media_directory(subreddit):
    return 'fetched_media/' + formatted_date + "/" + subreddit.strip() + "/"

# FIXME run the python commands directly without using subprocess, this is dirty
def process_command(command, url):
    print("Processing download for " + url)
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()

    with open('downloaded/sources', 'a') as dl:
        print("Appending URL to downloaded file.")
        dl.write(url + "\n")

def resolve_redirects(request):
    try:
        return urllib2.urlopen(request)
    except urllib2.HTTPError as e:
        if e.code == 429:
            print("[WARNING]: UrlLib2 Code 429: TOO MANY REQUESTS. Sleeping for " + str(redirect_timeout) + " seconds.")
            time.sleep(redirect_timeout)
            return resolve_redirects(request)
        raise

if __name__ == '__main__':
    main()
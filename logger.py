class Logger(object):
    # Plain with prefix
    def smfprint(self, string):
        print(self.add_prefix(string))

    # Blue header
    def smfprint_header(self, string):
        print(str(bcolors.HEADER + self.add_prefix(string)) + bcolors.ENDC)

    # Blue
    def smfprint_blue(self, string):
        print(str(bcolors.OKBLUE) + self.add_prefix(string) + bcolors.ENDC)

    # Green
    def smfprint_green(self, string):
        print(str(bcolors.OKGREEN) + self.add_prefix(string) + bcolors.ENDC)

    # Yellow + [WARNING]
    def smfprint_warning(self, string):
        print(str(bcolors.WARNING + self.add_prefix("[WARNING]: " + string)) + bcolors.ENDC)

    # Red + [ERROR]
    def smfprint_fail(self, string):
        print(str(bcolors.FAIL) + self.add_prefix("[ERROR] " + string) + bcolors.ENDC)

    # Bold
    def smfprint_bold(self, string):
        print(str(bcolors.BOLD) + self.add_prefix(string) + bcolors.ENDC)

    # Underline
    def smfprint_underline(self, string):
        print(str(bcolors.UNDERLINE) + self.add_prefix(string) + bcolors.ENDC)

    # Adds [subreddit_music_fetcher]
    def add_prefix(self, string):
        return "[subreddit_music_fetcher] " + string

# TODO add more colors
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

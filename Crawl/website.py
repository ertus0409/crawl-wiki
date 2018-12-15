# Website class to store information solely about the site structure
#   page-content is stored in Content class not the Website class.
class Website:
    def __init__(self, name, url, targetPattern):
        self.name = name
        self.url = url
        self.targetPattern = targetPattern
        self.base_url = 'https://en.wikipedia.org'


# Class content storing necessary data for the content provided.
class Content:
    def __init__(self, url, title, table):
        self.url = url
        self.title = title
        self.table = table
    # print() to better visualize data fot the command prompt.
    def print(self):
        print()
        print("TITLE:   %s" % self.title)
        print("URL:     %s" % self.url)
        print("TABLE:   %s" % self.table)

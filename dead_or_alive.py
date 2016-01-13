import requests

class Wiki_Person(object):

    def __init__(self, name):
        self._name = name.title()
        self._url = self.wiki_url()
        self._response = self.wiki_response()
    
    def wiki_url(self):
        """Return wiki url for given object"""
        return'https://en.wikipedia.org/w/api.php?action=query&titles={0}&continue=&prop=categories&format=json'.format(self._name)
        
    def wiki_response(self):
        """Return Json from wikipedia for given object"""
        return requests.get(self._url).json()

    @property
    def categories(self):
        """Return all categories for a given object """
        try:
            cat_list = self._response["query"]["pages"].values()[0]["categories"]
            return [item["title"][9:] for item in cat_list]
        except KeyError:
            print "{} is not a wikipedia page".format(self._name)
    
    def is_dead(self):
        for item in self.categories:
            if 'deaths' in item:
                return True
        return False

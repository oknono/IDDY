def wiki_json(name):
    name = name.strip().title()
    url = 'https://en.wikipedia.org/w/api.php?action=query&titles={0}&continue=&prop=categories&format=json'.format(name)
    return url

def categories(response):
	return response.json()["query"]["pages"].values()[0]["categories"]

def is_ambiguous(dic):
    for item in dic:
        if 'disambiguation' in item["title"]:
            return True
    return False
     
def is_dead(dic):
    for item in dic:
        if 'deaths' in item["title"]:
            return True
    return False

def was_born(dic):
    for item in dic:
        if 'births' in item["title"]:
            return True
    return False
    
      
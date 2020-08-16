class Episodes(object):
    def __init__(self, episodes):
        self.episodes = episodes
    
    def __repr__(self):
        return f"<{len(self.episodes)} episodes>"
    
    def get_episode_by_number(self, number):
        for x in self.episodes:
            if x.episode == number:
                return x

class Episode(object):

    def __init__(self, json_response, network, loop):
        self.__network = network
        self.__loop = loop
        self.anime_id = json_response.get("anime_id", None)
        self.created_at = json_response.get("created_at", None)
        self.disc = json_response.get("disc", None)
        self.duration = json_response.get("duration", None)
        self.edition = json_response.get("edition", None)
        self.episode = json_response.get("episode", None)
        self.episode_2 = json_response.get("episode2", None)
        self.filler = json_response.get("filler", None)
        self.id = json_response.get("id", None)
        self.session = json_response.get("session", None)
        self.snapshot = json_response.get("snapshot", None)
        self.fansub = json_response.get("fansub", None)
        self.title = json_response.get("title", None)

    def __repr__(self):
        return f"<Episode {self.id}>"


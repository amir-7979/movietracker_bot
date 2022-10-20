from dataclasses import dataclass
from typing import Any
from typing import List


@dataclass
class ActorsAndCharacter:
    id: str
    name: str
    gender: str
    country: str
    image: str
    positions: List[str]

    @staticmethod
    def from_dict(obj: Any) -> 'ActorsAndCharacter':
        _id = str(obj.get("id"))
        _name = str(obj.get("name"))
        _gender = str(obj.get("gender"))
        _country = str(obj.get("country"))
        _image = str(obj.get("image"))
        _positions = [str(y) for y in obj.get("positions")]
        return ActorsAndCharacter(_id, _name, _gender, _country, _image, _positions)


@dataclass
class Director:
    _id: str
    name: str
    gender: str
    country: str
    image: str
    positions: List[str]
    characterData: str

    @staticmethod
    def from_dict(obj: Any) -> 'Director':
        __id = str(obj.get("_id"))
        _name = str(obj.get("name"))
        _gender = str(obj.get("gender"))
        _country = str(obj.get("country"))
        _image = str(obj.get("image"))
        _positions = [str(y) for y in obj.get("positions")]
        _characterData = str(obj.get("characterData"))
        return Director(__id, _name, _gender, _country, _image, _positions, _characterData)


@dataclass
class LatestData:
    season: int
    episode: int
    quality: str
    hardSub: str
    dubbed: str
    censored: str
    subtitle: str
    watchOnlineLink: str
    updateReason: str

    @staticmethod
    def from_dict(obj: Any) -> 'LatestData':
        _season = int(obj.get("season"))
        _episode = int(obj.get("episode"))
        _quality = str(obj.get("quality"))
        _hardSub = str(obj.get("hardSub"))
        _dubbed = str(obj.get("dubbed"))
        _censored = str(obj.get("censored"))
        _subtitle = str(obj.get("subtitle"))
        _watchOnlineLink = str(obj.get("watchOnlineLink"))
        _updateReason = str(obj.get("updateReason"))
        return LatestData(_season, _episode, _quality, _hardSub, _dubbed, _censored, _subtitle, _watchOnlineLink,
                          _updateReason)


@dataclass
class Poster:
    url: str
    info: str
    size: int

    @staticmethod
    def from_dict(obj: Any) -> 'Poster':
        _url = str(obj.get("url"))
        _info = str(obj.get("info"))
        _size = int(obj.get("size"))
        return Poster(_url, _info, _size)


@dataclass
class Rating:
    imdb: float
    rottenTomatoes: int
    metacritic: int
    myAnimeList: int

    @staticmethod
    def from_dict(obj: Any) -> 'Rating':
        _imdb = float(obj.get("imdb"))
        _rottenTomatoes = int(obj.get("rottenTomatoes"))
        _metacritic = int(obj.get("metacritic"))
        _myAnimeList = int(obj.get("myAnimeList"))
        return Rating(_imdb, _rottenTomatoes, _metacritic, _myAnimeList)


@dataclass
class SeasonEpisode:
    seasonNumber: int
    episodes: int

    @staticmethod
    def from_dict(obj: Any) -> 'SeasonEpisode':
        _seasonNumber = int(obj.get("seasonNumber"))
        _episodes = int(obj.get("episodes"))
        return SeasonEpisode(_seasonNumber, _episodes)


@dataclass
class Writer:
    _id: str
    name: str
    gender: str
    country: str
    image: str
    positions: List[str]
    characterData: str

    @staticmethod
    def from_dict(obj: Any) -> 'Writer':
        __id = str(obj.get("_id"))
        _name = str(obj.get("name"))
        _gender = str(obj.get("gender"))
        _country = str(obj.get("country"))
        _image = str(obj.get("image"))
        _positions = [str(y) for y in obj.get("positions")]
        _characterData = str(obj.get("characterData"))
        return Writer(__id, _name, _gender, _country, _image, _positions, _characterData)


@dataclass
class Staff:
    directors: List[Director]
    writers: List[Writer]

    @staticmethod
    def from_dict(obj: Any) -> 'Staff':
        _directors = [Director.from_dict(y) for y in obj.get("directors")]
        _writers = [Writer.from_dict(y) for y in obj.get("writers")]
        return Staff(_directors, _writers)


@dataclass
class Summary:
    persian: str
    english: str
    english_source: str
    persian_source: str

    @staticmethod
    def from_dict(obj: Any) -> 'Summary':
        _persian = str(obj.get("persian"))
        _english = str(obj.get("english"))
        _english_source = str(obj.get("english_source"))
        _persian_source = str(obj.get("persian_source"))
        return Summary(_persian, _english, _english_source, _persian_source)


@dataclass
class TelBotItem:
    _id: str
    type: str
    rawTitle: str
    posters: List[Poster]
    summary: Summary
    latestData: LatestData
    releaseDay: str
    year: str
    premiered: str
    duration: str
    rated: str
    country: str
    genres: List[str]
    rating: Rating
    actorsAndCharacters: List[ActorsAndCharacter]
    staff: Staff
    seasonEpisode: List[SeasonEpisode]

    @staticmethod
    def from_dict(obj: Any) -> 'TelBotItem':
        __id = str(obj.get("_id"))
        _type = str(obj.get("type"))
        _rawTitle = str(obj.get("rawTitle"))
        _posters = [Poster.from_dict(y) for y in obj.get("posters")]
        _summary = Summary.from_dict(obj.get("summary"))
        _latestData = LatestData.from_dict(obj.get("latestData"))
        _releaseDay = str(obj.get("releaseDay"))
        _year = str(obj.get("year"))
        _premiered = str(obj.get("premiered"))
        _duration = str(obj.get("duration"))
        _rated = str(obj.get("rated"))
        _country = str(obj.get("country"))
        _genres = [str(y) for y in obj.get("genres")]
        _rating = Rating.from_dict(obj.get("rating"))
        _actorsAndCharacters = [ActorsAndCharacter.from_dict(y) for y in obj.get("actorsAndCharacters")]
        _staff = Staff.from_dict(obj.get("staff"))
        _seasonEpisode = [SeasonEpisode.from_dict(y) for y in obj.get("seasonEpisode")]
        return TelBotItem(__id, _type, _rawTitle, _posters, _summary, _latestData, _releaseDay, _year, _premiered,
                          _duration, _rated, _country, _genres, _rating, _actorsAndCharacters, _staff, _seasonEpisode)

    def get_actors(self) -> str:
        if len(self.actorsAndCharacters) != 0:
            return f"🎭 Actors : {', '.join([y.name.capitalize() for y in self.actorsAndCharacters][0:4])}\n\n"

    def get_last_update(self) -> str:
        if self.latestData.updateReason is not None:
            if self.latestData.updateReason == 'season'and self.latestData.season != 0:
                return f"➕ Update : season {self.latestData.season} added\n\n"
            if self.latestData.updateReason == 'episode' and self.latestData.episode != 0:
                return f"➕ Update : episode {self.latestData.episode} from season {self.latestData.season} added\n\n"
            if self.latestData.updateReason == 'quality' and len(self.latestData.quality) != 0:
                return f"➕ Update : quality {self.latestData.quality} added\n\n"

    def get_rate(self) -> str:
        rate: str = ''
        if self.rating.imdb != 0:
            rate = rate.__add__(f"🎖IMDb: {self.rating.imdb} ")
        if self.rating.metacritic != 0:
            rate = rate.__add__(f"|ⓂMeta: {self.rating.metacritic} ")
        if self.rating.rottenTomatoes != 0:
            rate = rate.__add__(f"|🍅RT: {self.rating.rottenTomatoes} ")
        if self.rating.myAnimeList != 0:
            rate = rate.__add__(f"|🏅myAnimeList: {self.rating.myAnimeList} ")
        if len(rate) != 0:
            if rate[0] == '|':
                rate = rate[1:]
            rate = rate.__add__('\n\n')
        return rate

    def get_summary(self) -> str:
        summary: str = ''
        first_part = '📜 Summary: \n'
        if len(self.summary.persian) == 0:
            if len(self.summary.english) != 0:
                summary = self.summary.english
        else:
            summary = self.summary.persian
        if len(summary) > 150:
            summary = " ".join(summary.split()[:85])
        return first_part + summary + ' ...\n\n'

    def get_year(self) -> str:
        if len(self.year) != 0:
            return f"📅 Year : {self.year}\n\n"

    def get_genre(self) -> str:
        if len(self.genres) != 0:
            return f"⭕ Genre : {', '.join(self.genres)}\n\n"

    def get_website_url(self) -> str:
        website_url = f"https://movie-tracker-nine.vercel.app/movie/{self._id}/{self.rawTitle.replace(' ', '_')}"
        if len(self.year) != 0:
            website_url = website_url.__add__(f"-{self.year}")
        return website_url

    def get_download_link(self) -> str:
        return f"https://t.me/MovieTracker1bot?start={self._id}-{self.type}"

    def get_url(self) -> str:
        if self.posters[0].url is None:
            print(self.id)
        return self.posters[0].url

    def to_string(self):
        return f"🎬 {self.rawTitle}\n\n🔹 Type : {self.type.title().replace('_', ' ')}\n\n{self.get_rate()}{self.get_year()}{self.get_genre()}{self.get_actors()}{self.get_summary()}[📥 download]({self.get_download_link()})\n\n[🌐 website]({self.get_website_url()})\n\n[🔔 channel](https://t.me/movie_tracker1) "

    def to_string_update(self):
        print(self.latestData)
        return f"🎬 {self.rawTitle}\n\n🔹 Type : {self.type.title().replace('_', ' ')}\n\n{self.get_rate()}{self.get_last_update()}{self.get_year()}{self.get_genre()}{self.get_actors()}{self.get_summary()}[📥 download]({self.get_download_link()})\n\n[🌐 website]({self.get_website_url()})\n\n[🔔 channel](https://t.me/movie_tracker1) "

    @property
    def id(self):
        return self._id

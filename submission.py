import plotly.express as px
from random import *

# Do not modify the line below.
countries = ["Argentina", "Bolivia", "Brazil", "Chile", "Colombia", "Ecuador", "Falkland Islands", "Guyana", "Paraguay",
             "Peru", "Suriname", "Uruguay", "Venezuela"]

# Do not modify the line below.
colors = ["blue", "green", "red", "yellow"]


class Country:
    def __init__(self, name):
        self.name = name
        self.neighbors = []
        self.color = None

    def paintCountry(self, color):
        self.color = color

    def removeColor(self):
        self.color = None

    def addNeighbors(self, *neighbors):
        for neighbor in neighbors:
            self.neighbors.append(neighbor)


class Map:
    def __init__(self):
        self.countries = []

    def isSafe(self, country_1, color):
        for neighbor in country_1.neighbors:
            if neighbor.color == color:
                return False

        return True

    def addCountry(self, country):
        self.countries.append(country)

    def isNeighbor(self, country_1, country_2):
        if country_2 in country_1.neighbors:
            return True

        return False

    def mapAsDict(self):
        countriesDict = {}
        for country in self.countries:
            countriesDict[country.name] = country.color

        return countriesDict

    def initializeMap(self):
        southAmerica = Map()

        argentina = Country("Argentina")
        bolivia = Country("Bolivia")
        brazil = Country("Brazil")
        chile = Country("Chile")
        colombia = Country("Colombia")
        ecuador = Country("Ecuador")
        falklandislands = Country("Falkland Islands")
        guyana = Country("Guyana")
        paraguay = Country("Paraguay")
        peru = Country("Peru")
        suriname = Country("Suriname")
        uruguay = Country("Uruguay")
        venezuela = Country("Venezuela")

        argentina.addNeighbors(bolivia, chile, paraguay, uruguay, brazil)
        bolivia.addNeighbors(argentina, brazil, chile, paraguay, peru)
        brazil.addNeighbors(argentina, bolivia, colombia, guyana, paraguay, peru, suriname, uruguay, venezuela)
        chile.addNeighbors(argentina, bolivia, peru)
        colombia.addNeighbors(brazil, ecuador, peru, venezuela)
        ecuador.addNeighbors(colombia, peru)
        guyana.addNeighbors(brazil, suriname, venezuela)
        paraguay.addNeighbors(argentina, bolivia, brazil)
        peru.addNeighbors(bolivia, brazil, chile, colombia, ecuador)
        suriname.addNeighbors(brazil, guyana)
        uruguay.addNeighbors(argentina, brazil)
        venezuela.addNeighbors(brazil, colombia, guyana)

        southAmerica.addCountry(argentina)
        southAmerica.addCountry(bolivia)
        southAmerica.addCountry(brazil)
        southAmerica.addCountry(chile)
        southAmerica.addCountry(colombia)
        southAmerica.addCountry(ecuador)
        southAmerica.addCountry(falklandislands)
        southAmerica.addCountry(guyana)
        southAmerica.addCountry(paraguay)
        southAmerica.addCountry(peru)
        southAmerica.addCountry(suriname)
        southAmerica.addCountry(uruguay)
        southAmerica.addCountry(venezuela)

        return southAmerica

    def BacktrackSearch(self):
        if self.__BacktrackSearchUtil__(0):
            print("There is solution.")
        else:
            print("There is no solution available.")

    # IC means Index of Country
    def __BacktrackSearchUtil__(self, IC):
        if IC == len(self.countries):
            return True

        shuffle(colors)

        for color in colors:
            if self.isSafe(self.countries[IC], color):
                self.countries[IC].paintCountry(color)

                if self.__BacktrackSearchUtil__(IC + 1):
                    return True

                self.countries[IC].removeColor()

        return False


def plot_choropleth(colormap):
    fig = px.choropleth(locationmode="country names",
                        locations=countries,
                        color=countries,
                        color_discrete_sequence=[colormap[c] for c in countries],
                        scope="south america")
    fig.show()


# Implement main to call necessary functions
if __name__ == "__main__":
    southAmerica = Map().initializeMap()
    southAmerica.BacktrackSearch()

    dictionary = southAmerica.mapAsDict()

    plot_choropleth(colormap=dictionary)
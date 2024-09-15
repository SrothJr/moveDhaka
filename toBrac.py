all_places = []

class ways:
    
    def __init__(self, From, To, fare="Unknown", means="Unknown"):
        self.From = From
        self.To = To
        self.fare = fare
        self.means = [means]

    # def get_ways(self, )

class places:
    def __init__(self, name, north=None, south=None, traffic = None):
        self.name = name
        self.north = north
        self.south = south
        self.traffic = traffic

        global all_places
        all_places.append(self)

    def add_north(self, north):
        self.north = north
    
    def add_south(self, south):
        self.south = south

    def add_traffic(self, traffic):
        self.traffic = traffic
    
    def add_to_list(self):
        global all_places
        all_places.append(self)


bracu = places("Brac University")
malibagh = places("Malibagh")
komolapur = places("KomolaPur", malibagh, None, 7)
sayedabad = places("Sayedabad", komolapur, None, 10)
shonirakhra = places("Shonir Akhra", sayedabad, None, 7)



bracu.add_south(malibagh)
malibagh.add_north(bracu)
# komolapur.add_to_list()

malibagh2bracu = ways(malibagh, bracu, 10, "Bus: Raida, Anabil, Turag")

print(all_places[0].name)
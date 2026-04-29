from planet import Planet, PlanetCollection

def main():
    planet1 = Planet(
        name="e2", 
        radius=560, 
        mass=720,
        distance=15000,
        planet_type="каменная"
    )

    print(planet1.name)
    print(planet1.radius)
    print(planet1.mass)
    print(planet1.distance)
    print(planet1.planet_type)


def db_tester():
    planet1 = Planet(
        name="1", 
        radius=5621230, 
        mass=72123213210,
        distance=150013321230,
        planet_type="каменная"
    )
    planet2 = planet1.__copy__()
    print(planet2)
    



if __name__ == "__main__":
    #main()
    db_tester()
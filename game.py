from goblin import Goblin
from hero import Hero

ARENA_NAME = "The Steel Pit"

def main():
    """Open the arena and introduce its first opponent."""
    print(f"Welcome to {ARENA_NAME}!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")
    print("The gates are opening...\n")

    #Create Goblin
    goblin = Goblin("Greg")

    print(f"{goblin.name} enters the arena with {goblin.health} health.")
<<<<<<< Updated upstream
    print("But no hero has answered the call... yet.")
=======

    #Create Second Goblin
    secondGoblin = Goblin("Scribble")
    print(f"{secondGoblin.name} enters the arena with {secondGoblin.health} health.")

    print("\nBut no hero has answered the call... yet.\n")

    #Create Mr.Speak
    hero = Hero("Mr.Speak")
    print(f"{hero.name} appears in the arena with {hero.health} health!")

def battle(hero: Hero, enemy: Goblin):
    while hero.is_alive() and enemy.is_alive():
        print(f"Mr.Speak reaches down to pick up a weapon and strikes {enemy.name}!\n")
        enemy.take_damage(hero.attack())
        
        if enemy.is_alive():
            print(f"{enemy.name} attacks {hero.name}!\n")
            hero.take_damage(enemy.attack())
    if hero.is_alive():
        print(f"{hero.name} wins!")
    else:
        print(f"{enemy.name} wins!")
>>>>>>> Stashed changes


if __name__ == "__main__":
    main()
    battle(hero = Hero("Mr.Speak"), enemy = Goblin("Greg"))

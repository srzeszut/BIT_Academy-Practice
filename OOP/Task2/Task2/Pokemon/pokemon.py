class Pokemon():
    name    = "Unknown Pokemon"
    origin  = "Unkown Origin"
    hp      = "Unkown Hp"
    attack  = "Unkown Attack"
    defense = "Unkown Defense"
    speed   = "Unkown Speed"
    total   = "Unkown Total"

    def Is_same_type(A, B):
        if type(A) == Pokemon or type(B) == Pokemon:
            print("Unknown origin of at least one of pokemons")
        else:
            print("Yes" if A.origin == B.origin else "No")

    def Fight(A, B):
        print(f"The winner:   {A.name if A.total > B.total else B.name}")

    def Compare_hp(A, B):
        print(f"More HP:      {A.name if A.hp > B.hp else B.name}")

    def Compare_attack(A, B):
        print(f"More Attack:  {A.name if A.attack > B.attack else B.name}")

    def Compare_defense(A, B):
        print(f"More Defense: {A.name if A.defense > B.defense else B.name}")

    def Compare_speed(A, B):
        print(f"More Speed:   {A.name if A.speed > B.speed else B.name}")

from lnn import Model, Variables, Predicate, Implies, Forall, Exists, And, Or, Not, World, Loss, Fact

"""
Wolves, foxes, birds, caterpillars, and snails are animals, and there are some of each of them.
Also there are some grains, and grains are plants.
Every animal either likes to eat all plants or all animals much smaller than itself that like to eat some plants.
Caterpillars and snails are much smaller than birds, which are much smaller than foxes, which in turn are much smaller than wolves.
Wolves do not like to eat foxes or grains, while birds like to eat caterpillars but not snails.
Caterpillars and snails like to eat some plants.
Therefore there is an animal that likes to eat a grain-eating animal.
"""

def test():
    # Define model
    model = Model()

    # Define variables
    x, y, z = Variables("x", "y", "z")

    # Define predicates
    animal_P = Predicate("is an animal")
    wolf_P = Predicate("is a wolf")
    fox_P = Predicate("is a fox")
    bird_P = Predicate("is a bird")
    caterpillar_P = Predicate("caterpillar")
    snail_P = Predicate("is a snail")
    plant_Q = Predicate("is a plant")
    grain_Q = Predicate("is a grain")
    smaller_S = Predicate("is much smaller than", arity=2)
    eats_R = Predicate("likes to eat", arity=2)

    # Define rules and knowledge
    wolf_is_animal = Implies(wolf_P(x), animal_P(x))
    all_wolves_are_animals = Forall(x, wolf_is_animal)
    wolf_exists = Exists(x, wolf_P)
    all_wolves_are_animals_and_exist = And(all_wolves_are_animals, wolf_exists)

    fox_is_animal = Implies(fox_P(x), animal_P(x))
    all_foxes_are_animals = Forall(x, fox_is_animal)
    fox_exists = Exists(x, fox_P)
    all_foxes_are_animals_and_exist = And(all_foxes_are_animals, fox_exists)

    bird_is_animal = Implies(bird_P(x), animal_P(x))
    all_birds_are_animals = Forall(x, bird_is_animal)
    bird_exists = Exists(x, bird_P)
    all_birds_are_animals_and_exist = And(all_birds_are_animals, bird_exists)

    caterpillar_is_animal = Implies(caterpillar_P(x), animal_P(x))
    all_caterpillars_are_animals = Forall(x, caterpillar_is_animal)
    caterpillar_exists = Exists(x, caterpillar_P)
    all_caterpillars_are_animals_and_exist = And(all_caterpillars_are_animals, caterpillar_exists)

    snail_is_animal = Implies(snail_P(x), animal_P(x))
    all_snails_are_animals = Forall(x, snail_is_animal)
    snail_exists = Exists(x, snail_P)
    all_snails_are_animals_and_exist = And(all_snails_are_animals, snail_exists)

    grains_exist = Exists(x, grain_Q)
    grains_are_plants = Implies(grain_Q(x), plant_Q(x))
    all_grains_are_plants = Forall(x, grains_are_plants)
    grains_exist_and_all_grains_are_plants = And(grains_exist, all_grains_are_plants)

    # (Ax)(
    #     P0x
    #     ->
    #     [(Ay)(Q0y -> Rxy) + (Ay)((P0y & Syx & (Ez)(Q0z & Ryz)) -> Rxy)]
    # )

    all_animals_eat_plants_or_smaller_animals_who_eat_plants = Forall(
        x,
        Implies(
            animal_P(x),
            Or(
                Forall(
                    y,
                    Implies(
                        plant_Q(y),
                        eats_R(x, y)
                    )
                ),
                Implies(
                    Forall(
                        y,
                        And(
                            animal_P(y),
                            smaller_S(y, x),
                            Exists(
                                z,
                                And(
                                    plant_Q(z),
                                    eats_R(y, z)
                                )
                            )
                        )
                    ),
                    eats_R(x, y)
                )
            )
        )
    )

    all_caterpillars_and_snails_smaller_than_birds = Forall(
        x,
        y,
        Implies(
            And(
                bird_P(y),
                Or(
                    snail_P(x),
                    caterpillar_P(x)
                )
            ),
            smaller_S(x, y)
        )
    )

    all_birds_smaller_than_foxes = Forall(
        x,
        y,
        Implies(
            And(
                bird_P(x),
                fox_P(y)
            ),
            smaller_S(x, y)
        )
    )

    all_foxes_smaller_than_wolves = Forall(
        x,
        y,
        Implies(
            And(
                fox_P(x),
                wolf_P(y)
            ),
            smaller_S(x, y)
        )
    )

    all_wolves_dont_eat_foxes_or_grains = Forall(
        x,
        y,
        Implies(
            And(
                wolf_P(x),
                Or(
                    fox_P(y),
                    grain_Q(y)
                )
            ),
            Not(eats_R(x, y))
        )
    )

    birds_eat_caterpillars = Forall(
        x,
        y,
        Implies(
            And(
                bird_P(x),
                caterpillar_P(y)
            ),
            eats_R(x, y)
        )
    )

    birds_dont_eat_snails = Forall(
        x,
        y,
        Implies(
            And(
                bird_P(x),
                snail_P(y)
            ),
            Not(eats_R(x, y))
        )
    )

    caterpillars_and_snails_eat_some_plants = Forall(
        x,
        Implies(
            Or(
                caterpillar_P(x),
                snail_P(x)
            ),
            Exists(
                y,
                And(
                    plant_Q(y),
                    eats_R(x, y)
                )
            )
        )
    )

    # Define query
    query = Exists(
        x,
        y,
        And(
            animal_P(x),
            animal_P(y),
            Exists(
                z,
                And(
                    grain_Q(z),
                    eats_R(y, z),
                    eats_R(x, y)
                )
            )
        )
    )

    # Add knowledge and rules
    model.add_knowledge(
        all_wolves_are_animals_and_exist,
        all_foxes_are_animals_and_exist,
        all_birds_are_animals_and_exist,
        all_caterpillars_are_animals_and_exist,
        all_snails_are_animals_and_exist,
        grains_exist_and_all_grains_are_plants,
        all_animals_eat_plants_or_smaller_animals_who_eat_plants,
        all_caterpillars_and_snails_smaller_than_birds,
        all_birds_smaller_than_foxes,
        all_foxes_smaller_than_wolves,
        all_wolves_dont_eat_foxes_or_grains,
        birds_eat_caterpillars,
        birds_dont_eat_snails,
        caterpillars_and_snails_eat_some_plants,
        world=World.AXIOM
    )

    # Set query
    #model.set_query(query)
    model.add_knowledge(
        query,
        world=World.CONTRADICTION
    )

    # Add fact data to model
    model.add_data(
        {
            wolf_P: {
                "wolf1": Fact.TRUE
            },
            fox_P: {
                ("fox1"): Fact.TRUE
            },
            bird_P: {
                ("bird1"): Fact.TRUE
            },
            caterpillar_P: {
                ("caterpillar1"): Fact.TRUE
            },
            snail_P: {
                ("snail1"): Fact.TRUE
            },
            grain_Q: {
                ("grain1"): Fact.TRUE
            }
        }
    )

    # Perform inference
    model.print()

    # model.infer()

    losses = [Loss.CONTRADICTION]
    epochs, total_loss = model.train(losses=losses, pbar=True)

    model.print()
    model.query.print(params=True)

    print(f"    epochs: {epochs}\n    total_loss: {total_loss}")




if __name__ == "__main__":
    test()
def parse_input():
    N = int(input())
    potion_to_recipes = {}
    all_potions = set()
    ingredients_used = set()
    # 
    for _ in range(N):
        line = input().strip()
        left, right = line.split('=')
        potion = left.strip()
        ingredients = [ing.strip() for ing in right.strip().split('+')]
        # 
        if potion not in potion_to_recipes:
            potion_to_recipes[potion] = []
        potion_to_recipes[potion].append(ingredients)
        # 
        all_potions.add(potion)
        ingredients_used.update(ingredients)
    # 
    target = input().strip()
    return potion_to_recipes, all_potions, ingredients_used, target


def solve():
    potion_to_recipes, all_potions, ingredients_used, target = parse_input()
    memo = {}
    base_items = ingredients_used - all_potions
    # 
    def min_orbs(potion):
        if potion in memo:
            return memo[potion]
        if potion in base_items:
            return 0
        # 
        min_cost = float('inf')
        for recipe in potion_to_recipes.get(potion, []):
            cost = len(recipe) - 1 + sum(min_orbs(ing) for ing in recipe)
            min_cost = min(min_cost, cost)
        # 
        memo[potion] = min_cost
        return min_cost
    # 
    print(min_orbs(target))


solve()

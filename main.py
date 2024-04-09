from supermarkets.intermarche import INTERMARCHES

products = INTERMARCHES.get_supermarkets_by_postal_code(38000)[0].search_products('lait')

print(list(map(lambda product: vars(product), products)))
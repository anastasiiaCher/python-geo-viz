city_list = [
    {"city": "Москва", "population": 12.5},
    {"city": "Санкт-Петербург", "population": 5.4},
    {"city": "Москва", "population": 1.6},
    {"city": "Екатеринбург", "population": 1.5},
    {"city": "Нижний Новгород", "population": 1.3},
]

num_cities = len(city_list)
total_population = sum([x["population"] for x in city_list])
print(f"Среднее арифметическое населения равно = {total_population/num_cities}")

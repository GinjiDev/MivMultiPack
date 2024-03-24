import MivMultiPack, time

module = MivMultiPack

generate = module.async_random_range(start=-1, stop=2)

while True:
    var = generate.generate_random_number()
    print(var)
    time.sleep(0.2)
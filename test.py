import MivMultiPack, time

module = MivMultiPack

generate = module.async_random(seed=2, digits=1)

while True:
    print(generate.generate_random_number())
    time.sleep(1)
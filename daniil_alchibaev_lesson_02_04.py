input_workers = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА',
                 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

for worker in input_workers:
    worker_name = (worker.split(" ")[-1]).capitalize()
    print(f"Привет, {worker_name}!")

import multiprocessing
import time

#funkcja do ciężkich obliczeń
def suma_kwadratow(start,end):
    print(f"Proces {multiprocessing.current_process().name} oblicza od {start} do {end}")
    return sum(x**x for x in range(start,end))

if __name__ == '__main__':
    zakresy = [(1,5_000_000),(5_000_000,10_000_000),(10_000_000,15_000_000),(15_000_000,20_000_000)]

    start_time = time.time()

    with multiprocessing.Pool(processes=4) as pool:
        wyniki = pool.starmap(suma_kwadratow,zakresy)

    suma = sum(wyniki)
    print(f"Suma kwadratów(wszystkie wyniki): {suma}")
    end_time = time.time()

    print(f"Czas wykonania: {end_time-start_time} sekund")
  

import threading
import time

def zadanie(nazwa):
    for i in range(5):
        print(f"Zadanie {nazwa} - {i}\n")
        time.sleep(1)

w1 = threading.Thread(target=zadanie, args=("wątek A",))
w2 = threading.Thread(target=zadanie, args=("wątek B",))

#uruchomienie równoległe wątków
w1.start()
w2.start()

#wymuszenie wątków do zakończenia
w1.join()
w2.join()

print("Wszystkie wątki zakończone!")

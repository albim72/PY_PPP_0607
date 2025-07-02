import traceback

def risky_division(a,b):
    try:
        result = a/b
        print(f"wynik dzielenia: {result}")
    except ZeroDivisionError as e:
        print("Division by zero!")
        print(f"Typ wyjątku: {type(e).__name__}")
        print(f"Szczegóły wyjątku: {e}")
        print(f"Stałe wyjątku: {e.__traceback__}")
        print(f"Stos wyjątku:")
        traceback.print_exc()
    except Exception as e:
        print("Nieoczekiwany wyjątek!")
        print(f"Typ wyjątku: {type(e).__name__}")
        print(f"Szczegóły wyjątku: {e}")
        print(f"Stałe wyjątku: {e.__traceback__}")
    else:
        print("Wszystko OK!")
    finally:
        print("Zakończono działanie funkcji\n")

risky_division(10,2)
risky_division(10,0)
risky_division("v",2)

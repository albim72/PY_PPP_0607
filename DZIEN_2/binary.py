def copy_binary_file(source_path, target_path):
    with open (source_path, "rb") as src:
       data = src.read()

    print(f"Odczytano {len(data)} bajtów z {source_path}")

    with open (target_path, "wb") as dst:
        dst.write(data)

    print(f"Zapisano {len(data)} bajtów do {target_path}")

copy_binary_file("planeta.jpg","copy.jpg")

def compare_files(file1,file2):
    with open(file1, "rb") as f1,open(file2, "rb") as f2:
        data1 = f1.read()
        data2 = f2.read()
        if data1 == data2:
            print("Pliki są identyczne")
        else:
            print("Pliki są różne")

compare_files("copy.jpg","planeta.jpg")
compare_files("fire.jpg","planeta.jpg")
compare_files("copy.jpg","fire.jpg")

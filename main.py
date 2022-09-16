from math_function import add,div,mul


def main():

    data_1 = int(input("Masukkan input 1(integer) : "))
    data_2 = int(input("Masukkan input 2(integer) : "))
    operator = input("Masukkan operator (+ * /) : ")

    if operator == "+":
        result = add(data_1, data_2)
    elif operator == "*":
        result = mul(data_1, data_2)
    elif operator == "/":
        result = div(data_1, data_2)
    else:
        print("ERROR! Operator salah/tidak ditemukan!")

    print("Hasilnya adalah : {} {} {} = {} ".format(data_1, operator, data_2, result))


if __name__ == "__main__":
    print("Hello Main !")
    main()
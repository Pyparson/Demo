

def test_print():

    i = (1)
    print(type(i))
    if "int" in str(type(i)):
        print("====one====")
        print(i)
        print("====one====")
    else:
        print("====two====")
        for j in i:
            print(j)
        print("====two====")


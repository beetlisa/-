def read_number(s):

    try:

        res = int(s)

        return res

    except ValueError:

        return "Error"

    finally:

        print("Done")



print(read_number("10"))

print(read_number("abc"))
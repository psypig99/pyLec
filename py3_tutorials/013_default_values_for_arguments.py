def get_gender(sex="unknown"):
    if sex is ("m" or "male"):
        sex = "male"
    elif sex is ("f" or "female"):
        sex = "female"

    print(sex)


get_gender("m")
get_gender("f")
get_gender()
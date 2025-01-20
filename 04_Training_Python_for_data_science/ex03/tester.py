from new_student import Student


def main():

    try:
        student = Student(name="Edward", surname="agle")
        print(student)
    except Exception as e:
        print(e)

    try:
        error1 = Student(name="Edward", surname="agle", login="eagle")
        print(error1)
    except Exception as e:
        print(e)

    try:
        error2 = Student(name="Edward", surname="agle", bla="eagle", heu="re")
        print(error2)
    except Exception as e:
        print(e)

    try:
        error3 = Student(name="Edward")
        print(error3)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()

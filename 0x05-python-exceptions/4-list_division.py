#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    my_list = []
    for i in range(list_length):
        try:
            my_list.append(my_list_1[i]/my_list_2[i])
        except ZeroDivisionError:
            my_list.append(0)
            print("division by 0")
            continue
        except TypeError:
            my_list.append(0)
            print("wrong type")
            continue
        except IndexError:
            my_list.append(0)
            print("out of range")
            continue
        finally:
            pass

    return my_list

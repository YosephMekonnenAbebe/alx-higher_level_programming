#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    yoseph_list = []
    for yosephi in range(list_length):
        try:
            yoseph_result = my_list_1[yosephi] / my_list_2[yosephi]
        except (ValueError, TypeError):
            print("wrong type")
            yoseph_result = 0
        except ZeroDivisionError:
            print("division by 0")
            yoseph_result = 0
        except IndexError:
            print("out of range")
            yoseph_result = 0
        finally:
            yoseph_list.append(yoseph_result)
    return yoseph_list

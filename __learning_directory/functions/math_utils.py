import timeit


def is_power_of_two(input_number: int) -> bool:
    return input_number and not (input_number & (input_number - 1))


a_power_of_two_number = 3273390607896141870013189696827599152216642046043064789483291368096133796404674554883270092325904157150886684127560071009217256545885393053328527589376  # noqa:E501

start_time = timeit.default_timer()
print(is_power_of_two(a_power_of_two_number))
print(timeit.default_timer() - start_time)

def fibonacci(n):
    if n > 1:
        first_fib = 0
        second_fib = 1
        num_of_sequences = 0
        while num_of_sequences < n:
            next_num_in_seq = first_fib + second_fib
            first_fib = second_fib
            second_fib = next_num_in_seq
            num_of_sequences += 1
        return first_fib


def double_investment(principle, rate):
    start = 0
    end = (principle * 2)
    acc = 0
    while start < end:
        start = principle * (1 + rate)
        principle = start
        acc += 1
        if start >= end:
            break
    return acc


def syracuse(n):
    starting_list = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
            starting_list.append(n)
        else:
            n = (3 * n) + 1
            starting_list.append(n)
    return starting_list


def goldbach(n):
    pass


if __name__ == '__main__':
    pass

    # fibonacci(4)
    # double_investment(10, 0.10)

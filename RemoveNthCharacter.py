def remove_nth_char(str, n):
    first_part = str[:n]
    last_part = str[n+1:]
    return first_part + last_part


print(remove_nth_char('python', 1))
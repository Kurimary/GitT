def get_full_time(experience):
    salary = 30000
    if experience > 2 and experience < 5:
        salary*=1.2
    elif experience >= 5:
        salary*=1.5
    return salary


exp = 5
result = get_full_time(exp)
print(result)


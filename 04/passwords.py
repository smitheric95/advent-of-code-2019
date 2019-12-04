def valid_password(password):
    contains_pair = False
    i, j = 0, 1

    while j < len(password):
        if password[i] == password[j] and password.count(password[i]) == 2:
            contains_pair = True
        elif password[j] < password[i]:
            return False
        
        i += 1
        j += 1
    
    return True if contains_pair else False
                
def num_passwords(a, b):
    # generate all passwords in range
    passwords = list(range(a, b+1))
    good_passwords = []

    # filter out those that don't meet the criteria
    for password in passwords:
        if valid_password(str(password)):
            good_passwords.append(password)

    return good_passwords

if __name__ == "__main__":
    # print(valid_password(str(112222)))
    print(len(num_passwords(152085, 670283)))
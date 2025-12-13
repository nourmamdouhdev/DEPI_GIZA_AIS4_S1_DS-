email = "Amit_ml@gmail.edu"

if email.count("@") != 1 or "." not in email[email.index("@"):]:
    print("not coorect email")
else:
    username = email[:email.index("@")]

    domain = email[email.index("@") + 1:email.rindex(".")]

    if email.endswith(".com"):
        domain_type = "com Domain"
    elif email.endswith(".edu"):
        domain_type = "edu Domain"
    else:
        domain_type = "other Domain"

    print("Username:", username)
    print("Domain:", domain)
    print("Domain Type:", domain_type)

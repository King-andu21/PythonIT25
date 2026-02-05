def banner(lause):
    return lause.upper()
print(banner("hello blud"))
amount = int(input("mitu korda soovid näha bannerit: "))
lause = input("millist lauset kuvada:")
for i in range(amount):
    print(banner(lause))

# test
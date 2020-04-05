#while True:#reply = input('Enter text:')#if reply == 'stop': breakprint('reply.upper()')



def outer():
    x = "local"
    print("OK:", x)
    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)

    inner()
    print("no:", x)
outer()


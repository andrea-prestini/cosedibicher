def messaggio(f):
    def wrapper():
        print("About to run the function...")
        f()
        print("Done with the function")
    return wrapper

    
@messaggio
def hello():
    print("Hello, World!")

    
hello()
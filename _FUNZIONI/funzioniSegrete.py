def private(func):
    func.private = True
    return func

@private
def secret():
    return 'segreta'


def not_secret():
    return 'non segreta'


for func in secret, not_secret:
    is_private = getattr(func, 'private', False)
    if not is_private:
        print(func()) 
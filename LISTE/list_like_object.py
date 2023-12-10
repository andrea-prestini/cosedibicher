class ASAPmob:

    def __init__(self):

        self._members = [
            "ASAP Ant",
            "ASAP Bari",
            "ASAP Ferg",
            "ASAP Illz",
            "ASAP Lotto",
            "ASAP Lou Banga",
            "ASAP Nast",
            "ASAP P on the Boards",
            "ASAP Relli",
            "ASAP Rocky",
            "ASAP Snacks",
            "ASAP Twelvyy",
            "ASAP Ty Beats",
            "ASAP TyY",
            "ASAP Trash Panda",
        ]

    def __len__(self):

        return len(self._members)

    def __getitem__(self, key):

        if isinstance(key, int):
            return self._members.pop(key)
        raise TypeError("Cannot get key %s" % key)

    def __contains__(self, member):

        return member in self._members

    def __iter__(self):

        while self._members:
            yield self._members.pop()


asap_mob = ASAPmob()
print("There are %d members in ASAP" % len(asap_mob))
print("-" * 40)

print("%s goes solo!" % asap_mob[0])
print("-" * 40)

print("There are now %d only members in the ASAP" % len(asap_mob))
print("-" * 40)

if "ASAP Relli" in asap_mob:
    print("It's IN...")
else:
    print("NOT present in ASAP...")
print("-" * 40)

for member in asap_mob:
    print(member)
print("-" * 40)
print("There are now %d only members in the ASAP" % len(asap_mob))

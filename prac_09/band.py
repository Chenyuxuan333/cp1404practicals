class Band:
    """A class to represent a band composed of musicians."""

    def __init__(self, name):
        """Initialize a Band with a name and an empty list of members."""
        self.name = name
        self.members = []

    def add_member(self, musician):
        """Add a musician to the band."""
        self.members.append(musician)

    def play(self):
        """
        Make all members of the band play their instruments.
        Returns a list of strings describing each member's action.
        """
        performance = []
        for member in self.members:
            performance.append(member.play())
        return performance

    def __str__(self):
        """Return a string representation of the band and its members."""
        if not self.members:
            return f"Band: {self.name} (no members)"

        member_names = ", ".join([member.name for member in self.members])
        return f"Band: {self.name}, Members: {member_names}"


# --- Example usage ---
if __name__ == '__main__':

    # Create some musicians
    guitarist = Musician("Jimi Hendrix")
    bassist = Musician("Flea")
    drummer = Musician("Dave Grohl")

    # Add instruments to musicians
    guitarist.add_instrument(Guitar("Fender Stratocaster", 1500.00))
    bassist.add_instrument(Guitar("Music Man StingRay", 2000.00))
    # The drummer has no instruments

    # Create a band and add members
    my_band = Band("The Awesome Band")
    my_band.add_member(guitarist)
    my_band.add_member(bassist)
    my_band.add_member(drummer)

    # Print the band's details
    print(my_band)
    print()

    # Make the band play
    print("Band is playing:")
    for action in my_band.play():
        print(action)

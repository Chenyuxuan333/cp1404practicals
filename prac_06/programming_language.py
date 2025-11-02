class ProgrammingLanguage:
    """Represent a programming language."""

    def __init__(self, name, typing, reflection, year):
        """Initialize a ProgrammingLanguage instance.

        name: string, the name of the programming language
        typing: string, the type system (Static/Dynamic)
        reflection: boolean, whether the language supports reflection
        year: integer, the year the language first appeared
        """
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Check if the language is dynamically typed. Return boolean."""
        return self.typing == "Dynamic"

    def __str__(self):
        """Return a formatted string representation."""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"
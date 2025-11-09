"""
CP1404/CP5632 Practical - Programming Language class with tests.
Represents programming languages with name, typing, reflection support,
first appeared year, and pointer arithmetic support.
"""


class ProgrammingLanguage:
    """Represent information about a programming language, including pointer arithmetic support."""

    def __init__(self, name, typing, reflection, year, pointer_arithmetic):
        """Construct a ProgrammingLanguage from the given values.

        Parameters:
            name (str): Name of the programming language
            typing (str): Type of typing (e.g., "Dynamic" or "Static")
            reflection (bool): Whether the language supports reflection
            year (int): Year the language first appeared
            pointer_arithmetic (bool): Whether the language supports pointer arithmetic
        """
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year
        self.pointer_arithmetic = pointer_arithmetic

    def __repr__(self):
        """Return string representation of a ProgrammingLanguage."""
        return (f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, "
                f"First appeared in {self.year}, Pointer Arithmetic={self.pointer_arithmetic}")

    def is_dynamic(self):
        """Determine if language is dynamically typed."""
        return self.typing == "Dynamic"

    def has_pointer_arithmetic(self):
        """Check if the language supports pointer arithmetic."""
        return self.pointer_arithmetic


def run_tests():
    """Run simple tests/demos on ProgrammingLanguage class."""
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995, False)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991, False)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991, False)
    c_plus_plus = ProgrammingLanguage("C++", "Static", False, 1983, True)

    languages = [ruby, python, visual_basic, c_plus_plus]
    print(python)

    print("\nThe dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)

    print("\nLanguages with pointer arithmetic:")
    for language in languages:
        if language.has_pointer_arithmetic():
            print(language.name)


if __name__ == "__main__":
    run_tests()
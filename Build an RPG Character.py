def create_character(char_name: str, strength: int, intelligence: int, charisma: int, /):
    full_dot = '●'
    empty_dot = '○'

    # Name validations
    if not isinstance(char_name, str):
        return "The character name should be a string"
    if not char_name:
        return "The character should have a name"
    if len(char_name) > 10:
        return "The character name is too long"
    if " " in char_name:
        return "The character name should not contain spaces"

    # Stats validations
    stats = (strength, intelligence, charisma)
    if not all(isinstance(stat, int) for stat in stats):
        return "All stats should be integers"
    if not all(stat >= 1 for stat in stats):
        return "All stats should be no less than 1"
    if not all(stat <= 4 for stat in stats):
        return "All stats should be no more than 4"
    if sum(stats) != 7:
        return "The character should start with 7 points"

    # Build stats lines
    str_line = "STR " + full_dot * strength + empty_dot * (10 - strength)
    int_line = "INT " + full_dot * intelligence + empty_dot * (10 - intelligence)
    cha_line = "CHA " + full_dot * charisma + empty_dot * (10 - charisma)

    # Combine everything into one string
    return f"{char_name}\n{str_line}\n{int_line}\n{cha_line}"

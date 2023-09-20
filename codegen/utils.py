
def to_snake_case_from_kebob(name):
    return "_".join([c.lower() for c in name.split("-")])


def to_pascal_case_from_snake(name):
    return "".join([c.title() for c in name.split("_")])


def indent(string, num_spaces):
    # https://www.oreilly.com/library/view/python-cookbook/0596001673/ch03s12.html
    return "\n".join([(num_spaces * " ") + line for line in string.split("\n")])



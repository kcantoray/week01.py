def add(
  first_name: str,
  last_name: str,
  role: str,
  underlying: list[list[str]]
) -> None:
  """Add a new character record to the underlying list."""
  underlying.append([first_name, last_name, role])


def add_unique_first_name(
  first_name: str,
  last_name: str,
  role: str,
  underlying: list[list[str]]
) -> None:
  """Add a record if the first name is not already in the list."""

  found = False
  
  for character in underlying:
    if character[0] == first_name:
      found = True

if not found:
  add(first_name, last_name, role, underlying)

add_unique_first_name("Jim", "Byers", "Test", st_characters)
add_unique_first_name("Lucas", "Sinclair", "Friend", st_characters)

print(st_characters)


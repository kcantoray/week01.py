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

def add_unique_last_name(
    first_name: str,
    last_name: str,
    role: str,
    underlying: list[list[str]]
) -> None:
    """Add a record if the last name is not already in the list."""

    found = False

    for character in underlying:
        if character[1] == last_name:
            found = True

    if found == False:
        add(first_name, last_name, role, underlying)

def remove_first_name(
  first_name: str,
  underlying: list[list[str]]
) -> str | None:
  """Remove and return the first record with the given first name."""

  found = False
  index = 0
  result = None

  for i in range(len(underlying)):
    if underlying[i][0] == first_name:
        if found == False:
            found = True
            index = i

  if found:
      result = underlying.pop(index)

  return result

def remove_all_first_name(
  first_name: str,
  underlying: list[list[str]]
) -> list[list[str]] | None:
  """Remove and return all records with the given first name."""

  removed = []
  i = 0

  while i < len(underlying):
    if underlying[i][0] == first_name:
      removed.append(underlying.pop(i))
    else:
      i += 1

  if len(removed) == 0:
    result = None
  else:
    result = removed

  return result

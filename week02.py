def add(
  first_name: str,
  last_name: str,
  role: str,
  underlying: list[list[str]]
) -> None:
  """Add a new character record to the underlying list."""
  underlying.append([first_name, last_name, role])

st_characters = [
    ["Jim", "Hopper", "Chief of Police"],
    ["Eleven", "", "Psychokinetic Overachiever"],
    ["Dustin", "Henderson", "Science Enthusiast"]
]

add("Yuri", "Ismaylov", "Smuggler", st_characters)

print(st_characters)

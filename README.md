# 50.007-machine-learning

## Guide
Q: I faced this error: `UnicodeDecodeError: 'charmap' codec can't decode byte 0x9d in position 4193: character maps to <undefined>`. How do I resolve this issue?

A: You will need to add the parameter `encoding="utf8"` in the `open()` function.

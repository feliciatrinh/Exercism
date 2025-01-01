# Isogram

Welcome to Isogram on Exercism's Python Track.
If you need help running the tests or submitting your code, check out `HELP.md`.

## Instructions

Determine if a word or phrase is an isogram.

An isogram (also known as a "non-pattern word") is a word or phrase without a repeating letter, however spaces and hyphens are allowed to appear multiple times.

Examples of isograms:

- lumberjacks
- background
- downstream
- six-year-old

The word _isograms_, however, is not an isogram, because the s repeats.

## Source

### Created by

- @behrtam

### Contributed to by

- @abhijitparida
- @cmccandless
- @Dog
- @ikhadykin
- @N-Parsons
- @Nishant23
- @olufotebig
- @rever0f
- @sdublish
- @thomasjpfan
- @tqa236
- @yawpitch

### Based on

Wikipedia - https://en.wikipedia.org/wiki/Isogram

### Notes
Solution 1
- You could create a dictionary to keep track of how many times each character appears
- you wouldn't add hyphens or spaces
- as soon as a character appears more than one i.e. it's already in the dictionary, you could return false
- case isn't specified so let's make it all lowercase just in case
- this solution assumed that only letters, spaces, and hyphens are allowed

Solution 2
- lowercase everything
- Use regex to capture all of the letters
- turn that into a set and check if the number of letters is equal to the size of the set
- you could also just replace the spaces and hyphens instead of using regex

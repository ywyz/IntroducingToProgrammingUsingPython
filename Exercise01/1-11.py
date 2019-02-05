time = 365 * 24 * 60 * 60
ft = 3120324986 + time // 7 - time // 13 + time // 45       # First year
print("The first year: ", ft)
sd = ft + time // 7 - time // 13 + time // 45              # Second year
print("The second year: ", sd)
td = sd + time // 7 - time // 13 + time // 45            # Third year
print("The third year: ", td)
fh = td + time // 7 - time // 13 + time // 4              # Fouth year
print("The fourth year: ", fh)
ft = fh + time // 7 - time // 13 + time // 4               # Fifth year
print("The fifth year: ", ft)

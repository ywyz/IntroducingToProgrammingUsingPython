firstday = 6
total = 6
print('{:>30}'.format('January 2005'))
print("----------------------------------------------------")
print('{:>6}'.format('Sun'), '{:>6}'.format('Mon'), '{:>6}'.format('Tue'),
      '{:>6}'.format('Wed'), '{:>6}'.format('Thu'), '{:>6}'.format('Fri'),
      '{:>6}'.format('Sat'))
for number in range(0, 7):
    if firstday >= number:
        print('{:>5}'.format(''), end=" ")
        total += 1
        continue
for n in range(1, 32):
    print('{:>3}'.format(n), end="    ")
    total += 1
    if total % 7 == 0:
        print("\n")

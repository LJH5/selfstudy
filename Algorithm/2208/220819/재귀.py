def asd(x):
    print('#', end='')
    if x == 3:
        print('#', end='')
        return
    print('#', end='')
    asd(x+1)

asd(0)

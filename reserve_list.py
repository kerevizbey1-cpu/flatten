def reverse_list(liste):
    liste = liste[::-1]
    for i in range(len(liste)):
        if isinstance(liste[i], list):
            liste[i] = reverse_list(liste[i])
    return liste

# Test:
data = [[1, 2], [3, 4], [5, 6, 7]]
print(reverse_list(data))

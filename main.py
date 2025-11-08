def flatten(liste):
    result = []
    for eleman in liste:
        if isinstance(eleman, list):
            result.extend(flatten(eleman))
        else:
            result.append(eleman)
    return result


def reverse_list(liste):
    liste = liste[::-1]
    for i in range(len(liste)):
        if isinstance(liste[i], list):
            liste[i] = reverse_list(liste[i])
    return liste

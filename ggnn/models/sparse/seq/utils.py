def top_k_prod(vals, k):
    #  vals has to be of shape [depth, num_vals, 2]
    #  complexity of this procedure is O(depth * k^2)
    depth = len(vals)
    worklist = [[[i[0]], i[1], [i[1]]] for i in vals[0]]
    for d in range(1, depth):
        layer = vals[d]
        new_vals = []
        for i in layer:
            for j in worklist:
                new_vals.append([j[0] + [i[0]], j[1] * i[1], j[2] + [i[1]]])

        worklist = list(reversed(sorted(new_vals, key=lambda x: x[1])))[:k]

    return worklist

print(top_k_prod([
    [(1, 0.14), (2, 0.03), (3, 0.025)],
    [(4, 0.5), (5, 0.2), (6, 0.001)],
    [(7, 0.8), (8, 0.023), (9, 0.0001)]
], 3))

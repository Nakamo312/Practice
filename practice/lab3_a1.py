from math import exp
cij = 3.7
def vol_mat():
    matrix = [[  0.1,  0.2,   0.1, 0.025,   0.2, 0.05, 0.025,  0.05,  0.05],
              [0.025,  0.2,   0.1, 0.025,   0.2,  0.1,   0.1,  0.05,   0.1],
              [0.025,  0.2,   0.1, 0.025, 0.025,  0.1,   0.1,   0.2, 0.025],
              [ 0.05,  0.1,   0.2, 0.025, 0.025,  0.1, 0.025, 0.025,   0.1],
              [ 0.05,  0.1,   0.2,   0.2,  0.05,  0.2, 0.025, 0.025,  0.02],
              [  0.1, 0.05, 0.025,   0.2,  0.05,  0.2,   0.2,   0.2,  0.05],
              [  0.2, 0.05, 0.025,   0.2, 0.025,  0.1,   0.2,   0.2,  0.05],
              [  0.2, 0.05,   0.2,   0.2, 0.025, 0.05,   0.1, 0.025,   0.2],
              [  0.2,0.025, 0.025,  0.05,   0.2, 0.05, 0.025,   0.2,   0.2]]
    return matrix
def dist_mat():

    matrix = [[         0, 30 + cij,  40 + cij,  30 + cij, 45 + cij, 50 + cij, 30 + cij, 50 + cij, 120 + cij],
              [  30 + cij,        0,  10 + cij,  20 + cij, 20 + cij, 25 + cij, 30 + cij, 40 + cij,  90 + cij],
              [  40 + cij, 10 + cij,         0,  10 + cij, 15 + cij, 20 + cij, 25 + cij, 25 + cij,  90 + cij],
              [  30 + cij, 20 + cij,  10 + cij,         0, 10 + cij, 15 + cij, 25 + cij, 25 + cij,  90 + cij],
              [  45 + cij, 20 + cij,  15 + cij,  10 + cij,        0, 20 + cij, 15 + cij, 25 + cij,  90 + cij],
              [  50 + cij, 25 + cij,  20 + cij,  15 + cij, 20 + cij,        0, 10 + cij, 20 + cij,  80 + cij],
              [  30 + cij, 30 + cij,  25 + cij,  25 + cij, 15 + cij, 10 + cij,       0 , 15 + cij,  70 + cij],
              [  50 + cij, 40 + cij,  25 + cij,  25 + cij, 25+ cij,   20 + cij, 15 + cij,        0,  50 + cij],
              [ 120 + cij, 90 + cij,  90 + cij,  90 + cij, 90 + cij, 80 + cij, 70 + cij, 50 + cij,        0]]
    return matrix
def cor_matrix():
    matrix = []
    for i in range(9):
        lst = []
        for j in range(9):
            if i != j:
                lst.append(pow(vol_mat()[i][j], 2) * 1 / pow(dist_mat()[i][j], 2))
            else:
                lst.append(0)
        matrix.append(lst)
    return matrix
mat = cor_matrix()
for i in mat:
    print(i)
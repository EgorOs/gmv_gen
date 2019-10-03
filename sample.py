import matplotlib.pyplot as plt
import numpy as np
from numpy.fft import fft, ifft, fftshift, fftfreq
from scipy.signal import max_len_seq
from collections import deque


# Расчёт автокорреляции здесь же
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.max_len_seq.html


class FieldCreator:

    def make_matrix(self, order, seed=None, check_coeffs=None):
        seq = max_len_seq(order, state=seed, taps=check_coeffs)[0]
        J = order + 1
        S = int(len(seq) / J)
        F_MP = seq.reshape(J,S)
        return F_MP

    def make_shift_table_from_seq(self, seq):
        seq = deque(seq.copy())
        shift_table = dict()
        for i in range(len(seq))[::-1]:
            seq.rotate(-1)
            shift_table[i] = seq.copy()
        return shift_table

    def make_shift_table_from_matrix(self, matrix, col_idx):
        J, S = matrix.shape
        selected_col = deque(matrix[:,col_idx])
        shift_table = dict()
        for i in range(len(selected_col))[::-1]:
            selected_col.rotate(-1)
            shift_table[i] = selected_col.copy()
        return shift_table

    def make_rule(self, matrix, shift_table):
        J, S = matrix.shape
        I_MP = []
        for j in range(1, S):
            col = matrix[:, j]
            for idx in range(J):
                if all(col == shift_table[idx]):
                    I_MP.append(idx)
        return I_MP

    def make_gmw(self, order, rule, seq):
        shift_table = self.make_shift_table_from_seq(seq)
        J = order + 1
        F_GMW = [[0] * J]
        for i in rule:
            F_GMW.append(list(shift_table[i]))
        return np.array(F_GMW).T


fc = FieldCreator()
seed = [0, 0, 0, 0, 0, 1]
check_coeffs = [6, 1, 0]
order = 6
seq = max_len_seq(order, state=seed, taps=check_coeffs)[0]
F_MP_1 = fc.make_matrix(order, seed=seed, check_coeffs=check_coeffs)
st_1 = fc.make_shift_table_from_matrix(F_MP_1, 3)
I_MP = fc.make_rule(F_MP_1, st_1)

F_MP_2 = fc.make_matrix(order, seed=seed, check_coeffs=[6,2,0])

seq = max_len_seq(3, state=[0,0,1], taps=[3,1,0])[0]
F_GMW = fc.make_gmw(order, I_MP, seq)

spec = fft(seq)
N = len(seq)
plt.plot(fftshift(fftfreq(N)), fftshift(np.abs(spec)), '.-')
plt.margins(0.1, 0.1)
plt.grid(True)
plt.show()
"""Experiment: Determine similarities between D8 and Y(2+2) groups
"""

from sympy.combinatorics import DihedralGroup, SymmetricGroup

from mathtools.comb.young import YoungTableau
from mathtools.groups import iso, young


def create_s4():
	"""Create S4 group"""
	return SymmetricGroup(4)


def create_d8():
	"""Create D8 group"""
	return DihedralGroup(4)


def create_y22():
	"""Create Y(2+2) group

	Young Symmetrizer group generated by Riemann Tensor index symmetries
	"""
	yt = YoungTableau("2 + 2", zero_indexed=True)
	return young.group(yt)


def create_y22_row_fused():
	"""Create Y(2+2)_R group

	Young Symmetrizer group generated by Riemann Tensor index symmetries
	"""
	yt = YoungTableau("2 + 2", zero_indexed=True)
	return young.group(yt, include_fused_rows=True, include_cols=False)


# return PermutationGroup([
# 	Permutation(1, 2),  # symmetrize 1st and 2nd indices
# 	Permutation(3, 4),  # symmetrize 3rd and 4th indices
# 	Permutation(1, 3)(2, 4)  # symmetrize 1st and 2nd pairs of indices, (1 and 2) with (3 and 4)
# ])


def check_iso(A, B, a_name, b_name, verbose: bool = False):
	possible = iso.is_iso_possible(A, B)
	print(f"Is isomorphism possible: {a_name} and {b_name}? {possible}")

	if not possible:
		return

	print("Finding isomorphism by element orders")
	f = iso.find_iso_by_element_orders(A, B)

	if f is None:
		print("No isomorphism found by element orders")
	else:
		print("Isomorphism found by element orders!")

		if verbose:
			print('Isomorphism:')
			for k, v in f.items():
				print(f"{k} -> {v}")


def main():
	"""Main function"""
	check_iso(create_y22(), create_d8(), "Y(2+2)", "D8")
	print()

	check_iso(create_y22(), create_s4(), "Y(2+2)", "S4")
	print()

	check_iso(create_y22_row_fused(), create_d8(), "Y(2+2)_R", "D8")


if __name__ == '__main__':
	main()

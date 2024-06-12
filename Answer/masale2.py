from math import sqrt

def main():
	meydan_x = 0
	meydan_y = 0
	toolO = 0
	arzO = 0


	tool = int(input("طول زمین را وارد کنید :"))
	arz = int(input("لطفا عرض زمین را وارد کنید :"))


	arr = [[0 for x in range(int(arz))] for y in range(int(tool))]


	for i in range(0, tool):
		for j in range(0, arz):
			arr[i][j] = input(f"[{i + 1}][{j + 1}] ")
			if arr[i][j] == "O" or arr[i][j] == "o":
				toolO = i
				arzO = j

	for i in range(0, tool):
		for j in range(0, arz):

			if i == toolO and j == arzO: #خانه O
				continue
			else:
				r2 = (i - toolO) ** 2 + (j - arzO) ** 2
				if r2 == 0:
					continue
				p_e = int(arr[i][j]) / (r2)
				meydan_x += p_e * ((i - toolO) / sqrt(r2))
				meydan_y += p_e * ((j - arzO) / sqrt(r2))

	print()
	print(meydan_x, meydan_y)

	with open("2", "w") as file:
		file.write(f"{meydan_x}, {meydan_y}")
	
main()
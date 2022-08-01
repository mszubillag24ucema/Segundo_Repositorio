# Ejercicio 12 - Certificado IELTS - usando for 

students = ["37128693", "38346828", "38122921", "38915457", "46655903", "46988530", "28498292", "37538741", "45788239", "36998322", "37570846", "30401721", "42223891", "40210778", "22981717", "27744330", "25916934", "41595563", "36107300", "41367347", "48577851", "24807285", "25145603", "21332845", "32098132", "34832996", "33530381", "44855039", "23571241", "23923908", "23747794", "46033685", "28372488", "33143443", "35759559", "21061055", "33613272", "24082600", "26477319", "35368988", "25393784", "21295674", "48348316", "31247247", "27557703", "24435687", "38794110", "44518399", "34178717", "22185788", "25030083", "21256524", "34592517", "41755997", "47330519", "34380715", "42724546", "26615771", "23171192", "20478110", "20753240", "28187999", "27785500", "37236996", "36552090", "36824210", "39684157", "26469844", "45037525", "30552911", "40100736", "36047292", "46818813", "36680587"]
student_marks = [15, 19, 19, 9, 6, 12, 20, 3, 1, 15, 10, 16, 3, 25, 18, 13, 24, 30, 7, 28, 20, 25, 28, 10, 2, 1, 18, 20, 3, 3, 19, 12, 11, 8, 24, 27, 15, 15, 19, 0, 27, 8, 29, 5, 1, 12, 8, 17, 19, 0, 0, 18, 15, 23, 22, 2, 24, 6, 10, 28, 18, 3, 15, 6, 26, 0, 21, 14, 24, 13, 10, 17, 16, 2]

my_document = "40210778"
index = 0
found_document_index = 0

advanced = 0
high_intermediate = 0
low_intermediate = 0
elementary = 0
low_elementary = 0

for student in students:
	if student == my_document:
		found_document_index = index
	index += 1

print(f"\nEstudiante: {my_document} | nota: {student_marks[found_document_index]}")

for mark in student_marks:
	if mark >= 0 and mark <= 9:
		low_elementary += 1
	elif mark <= 15:
		elementary += 1
	elif mark <= 19:
		low_intermediate += 1
	elif mark <= 24:
		high_intermediate += 1
	else:
		advanced += 1

print("\nTotal resultados por categoria")
print(f"Avanzado: {advanced}")
print(f"Intermedio alto: {high_intermediate}")
print(f"Intermedio bajo: {low_intermediate}")
print(f"Basico: {elementary}")
print(f"Por debajo del basico: {low_elementary}")

print(f"\nTotal de estudiantes: {len(students)}")

print("------------------------\n")
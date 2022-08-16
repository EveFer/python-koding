print('Programa que permite obtener el promedio\n')

score_practice_1 = float(input('Calificación de practica #1: '))
score_practice_2 = float(input('Calificación de practica #2: '))
score_practice_3 = float(input('Calificación de practica #3: '))

score_exam_partial = float(input('Calificación del examen parcial: '))
score_exam_final = float(input('Calificación del examen final: '))


average_practices = (score_practice_1 + score_practice_2 + score_practice_3) / 3

average = (average_practices + 2 * score_exam_partial + 3 * score_exam_final ) / 6

print('El promedio es: ', average)

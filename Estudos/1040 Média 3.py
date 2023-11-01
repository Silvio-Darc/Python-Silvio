entrada = str.split(input())
n1 = float(entrada[0])
n2 = float(entrada[1])
n3 = float(entrada[2])
n4 = float(entrada[3])
media = ((n1 * 2) + (n2 * 3) + (n3 * 4) + n4) / 10

print("Media: {:.1f}".format(media))

if media >= 7.0:
    print("Aluno aprovado.")
elif media >= 5.0:
    print("Aluno em exame.")
    exame = float(input())
    media_final = (exame + media) / 2
    print("Nota do exame: {:.1f}".format(exame))
    if media_final >= 5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print("Media final: {:.1f}".format(media_final))

else:
    print("Aluno reprovado.")

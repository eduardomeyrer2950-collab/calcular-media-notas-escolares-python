def calcular_media():
    qtd = int(input("Quantas notas quer informar? "))
    soma = 0

    for i in range(1, qtd + 1):
        nota = float(input(f"Digite a nota {i}: "))
        soma += nota

    media = soma / qtd
    print(f"\nMédia final: {media:.1f}")

    if media >= 7:
        print("✅ Aprovado!")
    elif media >= 5:
        print("⚠️ Recuperação.")
    else:
        print("❌ Reprovado.")

if __name__ == "__main__":
    calcular_media()

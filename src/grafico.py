import csv
import matplotlib.pyplot as plt

def plotar():
    numeros = []
    valores = []

    with open("contagem.csv") as f:
        reader = csv.DictReader(f)
        for row in reader:
            numeros.append(int(row["numero"]))
            valores.append(int(row["quantidade"]))

    # Estatísticas básicas
    minimo = min(valores)
    maximo = max(valores)

    print(f"Menor valor: {minimo}")
    print(f"Maior valor: {maximo}")

    # Margem para não cortar seco
    margem = (maximo - minimo) * 0.2 if maximo != minimo else 1

    plt.figure()

    # Barras mais finas
    plt.bar(numeros, valores, width=0.4)

    # 🔥 Zoom no eixo Y (começando perto do menor valor)
    plt.ylim(minimo - margem, maximo + margem)

    plt.xlabel("Face do dado")
    plt.ylabel("Frequência")
    plt.title("Distribuição dos lançamentos (zoom)")

    plt.xticks(numeros)

    plt.show()


if __name__ == "__main__":
    plotar()
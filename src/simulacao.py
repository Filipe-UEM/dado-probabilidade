import numpy as np
import csv
import time

def simular_dado(n_lancamentos, salvar_bruto=False):
    inicio = time.time()

    # Geração rápida
    resultados = np.random.randint(1, 7, size=n_lancamentos)

    # Contagem
    contagem = np.bincount(resultados, minlength=7)[1:]

    # Probabilidade esperada
    p = 1 / 6
    esperado = n_lancamentos * p

    # Desvio padrão teórico (binomial)
    desvio_teorico = np.sqrt(n_lancamentos * p * (1 - p))

    # Qui-quadrado
    chi2 = np.sum((contagem - esperado) ** 2 / esperado)

    fim = time.time()

    print(f"Tempo: {fim - inicio:.2f}s\n")

    print("Número | Observado | Esperado | Diferença")
    for i, obs in enumerate(contagem, start=1):
        print(f"{i:^6} | {obs:^9} | {esperado:^8.0f} | {obs - esperado:+}")

    print(f"\nDesvio padrão esperado: {desvio_teorico:.2f}")
    print(f"Qui-quadrado: {chi2:.2f}")

    # Salva contagem
    with open("contagem.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["numero", "quantidade"])
        for i, qtd in enumerate(contagem, start=1):
            writer.writerow([i, int(qtd)])

    # ⚠️ Opcional: salvar resultados brutos
    if salvar_bruto:
        print("\nSalvando resultados brutos (isso pode demorar)...")

        with open("lancamentos.csv", "w") as f:
            f.write(",".join(map(str, resultados)))

    print("\nArquivos gerados:")
    print("- contagem.csv")
    if salvar_bruto:
        print("- lancamentos.csv")


if __name__ == "__main__":
    simular_dado(1_000_000, salvar_bruto=True)
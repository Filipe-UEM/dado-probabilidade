import numpy as np
import matplotlib.pyplot as plt

def simular_master(n_rodadas=100, n_lancamentos=1_000_000):
    acumulado = np.zeros(6, dtype=np.int64)

    plt.figure()

    for rodada in range(1, n_rodadas + 1):
        # Simulação rápida
        resultados = np.random.randint(1, 7, size=n_lancamentos)

        contagem = np.bincount(resultados, minlength=7)[1:]

        # Soma no acumulado global
        acumulado += contagem

        # 🔹 Normaliza para proporção (melhor pra comparar)
        proporcao = acumulado / acumulado.sum()

        # 🔹 Sobreposição com transparência
        plt.plot(range(1, 7), proporcao, alpha=0.1)

        if rodada % 10 == 0:
            print(f"Rodada {rodada} concluída")

    # 🔥 Resultado final destacado
    plt.plot(range(1, 7), proporcao, linewidth=3, label="Final")

    plt.xlabel("Face do dado")
    plt.ylabel("Probabilidade acumulada")
    plt.title("Convergência das probabilidades (simulação massiva)")
    plt.xticks(range(1, 7))
    plt.legend()

    plt.show()

    # 🔹 Resultado final
    mais_frequente = np.argmax(acumulado) + 1

    print("\nResultado final acumulado:")
    for i, v in enumerate(acumulado, start=1):
        print(f"{i}: {v}")

    print(f"\nNúmero que mais saiu: {mais_frequente}")


if __name__ == "__main__":
    simular_master()
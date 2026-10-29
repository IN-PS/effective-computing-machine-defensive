#!/usr/bin/env python3
"""Estimativas de ordem de grandeza usadas na avaliação de viabilidade (S1).

Todos os resultados são TEÓRICOS [T]: modelos simplificados, com hipóteses
declaradas em cada bloco. Servem para dimensionar ordens de grandeza e
identificar gargalos físicos, NUNCA como critério de projeto ou para
justificar qualquer ensaio com pessoas, quedas ou lançamento.

Uso: python3 analises/ordens_de_grandeza.py
Sem dependências externas. Unidades SI em todo o código.
"""

import math

G = 9.81  # m/s²

# Propriedades de referência (ver dados/matriz_materiais_preliminar.csv para fontes).
# sigma: resistência à tração (Pa); E: módulo inicial (Pa); rho: densidade (kg/m³);
# tenac: tenacidade/trabalho de ruptura por volume (J/m³).
MATERIAIS = {
    "Seda MA (Araneus diadematus)": dict(sigma=1.1e9, E=10e9, rho=1300, tenac=160e6),
    "Espidroína recombinante 556 kDa": dict(sigma=1.03e9, E=13.7e9, rho=1300, tenac=114e6),
    "Náilon 6,6 (fibra)": dict(sigma=0.95e9, E=5e9, rho=1140, tenac=80e6),
    "Para-aramida (Kevlar 49)": dict(sigma=3.6e9, E=130e9, rho=1440, tenac=50e6),
    "UHMWPE (faixa comercial)": dict(sigma=3.5e9, E=110e9, rho=970, tenac=None),
}


def tenacidade(m):
    # UHMWPE: sem valor medido localizado; estimativa elástico-linear sigma²/(2E).
    return m["tenac"] if m["tenac"] is not None else m["sigma"] ** 2 / (2 * m["E"])


def bloco_massa():
    print("1) Seção e massa de linha para uma carga ESTÁTICA de referência")
    print("   Hipóteses: carga 687 N (70 kg × g), tração uniaxial pura, sem nós,")
    print("   sem terminações, sem fadiga, sem variabilidade. Fator f = carga de")
    print("   ruptura exigida / carga aplicada. Comprimento ilustrativo: 30 m.\n")
    carga = 70 * G
    comprimento = 30.0
    print(f"   {'Material':34s} {'f':>3s} {'d (mm)':>8s} {'g/m':>7s} {'g/30 m':>8s}")
    for nome, m in MATERIAIS.items():
        for f in (1, 10):
            area = f * carga / m["sigma"]
            d = 2 * math.sqrt(area / math.pi)
            massa_m = area * m["rho"]
            print(f"   {nome:34s} {f:3d} {d*1e3:8.2f} {massa_m*1e3:7.2f} {massa_m*comprimento*1e3:8.0f}")
    print("\n   Massa de 'dope' proteico para a linha de seda com f = 10, 30 m,")
    for solidos in (0.2, 0.3, 0.5):
        area = 10 * carga / MATERIAIS["Seda MA (Araneus diadematus)"]["sigma"]
        massa_fibra = area * 1300 * comprimento
        print(f"   teor de sólidos {solidos:.0%}: ~{massa_fibra / solidos * 1e3:.0f} g de dope")
    print()


def bloco_difusao():
    print("2) Tempo característico de remoção de solvente/água por difusão radial")
    print("   t ≈ r²/D (ordem de grandeza; ignora formação de pele, que o aumenta).")
    print("   D = 1e-10 a 1e-9 m²/s (faixa típica para água em solução polimérica")
    print("   concentrada; hipótese a verificar para cada sistema).\n")
    print(f"   {'raio':>10s} {'t (D=1e-9)':>14s} {'t (D=1e-10)':>14s}")
    for r in (2e-6, 10e-6, 50e-6, 250e-6, 1e-3):
        t1 = r**2 / 1e-9
        t2 = r**2 / 1e-10
        print(f"   {r*1e6:8.0f} µm {t1:12.3g} s {t2:12.3g} s")
    print("\n   Comparação: uma linha que percorre 10 m a 30 m/s fica ~0,33 s no ar.\n")


def bloco_bico():
    print("3) Queda de pressão para extrudar um fluido por um bico cilíndrico")
    print("   Hagen–Poiseuille (newtoniano, laminar): ΔP = 8 μ L v / r².")
    print("   Bico: r = 0,25 mm, L = 10 mm. Fluido pseudoplástico real reduziria μ")
    print("   efetivo, mas o cisalhamento intenso pode solidificar o dope DENTRO do")
    print("   bico (mesmo mecanismo que forma a fibra na glândula).\n")
    r, L = 0.25e-3, 10e-3
    velocidades = (0.015, 1.0, 10.0)
    print(f"   {'μ (Pa·s)':>9s} " + " ".join(f"{'v=' + str(v) + ' m/s':>14s}" for v in velocidades))
    for mu in (1, 100, 1000):
        linha = " ".join(f"{8 * mu * L * v / r**2 / 1e6:11.3g} MPa" for v in velocidades)
        print(f"   {mu:9d} {linha}")
    print("\n   0,015 m/s ≈ velocidade típica de fiação natural do fio de ancoragem")
    print("   (Shao & Vollrath 2002). 1 MPa = 10 bar.\n")


def bloco_dinamico():
    print("4) Carga estática × carga dinâmica (modelo elástico-linear, SEM amortecimento)")
    print("   Objeto de 1 kg em queda livre retido por linha de seção 0,1 mm²,")
    print("   fator de queda h/L = 1 (L = 1 m). F_max = mg + sqrt((mg)² + 2·mg·E·A·h/L).")
    print("   Energia disponível na linha ≈ tenacidade × volume (deformação uniforme).")
    print("   CÁLCULO APENAS — ensaios de queda estão fora do escopo do projeto.\n")
    m, A, L, h = 1.0, 0.1e-6, 1.0, 1.0
    peso = m * G
    energia = m * G * h
    print(f"   Peso estático: {peso:.1f} N; energia de queda: {energia:.1f} J\n")
    print(f"   {'Material':34s} {'F_rup (N)':>9s} {'F_max (N)':>9s} {'E_linha (J)':>11s}")
    for nome, mat in MATERIAIS.items():
        f_rup = mat["sigma"] * A
        f_max = peso + math.sqrt(peso**2 + 2 * peso * mat["E"] * A * h / L)
        e_linha = tenacidade(mat) * A * L
        print(f"   {nome:34s} {f_rup:9.0f} {f_max:9.0f} {e_linha:11.1f}")
    print("\n   Leitura: com carga estática de ~10 N (3–10 % da ruptura), o pico")
    print("   dinâmico ideal supera a ruptura em todos os casos; o critério de")
    print("   energia favorece materiais tenazes. Materiais reais com escoamento e")
    print("   histerese (seda, náilon) fogem do modelo linear — por isso ensaios")
    print("   dinâmicos exigem laboratório equipado, não extrapolação.\n")


def bloco_bancada():
    print("5) Energia armazenada em um corpo de prova típico do ensaio S3")
    print("   Fio fino de náilon: ruptura ~15 N, deformação ~20 %, L0 = 100 mm.")
    f, eps, l0 = 15.0, 0.20, 0.100
    u_lin = 0.5 * f * eps * l0
    print(f"   Energia elástica (aprox. linear): ~{u_lin:.2f} J (limite superior F·ΔL = {f*eps*l0:.2f} J)")
    massa, queda = 1.5, 0.03
    print(f"   Recipiente de carga {massa} kg caindo {queda*100:.0f} cm na bandeja: {massa*G*queda:.2f} J")
    print("   Ordem de grandeza compatível com proteção ocular + anteparo leve.\n")


if __name__ == "__main__":
    bloco_massa()
    bloco_difusao()
    bloco_bico()
    bloco_dinamico()
    bloco_bancada()

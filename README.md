# Cálculo de Salário e FGTS 💸

Este é um projeto simples desenvolvido em Python com interface gráfica (GUI) para auxiliar no cálculo de salário líquido após descontos percentuais e estimativa de valores de FGTS mensal e anual.

## 🚀 Funcionalidades

* **Cálculo de Salário Líquido:** Informa o valor final após aplicar uma porcentagem de desconto customizável.
* **FGTS Mensal:** Calcula automaticamente a alíquota de 8% sobre o salário bruto informado.
* **FGTS Anual:** Fornece uma estimativa do acúmulo de FGTS após 12 meses.
* **Interface Gráfica:** Desenvolvida com Qt Designer para uma experiência de usuário amigável.

## 🛠️ Tecnologias Utilizadas

* **Python 3.x**: Linguagem principal.
* **PySide6 (Qt for Python)**: Utilizado para carregar o arquivo `.ui` e gerenciar a interface.
* **Qt Designer**: Ferramenta para o design visual da janela.

## 📦 Como Executar

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/tiagonunes1337/calculoSalario-Fgts.git](https://github.com/tiagonunes1337/calculoSalario-Fgts.git)
    cd calculoSalario-Fgts
    ```

2.  **Instale a biblioteca necessária:**
    ```bash
    pip install PySide6
    ```

3.  **Execute a aplicação:**
    ```bash
    python controle.py
    ```

## 📝 Estrutura de Arquivos

* `controle.py`: Arquivo principal contendo a lógica de cálculo e conexão com a interface.
* `interface.ui`: Arquivo de design gerado pelo Qt Designer.

---
Desenvolvido por **Tiago de Aquino Nunes** 🎓


# Monitoramento de Poluição Oceânica com Redes de Sensores Inteligentes
Este repositório contém uma solução para o problema de alocação ótima de sensores subaquáticos visando o monitoramento da poluição oceânica. Utilizaremos técnicas de programação dinâmica para otimizar a distribuição dos sensores em um ambiente bidimensional (como o oceano).

---
## Integrantes do projeto
| Nome | RM  | Turma |
|--|--|--|
|Gustavo Cristiano Pessoa de Souza | 551924  | 2ESPF|
|Filipe Bernard | 97830  | 2ESPF|
|Ricardo Vergani| 550166  | 2ESPF|
---
## Descrição do Problema
A poluição dos oceanos é um desafio global que afeta a biodiversidade, a economia e a saúde humana. Para monitorar e combater essa poluição, é essencial implantar redes de sensores subaquáticos. No entanto, a alocação desses sensores deve ser otimizada para maximizar a eficiência e minimizar os custos.

---
## Solução Proposta
- Distância entre Pontos:
    - Implementamos uma função para calcular a distância Euclidiana entre dois pontos no plano 2D. Essa distância será usada para avaliar o custo de alocação dos sensores.
- Programação Dinâmica:
    - Utilizamos a técnica de programação dinâmica para encontrar a distribuição ótima dos sensores. O objetivo é minimizar a soma das distâncias entre os sensores selecionados.
- Encontrando a Distribuição Ótima:
    - A função `encontrar_distribuicao_otima_sensores` recebe uma lista de coordenadas (x, y) dos pontos onde os sensores podem ser alocados e o número desejado de sensores.
    - Ela retorna os índices dos pontos selecionados para a alocação dos sensores.
---
## Como Usar
- Clone este repositório:

    ```
  git clone https://github.com/seu-usuario/monitoramento-poluicao-oceanica.git
    ```

- Execute o código Python:

    ```
  python monitoramento_poluicao.py
    ```

- Ajuste os pontos e o número de sensores conforme necessário no arquivo monitoramento_poluicao.py.
- --
## Referências
- Smith, J. (2020). Ocean Pollution: Causes, Effects, and Solutions. Link
- Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2009). Introduction to Algorithms. MIT Press.
- Kleinberg, J., & Tardos, É. (2006). Algorithm Design. Pearson.
- Bellman, R. (1957). Dynamic Programming. Princeton University Press.
---
### Licença
Este projeto está licenciado sob a Licença MIT. Consulte o arquivo LICENSE para obter mais detalhes.

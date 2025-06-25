
# Simulação de CSMA/CD - Grau B - Redes de Computadores

## 🎯 Objetivo do Trabalho

O objetivo deste projeto é desenvolver uma simulação do protocolo de controle de acesso ao meio **CSMA/CD (Carrier Sense Multiple Access with Collision Detection)**, conforme proposto na disciplina de **Redes de Computadores**.

A implementação simula o comportamento de múltiplos transmissores tentando acessar um canal de comunicação compartilhado, considerando os conceitos de:

- **Carrier Sense:** Verificar se o meio está livre antes de transmitir.
- **Multiple Access:** Múltiplos transmissores competindo pelo uso do canal.
- **Collision Detection:** Detecção de colisões durante a transmissão.
- **Backoff Exponencial Truncado:** Tempo de espera aleatório crescente após colisões.

## 🖥️ Tecnologias utilizadas

- Linguagem: **Python 3**
- Concorrência: **Múltiplas threads**
- Persistência de estado do canal: **Arquivo `canal.txt`**
- Registro de logs: **Arquivo `log_transmissao.txt`**
- Estatísticas e análises: **Arquivos `estatisticas.txt`, `.xlsx`, `.ipynb`**

## 📁 Estrutura de Arquivos

| Arquivo | Descrição |
|---|---|
| `csma_cd_simulation.py` | Código principal da simulação. Realiza o controle de concorrência, detecção de colisões, aplicação de backoff exponencial truncado e geração de logs e estatísticas. |
| `canal.txt` | Arquivo que simula o canal de comunicação. Indica se está LIVRE ou OCUPADO. |
| `log_transmissao.txt` | Registro detalhado de todos os eventos da simulação. Contém as interações entre transmissores e o canal. |
| `estatisticas.txt` | Contém os dados estatísticos finais de cada execução: tempo total, ociosidade, desempenho e colisões. |
| `Testes_realizados.xlsx` | Arquivo Excel que consolida os resultados de 60 testes realizados (10 repetições para cada número de transmissores — 4, 8 e 12 — com dois tempos de backoff: 0.5s e 0.05s). |
| `Analise_desempenho.ipynb` | Notebook com gráficos e análises comparativas entre os testes, destacando impacto do número de transmissores e valores de backoff sobre o desempenho e colisões. |
| `README.md` | Documento de descrição do projeto e instruções de execução. |

## 🚀 Como executar a simulação

1. Certifique-se de ter o **Python 3** instalado na sua máquina.

2. No terminal, navegue até a pasta do projeto:

```bash
cd REDES2-GRAUB
```

3. Execute o programa:

```bash
python csma_cd_simulation.py
```

> ⚠️ Os arquivos `canal.txt`, `log_transmissao.txt` e `estatisticas.txt` serão sobrescritos a cada nova execução.

## ✅ O que a simulação faz

- Cria múltiplos transmissores (threads), cada um tentando enviar um número fixo de pacotes (por padrão, 5).
- Antes de cada envio, o transmissor verifica se o canal está livre (`canal.txt`).
- Se o canal estiver ocupado, o transmissor aguarda um tempo de backoff e tenta novamente.
- Se duas transmissões ocorrerem simultaneamente, ocorre **colisão**, e os transmissores envolvidos realizam um **backoff exponencial truncado**.
- Transmissões bem-sucedidas e colisões são registradas nos arquivos de log e estatísticas.

## 📊 Estatísticas geradas

Ao final da execução, o arquivo `estatisticas.txt` trará informações como:

- Tempo total da simulação
- Tempo total de canal ocupado (transmissões bem-sucedidas)
- Tempo ocioso do canal
- Percentual de utilização do canal (desempenho)
- Total de colisões
- Colisões por transmissor
- Tentativas de envio por transmissor

As estatísticas de múltiplas execuções também foram organizadas no arquivo `Testes_realizados.xlsx` para posterior análise.

## 📈 Análise de desempenho

O notebook `Analise_desempenho.ipynb` compara os testes com diferentes números de transmissores (4, 8 e 12) e diferentes tempos de espera após encontrar o canal ocupado (0.5s e 0.05s). Nele são analisados:

- Desempenho médio do canal
- Total de colisões por cenário
- Tempo ocioso médio
- Impacto do número de transmissores na eficiência do canal

## 📌 Observações finais

- O código foi projetado para refletir de forma didática os conceitos do protocolo CSMA/CD, com controle de concorrência, colisões e mecanismo de backoff.
- A simulação é determinística no comportamento, mas contém elementos de aleatoriedade (tempo de transmissão, tempo de backoff) para simular um ambiente realista.
- As análises gráficas auxiliam na visualização do impacto da concorrência e das colisões sobre o desempenho da rede.

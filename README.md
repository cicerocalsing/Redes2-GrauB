
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
- Estatísticas finais: **Arquivo `estatisticas.txt`**

## 📁 Estrutura de Arquivos

| Arquivo | Descrição |
|---|---|
| `csma_cd_simulation.py` | Código principal da simulação |
| `canal.txt` | Representação do estado atual do canal (livre ou ocupado) |
| `log_transmissao.txt` | Registro detalhado de todos os eventos da simulação |
| `estatisticas.txt` | Estatísticas finais, como tempo de simulação, uso do canal, colisões por transmissor, etc |
| `README.md` | Este arquivo de documentação |

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

## ✅ O que a simulação faz

- **Cria 4 transmissores (threads), cada um enviando 5 pacotes.**
- Antes de cada transmissão, cada transmissor verifica se o canal está livre.
- Se o canal estiver ocupado, a thread aguarda um pequeno intervalo antes de tentar novamente.
- Se duas threads iniciarem transmissão ao mesmo tempo, o sistema detecta colisão e aplica um **backoff exponencial truncado** antes da próxima tentativa.
- O tempo de cada transmissão é aleatório, simulando diferentes tamanhos de pacotes.
- Ao final, a simulação gera **logs completos** e **estatísticas detalhadas**.

## 📊 Estatísticas geradas

Ao final da execução, o arquivo `estatisticas.txt` trará informações como:

- Tempo total da simulação
- Tempo total de canal ocupado
- Tempo ocioso do canal
- Percentual de utilização do canal (desempenho)
- Total de colisões
- Colisões por transmissor
- Tentativas de envio por transmissor

## 📌 Observações finais
- Durante a execução, os arquivos de canal, log e estatísticas são sobrescritos para garantir os resultados da nova simulação.

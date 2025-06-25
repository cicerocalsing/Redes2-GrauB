import os
import time
import random
import threading
from collections import defaultdict

CAMINHO_CANAL = "canal.txt"
LOG_FILE = "log_transmissao.txt"
STATS_FILE = "estatisticas.txt"

NUM_THREADS = 20
PACOTES_POR_THREAD = 5
TEMPO_TRANSMISSAO_MIN = 0.5
TEMPO_TRANSMISSAO_MAX = 1.5

colisoes_totais = 0
tempo_ocupado_total = 0
tentativas_por_thread = {}
colisoes_por_thread = defaultdict(int)

lock = threading.Lock()

start_time = 0
end_time = 0

def log(mensagem):
    print(mensagem)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(mensagem + "\n")

def ler_canal():
    if not os.path.exists(CAMINHO_CANAL):
        return "LIVRE"
    with open(CAMINHO_CANAL, "r") as f:
        return f.read().strip()

def escrever_canal(status):
    with open(CAMINHO_CANAL, "w") as f:
        f.write(status)

def backoff(tentativa, id_thread):
    k = min(tentativa, 10)
    tempo_espera = random.uniform(0, (2 ** k) * 0.1)
    log(f"[{id_thread}] ⏳ Backoff por {tempo_espera:.2f} segundos (tentativa {tentativa})")
    time.sleep(tempo_espera)

def transmitir(id_thread):
    global colisoes_totais, tempo_ocupado_total

    tentativas_por_thread[id_thread] = 0

    for pacote in range(1, PACOTES_POR_THREAD + 1):
        sucesso = False
        tentativa = 0

        while not sucesso:
            tentativa += 1
            tentativas_por_thread[id_thread] += 1
            estado_canal = ler_canal()

            if estado_canal == "LIVRE":
                escrever_canal(f"OCUPADO-{id_thread}-PACOTE-{pacote}")
                log(f"[{id_thread}] 📦 Tentando transmitir pacote {pacote}...")

                tempo_transmissao = random.uniform(TEMPO_TRANSMISSAO_MIN, TEMPO_TRANSMISSAO_MAX)
                log(f"[{id_thread}] 📶 Transmitindo... Tempo estimado: {tempo_transmissao:.2f} segundos")
                time.sleep(tempo_transmissao)

                estado_canal_final = ler_canal()
                if estado_canal_final == f"OCUPADO-{id_thread}-PACOTE-{pacote}":
                    log(f"[{id_thread}] ✅ Transmissão concluída com sucesso.")
                    escrever_canal("LIVRE")
                    with lock:
                        tempo_ocupado_total += tempo_transmissao
                    sucesso = True
                else:
                    log(f"[{id_thread}] 🚨 Colisão detectada!")
                    with lock:
                        colisoes_totais += 1
                        colisoes_por_thread[id_thread] += 1
                    escrever_canal("LIVRE")
                    backoff(tentativa, id_thread)
            else:
                log(f"[{id_thread}] ❌ Canal ocupado, aguardando...")
                time.sleep(0.5)

        tempo_espera_entre_pacotes = random.uniform(0.3, 0.8)
        time.sleep(tempo_espera_entre_pacotes)

def salvar_estatisticas():
    tempo_total_simulacao = end_time - start_time
    tempo_ocioso = tempo_total_simulacao - tempo_ocupado_total
    desempenho_percentual = (tempo_ocupado_total / tempo_total_simulacao) * 100 if tempo_total_simulacao > 0 else 0

    with open(STATS_FILE, "w", encoding="utf-8") as f:
        f.write(f"Tempo total da simulação: {tempo_total_simulacao:.2f} segundos\n")
        f.write(f"Tempo total de transmissão (canal ocupado): {tempo_ocupado_total:.2f} segundos\n")
        f.write(f"Tempo ocioso (canal livre): {tempo_ocioso:.2f} segundos\n")
        f.write(f"Desempenho de transmissão (uso do canal): {desempenho_percentual:.2f}%\n\n")

        f.write(f"Total de colisões: {colisoes_totais}\n")
        f.write("Colisões por transmissor:\n")
        for thread_id, qtd_colisoes in colisoes_por_thread.items():
            f.write(f" - {thread_id}: {qtd_colisoes} colisões\n")

        f.write("\nTentativas por transmissor:\n")
        for thread_id, tentativas in tentativas_por_thread.items():
            f.write(f" - {thread_id}: {tentativas} tentativas\n")

def main():
    global start_time, end_time

    if os.path.exists(LOG_FILE):
        os.remove(LOG_FILE)
    if os.path.exists(STATS_FILE):
        os.remove(STATS_FILE)
    if os.path.exists(CAMINHO_CANAL):
        os.remove(CAMINHO_CANAL)

    start_time = time.time()

    threads = []
    for i in range(1, NUM_THREADS + 1):
        t = threading.Thread(target=transmitir, args=(f"T{i}",))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    end_time = time.time()
    salvar_estatisticas()
    log("✅ Transmissão finalizada! Estatísticas salvas.")

if __name__ == "__main__":
    main()

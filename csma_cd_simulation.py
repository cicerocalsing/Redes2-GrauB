import threading
import time
import random
from datetime import datetime

def log(transmissor_id, mensagem):
    tempo = datetime.now().strftime('%H:%M:%S')
    print(f"[{tempo}] [{transmissor_id}] {mensagem}")

class Canal:
    def __init__(self):
        self.lock = threading.Lock()
        self.ocupado = False

    def verificar_meio(self):
        """📡 Verifica se o canal está livre (False) ou ocupado (True)."""
        return self.ocupado
    
    def ocupar_meio(self, transmissor_id):
        with self.lock:
            self.ocupado = True
            log(transmissor_id, "🔴 Canal agora está OCUPADO.")

    def liberar_meio(self, transmissor_id):
        with self.lock:
            self.ocupado = False
            log(transmissor_id, "🟢 Canal agora está LIVRE.")


class Transmissor(threading.Thread):
    def __init__(self, transmissor_id, canal):
        super().__init__()
        self.transmissor_id = transmissor_id
        self.canal = canal
        self.max_tentativas = 10  # Limite para o backoff exponencial
        self.tentativas = 0

    def run(self):
        while True:
            log(self.transmissor_id, "🔍 Verificando o meio...")
            if not self.canal.verificar_meio():
                log(self.transmissor_id, "🚀 Meio livre! Iniciando transmissão...")
                self.canal.ocupar_meio(self.transmissor_id)

                tempo_transmissao = random.uniform(0.5, 1.5)
                log(self.transmissor_id, f"📶 Transmitindo... Tempo estimado: {tempo_transmissao:.2f} segundos")
                time.sleep(tempo_transmissao)

                if random.random() < 0.3:
                    log(self.transmissor_id, "🚨 Colisão detectada!")
                    self.handle_colisao()
                else:
                    log(self.transmissor_id, "✅ Transmissão concluída com sucesso.")
                    self.canal.liberar_meio(self.transmissor_id)
                    break
            else:
                log(self.transmissor_id, "❌ Meio ocupado, aguardando...")
                time.sleep(random.uniform(0.1, 0.3))


    def handle_colisao(self):
        self.canal.liberar_meio(self.transmissor_id)
        self.tentativas += 1

        if self.tentativas > self.max_tentativas:
            log(self.transmissor_id, "🚫 Número máximo de tentativas atingido. Abortando transmissão.")
            return

        k = min(self.tentativas, 10)
        backoff_time = random.uniform(0, (2 ** k) * 0.1)
        log(self.transmissor_id, f"⏳ Backoff por {backoff_time:.2f} segundos (tentativa {self.tentativas})")
        time.sleep(backoff_time)


def main():
    canal = Canal()

    # Criando quatro transmissores
    transmissores = []
    for i in range(1, 5):
        t = Transmissor(f"T{i}", canal)
        transmissores.append(t)

    # Iniciando todas as threads
    for t in transmissores:
        t.start()

    # Esperando todas as threads terminarem
    for t in transmissores:
        t.join()

    print("\n✅ Simulação finalizada com 4 transmissores!")

if __name__ == "__main__":
    main()


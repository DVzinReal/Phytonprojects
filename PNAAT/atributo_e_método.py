class SensorVibracao:
    def __init__(self, id_sensor):
        self.id_sensor = id_sensor
        self.vibracao_atual = 2.3  # em mm/s RMS
        self.limite_maximo = 4.5  # em mm/s RMS

# Criamos uma instância do sensor
sensor_vibracao = SensorVibracao("SENSOR-MOTOR-01")

# 1. ACESSANDO um atributo para verificar a vibração atual
print(f"Vibração atual: {sensor_vibracao.vibracao_atual} mm/s")

# 2. MODIFICANDO um atributo para definir um novo limite
print("Ajustando limite máximo de vibração...")
sensor_vibracao.limite_maximo = 5.0

# 3. VERIFICANDO a mudança
print(f"Novo limite máximo: {sensor_vibracao.limite_maximo} mm/s")

class Esteira:
    def __init__(self, id_esteira):
        self.id = id_esteira
        self.status = "parada" # Status inicial

    def ligar(self):
        self.status = "movendo"
        print(f"Esteira {self.id}: movendo.")

    def parar(self):
        self.status = "parada"
        print(f"Esteira {self.id}: parada para acesso do robô.")

class Robo:
    def __init__(self, id_robo):
        self.id = id_robo
        self.status = "em espera"

    def pegar_peca(self, esteira_alvo):
        print(f"Robô {self.id}: iniciando operação de coleta.")
        self.status = "trabalhando"

        # INTERAÇÃO: O robô ACESSA o atributo da esteira
        if esteira_alvo.status == "movendo":
            print(f"Robô {self.id}: a esteira está movendo. Solicitando parada...")
            # INTERAÇÃO: O robô CHAMA o método da esteira
            esteira_alvo.parar()

        print(f"Robô {self.id}: pegando a peça da esteira {esteira_alvo.id}.")
        # Lógica para pegar a peça aqui...
        print(f"Robô {self.id}: peça coletada com sucesso.")
        self.status = "em espera"

        esteira_producao = Esteira("EST-01")
        robo_braco = Robo("RB-01")

        # 1. Ligamos a esteira
        esteira_producao.ligar()

        # 2. O robô tenta pegar a peça, interagindo com a esteira
        robo_braco.pegar_peca(esteira_producao)

        # 3. Verificamos o estado final da esteira
        print(f"Estado final da esteira {esteira_producao.id}: {esteira_producao.status}")
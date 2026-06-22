Trabalho Avaliativo – G2
Disciplina: Pensamento Computacional
Professor: Leonam Vieira Hemann
Turma: SIS1
Estudante: Guilherme William Carpowiski de Lima (Trabalho realizado individualmente) Data de início: 02/06/2026
Data de entrega: 25/06/2026
Valor: G2

# Estação de Cabeceira Inteligente com ESP32, OLED e Abajur Sensitivo

Trabalho prático avaliativo desenvolvido para a nota de G2 da disciplina de **Pensamento Computacional**. O projeto consiste em um sistema embarcado utilizando o microcontrolador ESP32 para gerenciar um relógio sincronizado via Internet (NTP) exibido em uma tela OLED e integrado ao acionamento tátil (capacitivo) de uma lâmpada de abajur doméstica.

## 📌 Informações do Projeto
* **Disciplina:** Pensamento Computacional
* **Professor:** Leonam Vieira Hemann
* **Turma:** SIS1
* **Estudante:** Guilherme William Carpowiski de Lima *(Projeto executado individualmente)*
* **Data de Entrega:** 25/06/2026
* **Instituição:** Faculdade AMF

---

## 🛠️ Organização do Trabalho e Responsabilidades

Como o projeto foi executado de forma individual, todas as atribuições de gerenciamento de hardware, desenvolvimento de software e modelagem lógica foram concentradas no integrante:

| Integrante | Responsabilidade no Trabalho |
| :--- | :--- |
| **Guilherme William C. de Lima** | Idealização da proposta, montagem e correção física do circuito de hardware, programação em C/C++ na Arduino IDE, aplicação dos pilares do Pensamento Computacional, testes de bancada e redação do relatório técnico. |

---

## 💡 1ª e 2ª Etapa: Criação da Ideia e Definição do Problema

### Ideia Principal
O desenvolvimento de uma **Estação de Cabeceira Inteligente e Multiuso**. O dispositivo utiliza a conectividade Wi-Fi do microcontrolador ESP32 para buscar o horário oficial brasileiro em servidores NTP na internet, eliminando atrasos. Paralelamente, utiliza pinos de leitura capacitiva integrados ao chip para alternar o estado de acendimento de uma lâmpada através do toque do usuário na estrutura condutiva do abajur.

### Justificativa e Contexto
A proposta surgiu através da análise de problemas cotidianos de ergonomia e utilidade dentro do quarto:
1. **Desconfiguração de Horários:** Relógios digitais comuns atrasam com o tempo ou desconfiguram completamente ao sofrerem quedas bruscas de energia elétrica na rede residencial.
2. **Ergonomia Noturna:** Encontrar interruptores mecânicos pequenos, chaves de corda ou botões em fios de abajures no escuro total costuma ser difícil e inconveniente para usuários comuns, idosos ou pessoas com mobilidade reduzida.

Ao aplicar o ESP32, unificamos a resolução de ambos os problemas em um único eletrodoméstico inteligente de baixo custo de fabricação.

---

## 📋 3ª Etapa: Planejamento da Solução

O sistema foi planejado para executar as seguintes ações automatizadas:
* **Entradas de Dados (Inputs):** Sinais do protocolo UDP vindos do servidor de tempo `pool.ntp.org`; leitura de capacitância eletrostática humana através da API `touchRead()` no pino touch do ESP32.
* **Processamento (Logic):** Filtragem de dados temporais para o fuso horário de Brasília (GMT -3); cálculo de *Debounce* por software para evitar múltiplos acionamentos em um único toque no abajur.
* **Saídas (Outputs):** Atualização de strings em texto grande (`HH:MM:SS`) a cada 1 segundo em uma tela OLED de tecnologia I2C (SSD1306); alteração de estado lógico (HIGH/LOW) na GPIO de controle da lâmpada.

---

## 🧩 Aplicação dos Pilares do Pensamento Computacional

### 1. Decomposição
Para simplificar a engenharia do projeto, o problema complexo foi dividido em 5 pequenos blocos de desenvolvimento independente:
* **Módulo de Rede:** Inicialização do rádio Wi-Fi interno do chip e autenticação na rede local.
* **Módulo Cronometrado:** Conexão com o protocolo NTP e tradução do timestamp para horas, minutos e segundos.
* **Módulo Visual:** Inicialização lógica do display SSD1306 através do barramento I2C e renderização gráfica dos caracteres.
* **Módulo Sensitivo:** Varredura elétrica contínua e calibração de limite (*threshold*) de toque no abajur.
* **Módulo de Potência:** Chaveamento eletrônico seguro para acionar a alimentação da lâmpada.

### 2. Reconhecimento de Padrões
* **Ciclos Periódicos:** Identificou-se que a tarefa de leitura do relógio interno e atualização da tela é um padrão cíclico imutável que deve ocorrer rigorosamente em intervalos fixos de 1000 milissegundos.
* **Padronização de Strings:** A lógica matemática de formatação de dois dígitos (`%02d`) usada para exibir o número da hora (ex: transformar `5` em `05`) se repete de forma idêntica para os minutos e segundos.
* **Precedência de Inicialização:** A rotina de Boot segue uma sequência linear fixa na eletrônica: Alimentação ➔ Periféricos de Hardware ➔ Handshake do Wi-Fi ➔ Sincronização de Data/Hora.

### 3. Abstração
No desenvolvimento deste protótipo, detalhes secundários foram completamente ignorados para manter o foco na funcionalidade principal:
* **O que ficou de fora:** Criação de alarmes/despertador, animações fluidas de transição de tela, interface de configuração de rede pelo celular (Access Point) e controle de dimerização da intensidade da lâmpada.
* **O que foi mantido como indispensável:** Sincronização estável de tempo mundial e sensibilidade instantânea do toque no abajur.

---

## 💻 4ª Etapa: Algoritmo da Solução

Abaixo encontra-se a representação em formato de pseudocódigo da lógica final gravada no microcontrolador:

```text
Algoritmo EstacaoCabeceiraInteligente
    Definir rede_wifi = "AMF"
    Definir senha_wifi = "amf@2025"
    Definir fuso_horario = -10800 segundos (GMT -3)
    Definir limite_touch = 20
    
    Procedimento setup()
        Iniciar Comunicação Serial em 115200 bps
        Iniciar Barramento I2C para Display OLED (Endereço lógico 0x3C)
        Se (Falha ao iniciar display) Então
            Imprimir erro na Serial e travar execução
        Fim Se
        
        Exibir no OLED: "Conectando ao WiFi..."
        Conectar no Wi-Fi(rede_wifi, senha_wifi)
        Enquanto (Status do Wi-Fi for diferente de CONECTADO) Faça
            Aguardar 500 milissegundos
        Fim Enquanto
        
        Configurar Relógio Interno via configTime(fuso_horario, NTP_Server)
    Fim Procedimento

    Procedimento loop()
        Se (Buscar_Tempo_Local_Sucesso()) Então
            Limpar buffer do display OLED
            Formatar texto no padrão "HH:MM:SS"
            Desenhar texto centralizado com tamanho 2
            Atualizar tela fisicamente
        Senão
            Exibir no OLED: "Erro ao obter hora"
        Fim Se
        
        Se (Leitura_Pino_Capacitivo() < limite_touch) Então
            Inverter_Estado_Fisico(Pino_Lampada_Abajur)
            Aguardar 300 milissegundos (Proteção contra repetição/Debounce)
        Fim Se
        
        Aguardar 1000 milissegundos
    Fim Procedimento
Fim Algoritmo

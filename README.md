# Oficina de Computação Física
### Prof. Peter Jandl Jr.

<img src='https://github.com/pjandl/ocf/blob/main/repo-cover-ocf.png?raw=true' alt='![Oficina Computação Física]' />

Esta é uma oficina experimental de *computação física*:

> Computação Física, ou Physical Computing, é o uso de computação e de eletrônica (sensores e atuadores) na prototipação de objetos físicos para interação com seres humanos cujo objetivo é interligar os mundos físico e virtual, assim demonstrar como usar a computação e a interação com a tecnologia para o desenvolvimento de suas atividades rotineiras [DREAMFELL, 2011](https://dreamfeel.wordpress.com/2009/03/07/computacao-fisica/).

Desta maneira, o objetivo principal desta oficina é apresentar conceitos básicos de programação e eletrônica, na forma de roteiros de experiências que permitam a montagem de protótipos simples, capazes de capturar dados do mundo real, produzir ações no mundo real, além de compartilhar informações com pessoas e dispositivos. Para tanto serão utilizadas elementos de eletrônica e de computação.

A parte da eletrônica requer o uso de alguma placa de desenvolvimento de baixo custo, tais como as populares:

- Arduino (uno, mega, nano)
- NodeMCU (esp8266, esp32)
- Raspberry Pi (Pico, Pico W)
- Banana Py PicoW
- STM 32 (blue pill, black pill)

Também serão utilizados componentes eletrônicos diversos, tais como resistores, termistores, foto-resistores, leds, relês, servo-motores, motores DC, módulos sensores, displays e outros. Para aqueles que desejam dispor destes elementos para realizar livremente as montagens apresentadas ou outras, sugere-se os itens da [lista de componentes](https://github.com/pjandl/ocf/tree/main/lista-componentes.md).

A parte da computação usa duas das mais conhecidas e flexíveis linguagens de programação: [**C++**](https://www.arduino.cc/reference/en/) e [**Python**](https://docs.micropython.org/en/latest/). Além destas linguagens é conveniente a utilização de ambientes de desenvolvimento integrados (*Integrated Development Enviroments* - IDEs) como [Thonny](https://github.com/thonny/thonny/releases/) e [Arduino IDE](https://www.arduino.cc/en/software), que facilitam muito o processo de desenvolvimento e de testes.

Daremos preferência ao uso do Python, pois sua simplicidade leva a um aprendizado mais rápido, o que é sempre interessante. Na verdade, utilizaremos o **MicroPython**, uma versão mais leve do Python, criada com o intuito de incentivar o uso de placas de desenvolvimento dotadas de capacidades mais sofisticadas, mas de ótimo custo/benefício, como os NodeMCU ESP8266 e ESP32, as Raspberry Pi Pico e Pico W, e a Banana Py PicoW.

Isto permitirá a montagem de muitos protótipos, explorando princípios da eletrônica, da programação de computadores e da comunicação em rede, possibilitando que seja, criados sistemas de captura de dados, de automação residencial/predial/comercial/industrial, aplicações de Internet das Coisas (IoT), além de jogos, brinquedos e mais.

Vamos trabalhar!

## Organização dos Materiais

Os materiais desta oficina estão distribuídos em diretórios diferentes para facilitar seu acesso e consulta. Segue uma lista, com os itens mais importantes no seu início.

- [T-2024-1](https://github.com/pjandl/ocf/tree/main/T-2024-1) :: materiais da temporada *2024-1* (atual) da oficina, onde se localizam os roteiros dos experimentos/montagens e os programas Python correspondentes.
- [Bibliotecas](https://github.com/pjandl/ocf/tree/main/Bibliotecas) :: bibliotecas/módulos utilizados nos roteiros da oficina.
- [NodeMCU](https://github.com/pjandl/ocf/tree/main/NodeMCU) :: contém informações específicas sobre as placas de desenvolvimento NodeMCU baseadas no ESP8266 e ESP32.
- [Componentes](https://github.com/pjandl/ocf/tree/main/Componentes) :: contém informações sobre componentes diversos, como resistores, leds, etc.
- [T-2023-2](https://github.com/pjandl/ocf/tree/main/T-2023-2) :: materiais da temporada *2023-2* da oficina, que incluem os roteiros dos experimentos/montagens e os programas correspondentes.
- [T-2023-1](https://github.com/pjandl/ocf/tree/main/T-2023-1) :: materiais da temporada *2023-1* da oficina, onde se localizam os roteiros dos experimentos/montagens e os exemplos Python correspondentes.
- [T-2022-2](https://github.com/pjandl/ocf/tree/main/T-2022-2) :: materiais da temporada 2022-2 da oficina, ou seja, os roteiros dos experimentos/montagens e os exemplos de programação correspondentes.
- [Apresentações](https://github.com/pjandl/ocf/tree/main/Apresentacoes) :: apresentações da Oficina de Computação Física, contendo uma breve introdução ao tema e visão geral das atividades da oficina.

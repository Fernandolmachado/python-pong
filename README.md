# python-pong
Clássico jogo Pong desenvolvido em Python utilizando a biblioteca Pygame.

Mecânicas

  - O "campo de jogo" está disposto na horizontal, onde os paddles ficam nas laterais da tela;
  - Os paddles podem mover-se apenas verticalmente, dentro dos limites do "campo de jogo";
  - A bola inicia parada no centro do campo. Após um intervalo de tempo parametrizado, aleatoriamente, movimenta-se em um sentido nos intervalos angulares [315°, 45°] e [135°, 225°];
  - A bola possui velocidade constante durante toda partida;
  - A bola colide com as paredes do campo e altera seu sentido verticalmente sem perda de velocidade;
  - Os paddles são movimentados pelos jogadores;
  - Os paddles são utilizados para rebater a bola na direção de seu adversário, não permitindo que a bola atinja a extremidade horizontal do campo de jogo;
  - A bola possui aderência com relação aos paddles;
  - Caso a bola atinja uma extremidade horizontal, 1 ponto será concedido ao jogador da extremidade oposta e a bola será reiniciada no centro e escolhido aleatoriamente uma direção;
  - A partida ocorre em um intervalo de tempo configurado pelo jogador, tendo seus limites em 30s a 300s, e podendo variar de 30s em 30s;
  - Ao fim do tempo de partida, o jogador com maior pontuação vence, porém há a possibilidade de empate;
  - As opções do jogador são salvas em formato json.

Controles

  Mouse: Navegação pelos menus.
  W: Move paddle 1 para cima.
  S: Move paddle 1 para baixo.
  UP: Move paddle 2 para cima.
  DOWN: Move paddle 2 para baixo.
  ESC: Pause

UI

  Tela de Menu Principal
    Botão Jogar (Inicia partida)
    Botão Opções (Apresenta tela de opções)
    Botão Sair (Fecha o jogo)

  Tela de Opções
    Volume de música (Com botões em forma de seta para aumentar ou diminuir volume da música)
    Volume de sfx (Com botões em forma de seta para aumentar ou diminuir volume do sfx)
    Tempo de partida (Com botões em forma de seta para aumentar ou diminuir o tempo de jogo)
    Botão Menu (Volta ao menu principal)

  Quadro de informações
    Temporizador da partida
    Placar (Apresenta pontuação dos players)

  Tela de Pause
    *Sobrepõe a tela da partida estática
    Botão Jogar (Volta a partida)
    Botão Reiniciar (Reinicia partida, pontuação e temporizador)
    Botão Menu (Volta ao menu principal)
    
  Tela de Fim de Partida
    Texto indicando vencedor ou empate
    Botão Jogar Novamente (Inicia uma nova partida)
    Botão Menu (Volta ao menu principal)
    
Assets

  Sons
    Musica de jogo
    Efeito hover
    Efeito click
    Efeito colisão com parede
    Efeito colisão com paddles
    Efeito gol
    
Publicação
  Código e assets ficaram disponíveis no GitHub.

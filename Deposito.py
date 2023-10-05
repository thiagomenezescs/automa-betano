import time
import pyautogui

numero_vezes = 0

numero_chegar = 9

while numero_vezes < numero_chegar:
    time.sleep(5)
    #Mover para barra de pesquisa
    pyautogui.moveTo(401,73)
    pyautogui.click()
    # Escrever o link da area de saque
    time.sleep(1)
    pyautogui.write('https://br.betano.com/myaccount/withdraw/pix')
    pyautogui.press("enter")
    time.sleep(5)
    # Defina as coordenadas iniciais (x, y) onde você deseja clicar
    x_inicial, y_inicial = 515,501

    # Defina as coordenadas finais (x, y) para onde você deseja arrastar (para baixo)

    x_final, y_final = 602,502  # Arrastando para baixo, aumentando o valor y

    # Duração do movimento em segundos (ajuste conforme necessário)
    duração_movimento = 1.0

    # Clique e segure o botão do mouse na posição inicial
    pyautogui.mouseDown(x=x_inicial, y=y_inicial)

    # Movimente o cursor para a posição final ao longo do tempo especificado
    pyautogui.moveTo(x_final, y_final, duration=duração_movimento)

    # Solte o botão do mouse na posição final
    pyautogui.mouseUp(x=x_final, y=y_final)
    time.sleep(2)
    # Aposa rolar até em baixo ele irar mover ate a opção de escrever quanto sacar
    pyautogui.moveTo(779,683)
    pyautogui.click()
    time.sleep(1)
    # Clicar na caixa para digitar o valor
    pyautogui.moveTo(554,598)
    pyautogui.write('50')
    time.sleep(1)
    # Agora ele ira mover para o botão de saque e clicar
    pyautogui.moveTo(556,640)
    pyautogui.click()
    # Agora ele ira voltar na area de pix para copiar e colar o cpf no outro site 
    pyautogui.moveTo(164,69)
    pyautogui.click()
    # Escrever o link da area de saque
    time.sleep(1)
    pyautogui.write('https://br.betano.com/myaccount/withdraw/pix')
    pyautogui.press("enter")
    time.sleep(5)
    # Agora copiar e colar o cpf 
    # Vá para o início do texto que você deseja selecionar (ajuste as coordenadas)
    pyautogui.click(x=500, y=500)

    # Pressione a tecla Shift e mantenha pressionada (isso simula a seleção)
    pyautogui.keyDown('shift')

    # Mova o cursor para o final do texto que você deseja selecionar (ajuste as coordenadas)
    pyautogui.move(100, 0)  # Mova 100 pixels para a direita (ajuste conforme necessário)

    # Libere a tecla Shift (isso completa a seleção)
    pyautogui.keyUp('shift')

    # Pressione Ctrl + C para copiar o texto selecionado
    pyautogui.hotkey('ctrl', 'c')

    # Aguarde um curto período de tempo para garantir que a cópia seja feita
    time.sleep(1)

    # Apos ela copiar ela ira para o site da Tech play pra colar la
    pyautogui.moveTo(1000, 1000) # posição do x e y do site tech play
    time.sleep(1)
    pyautogui.moveTo(1300, 1200) # posição x e y do botão de pra abrir a opção de listar
    pyautogui.click()
    time.sleep(1)
    pyautogui.moveTo(1500, 1000) # posição x e y do botão listar
    pyautogui.click()
    time.sleep(1)
    # Mova o cursor para a posição onde você deseja colar o cpf (ajuste as coordenadas)
    pyautogui.click(x=600, y=600)

    # Pressione Ctrl + V para colar o texto copiado
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)
    pyautogui.moveTo(1500, 400) # posição do botão filtar
    pyautogui.click()
    time.sleep(5)
    pyautogui.moveTo(1000, 200) # posição do botão atualizar saldo
    pyautogui.click()
    time.sleep(3)
    pyautogui.moveTo(1000, 300) # posição do botão inativar a conta
    pyautogui.click()
    time.sleep(4)
    pyautogui.moveTo(800, 50) # posição do botão confirmar
    pyautogui.click()
    time.sleep(15)
    # Agora é preciso que você coloque abaixo a posição x e y da tela da betano em que estavamos
    pyautogui.moveTo(1000, 100) # posição so para para o mouse voltar para o outro monitor e ficar sobre a tela da bentano 
    time.sleep(3)
    # Bom agora ele ira minimizar esta tela da betano pois ja concluimos nela e ira passar para a proxima e repetir isso tudo dnv
    pyautogui.moveTo(1158, 30)
    pyautogui.click()
    
    numero_vezes += 1

import tkinter as tk
from tkinter import messagebox
import subprocess
import time
import pyautogui

# Defina as cores e fontes
bg_color = "#000000"  # Cor de fundo
button_color = "#3498db"  # Cor dos botões
button_text_color = "#ffffff"  # Cor do texto dos botões
font = ("Arial", 14)  # Fonte

users = {"123": "123"}

def verif_login():
    user = user_entry.get()
    password = password_entry.get()

    if user in users and users[user] == password:
        open_main_window()
    else:
        messagebox.showerror("Erro no login", "Usuario ou senha incorretos")
    
def open_main_window():
    login_window.destroy()

    main_window = tk.Tk()
    main_window.geometry("500x480")
    main_window.title("Gerenciador de Scripts")
    main_window.configure(bg=bg_color)  # Define a cor de fundo

def exe_script1():
        # Implemente o script aqui

# Especifique o caminho completo para o executável do Dolphin
caminho_executavel_dolphin = r'C:\\Users\\TH\\AppData\\Local\\Programs\\Dolphin Anty\\Dolphin Anty.exe'

# Número de vezes que você deseja executar o código
num_execucoes = 9

# Variável de contagem
execucoes_realizadas = 0

caixa_name = 1

sleep_incial = 13

subprocess.Popen(caminho_executavel_dolphin, shell=True)

while execucoes_realizadas < num_execucoes:
        # Aguarde alguns segundos para que o Dolphin seja carregado completamente
    time.sleep(sleep_incial)

        # Coordenadas do botão "Create Profile"
    x_create_profile = 917  # Substitua pelo valor correto
    y_create_profile = 39  # Substitua pelo valor correto

        # Mova o cursor do mouse para as coordenadas do botão "Create Profile" e clique
    pyautogui.moveTo(x_create_profile, y_create_profile)
    pyautogui.click()

        # Aguarde um segundo para a próxima etapa
    time.sleep(1)

        # Escreva o número "1" na caixa "Input Name"
    pyautogui.write(str(caixa_name))

        # Coordenadas do botão "NEW FINGERPRINT"
    x_new_fingerprint = 994  # Substitua pelo valor correto
    y_new_fingerprint = 72  # Substitua pelo valor correto

        # Mova o cursor do mouse para as coordenadas do botão "NEW FINGERPRINT" e clique duas vezes
    pyautogui.moveTo(x_new_fingerprint, y_new_fingerprint)
    pyautogui.click()
    time.sleep(0.3)

        # Aguarde um segundo para a próxima etapa
    time.sleep(0.3)

        # Coordenadas do botão "USER DATA"
    x_user_data = 1084  # Substitua pelo valor correto
    y_user_data = 122  # Substitua pelo valor correto

        # Mova o cursor do mouse para as coordenadas do botão "USER DATA" e clique
    pyautogui.moveTo(x_user_data, y_user_data)
    pyautogui.click()

        # Aguarde um segundo para a próxima etapa
    time.sleep(0.4)

        # Coordenadas do botão "Do not track"
    x_do_not_track = 371  # Substitua pelo valor correto
    y_do_not_track = 412  # Substitua pelo valor correto

        # Mova o cursor do mouse para as coordenadas do botão "Do not track" e clique
    pyautogui.moveTo(x_do_not_track, y_do_not_track)
    pyautogui.click()

        # Aguarde um segundo para a próxima etapa
    time.sleep(0.3)

        # Coordenadas do botão "Create"
    x_create = 1149  # Substitua pelo valor correto
    y_create = 74  # Substitua pelo valor correto

        # Mova o cursor do mouse para as coordenadas do botão "Create" e clique
    pyautogui.moveTo(x_create, y_create)
    pyautogui.click()

        # Incrementa a variável de contagem
    execucoes_realizadas += 1
    caixa_name += 1
    sleep_incial = 0.5
    
    if execucoes_realizadas == 9:
        time.sleep(1)
        # Iniciar os 9 navegadores em ordem
        pyautogui.moveTo(521,126) # Botão de inciar do primeiro 
        pyautogui.click()
        time.sleep(0.1)
        pyautogui.moveTo(520,172) # Botão de inciar do Segundo
        pyautogui.click()
        time.sleep(0.1)
        pyautogui.moveTo(521,222) # Botão de inciar do Terceiro 
        pyautogui.click()
        time.sleep(0.1)
        pyautogui.moveTo(521,270) # Botão de inciar do Quarto 
        pyautogui.click()
        time.sleep(0.1)
        pyautogui.moveTo(520,318) # Botão de inciar do Quinto 
        pyautogui.click()
        time.sleep(0.1)
        pyautogui.moveTo(520,366) # Botão de inciar do Sexto 
        pyautogui.click()
        time.sleep(0.1)
        pyautogui.moveTo(520,414) # Botão de inciar do Setimo 
        pyautogui.click()
        time.sleep(0.1)
        pyautogui.moveTo(519,461) # Botão de inciar do Oitavo 
        pyautogui.click()
        time.sleep(0.1)
        pyautogui.moveTo(517,510) # Botão de inciar do Nono 
        pyautogui.click()
        time.sleep(13)
        contagem = 1
        numero_final = 9
        while contagem < numero_final:
            # Onde sera posto os usuarios por ordem
            usuarios = 'Usuario'
            senhas = 'senha'
            if contagem == 2:
                usuarios = 'Usuario'
                senhas = 'senha'
            elif contagem == 3:
                usuarios = 'Terceiro usuario'
                senhas = 'Terceira senha'
            elif contagem == 4:
                usuarios = 'Quarto usuario'
                senhas = 'Quarta senha'
            elif contagem == 5:
                usuarios = 'Quinto usuario'
                senhas = 'Quinta senha'
            elif contagem == 6:
                usuarios = 'Sexto usuario'
                senhas = 'Sexta senha'
            elif contagem == 7:
                usuarios = 'Setimo usuario'
                senhas = 'Setima senha'
            elif contagem == 8:
                usuarios = 'Oitavo usuario'
                senhas = 'Oitavo senha'
            elif contagem == 9:
                usuarios = 'Nono usuario'
                senhas = 'Nona senha'
            # Iniciar o login na betano e abrir ela
            pyautogui.write("https://br.betano.com")
            pyautogui.press("enter")
            time.sleep(5)
            # Clicar no botão para fechar os cookies
            pyautogui.moveTo(955,689)
            pyautogui.click()
            time.sleep(1)
            # Mover para o botão inicar sessão na betano
            pyautogui.moveTo(744,555) 
            pyautogui.click()
            time.sleep(1)
            pyautogui.click()
            time.sleep(2)
            # Clicar no não sou um robô
            pyautogui.moveTo(390,359)
            pyautogui.click()
            time.sleep(8)
            # Escrever o primeiro usuario da primeira conta
            pyautogui.write(usuarios)
            time.sleep(1)
            # Mover para o campo de usuario
            pyautogui.moveTo(648,306)
            time.sleep(0.2)
            # Mover para o campo da senha
            pyautogui.moveTo(648,373)
            pyautogui.click()
            time.sleep(0.2)
            # Escrever a senha da primeira conta
            pyautogui.write(senhas)
            time.sleep(0.3)
            # Mover para o botão de entrar na conta
            pyautogui.moveTo(767,446)
            pyautogui.click()
            time.sleep(2)
            # Clicar para fechar a parte de salvar conta
            pyautogui.moveTo(923,103)
            pyautogui.click()
            time.sleep(1.5)
            # Clicar na barra de pesquisa para trocar o link do site
            pyautogui.moveTo(401,73)
            pyautogui.click()
            pyautogui.write('br.betano.com/myaccount/marketingbonus') #Link da aba pra colocar o bonus
            pyautogui.press("enter")
            time.sleep(3)
            pyautogui.moveTo(446,380) # Caixa pra escrever o codigo bonus
            pyautogui.click()
            time.sleep(1)
            pyautogui.write('OGOLVIP') # Assim que entrar na aba ja escrever o bonus
            pyautogui.press("enter")
            # Fechar a página do bonus
            pyautogui.moveTo(446,380)
            pyautogui.click()
            time.sleep(1)
            # Clicar na barra de pesquisa para trocar o link do site
            pyautogui.moveTo(401,73)
            pyautogui.click()
            pyautogui.write('https://br.betano.com/myaccount/profile/edit') #Link da aba pra colocar o bonus
            pyautogui.press("enter")
            time.sleep(3)
            # Minimizar a primeira aba e fazer tudo dnv na segunda
            time.sleep(2)
            pyautogui.moveTo(996,20)
            pyautogui.click()
            contagem += 1

        messagebox.showinfo("Déposito", "O comando depósito foi executado")

    def exe_script2():
        # Implemente o script aqui
        #
        messagebox.showinfo("Saque", "O comando saque foi executado")

    # Crie um frame para conter os botões e centralize-os verticalmente
    button_frame = tk.Frame(main_window, bg=bg_color)
    button_frame.pack(expand=True, fill='both', pady=150)

    # Crie um frame interno para conter os botões script1 e script2
    button_frame_internal = tk.Frame(button_frame, bg=bg_color)
    button_frame_internal.pack()

    button_script1 = tk.Button(
        button_frame_internal, text="Depósito", command=exe_script1(),
        width=12, height=7, padx=5, pady=5, bg=button_color, fg=button_text_color, font=font, borderwidth=2, relief="solid"
    )
    button_script1.pack(side=tk.LEFT, padx=10)

    button_script2 = tk.Button(
        button_frame_internal, text="Saque", command=exe_script2(),
        width=12, height=7, padx=5, pady=5, bg=button_color, fg=button_text_color, font=font, borderwidth=2, relief="solid"
    )
    button_script2.pack(side=tk.LEFT, padx=5)

    main_window.mainloop()


login_window = tk.Tk()
login_window.geometry("500x480")
login_window.title("Login")
login_window.configure(bg=bg_color)  # Define a cor de fundo

# Crie um frame para conter os elementos de login e senha
login_frame = tk.Frame(login_window, bg=bg_color)
login_frame.pack(expand=True, fill='both', pady=150)

user_label = tk.Label(login_frame, text="Usuario:", bg=bg_color, font=font)
user_label.pack()

user_entry = tk.Entry(login_frame, font=font)
user_entry.pack()

password_label = tk.Label(login_frame, text="Senha:", bg=bg_color, font=font)
password_label.pack()

password_entry = tk.Entry(login_frame, show="*", font=font)
password_entry.pack()

login_button = tk.Button(
    login_frame, text="Login", command=verif_login,
    width=15, height=2, bg=button_color, fg=button_text_color, font=font, borderwidth=2, relief="solid"
)
login_button.pack(pady=20)  # Adicione espaçamento vertical

login_window.mainloop()
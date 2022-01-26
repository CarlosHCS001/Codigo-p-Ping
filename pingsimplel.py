import os ##Importa o modulo ou biblioteca os (integra os programas e
#recursos do S.O


print("#" * 60) ##Imprimindo 60 vezes

ip_ou_host = input("Digite o ip ou host a ser verificacao: ")
#criamos uma variavel que vai receber do usuario um ip
print("-" * 60) ##Imprimindo - 60 vezes
os.system('ping -n 6 {}'.format(ip_ou_host)) ##chamando system da biblioteca os - comando ping
print("-" * 60) ##imprimindo - 60 vezes
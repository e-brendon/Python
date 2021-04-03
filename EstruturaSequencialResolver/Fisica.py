#!/usr/bin/env python3

def menu():   
   print('As conversoes de medidas nao seram feitas pelo programa \n!!')
   print('digite o numero da ação pretendida \n')
   acao = (raw_input(' digite: 1 - Movinmento uniforme \n 2 - Movimento uniforme s=s0+v*t \n 3 - Conversão de km/h para m/s \n 4 - para sair do programa \n'))
   if (acao != '1' and acao != '2' and acao != '3' and acao != '4'):
      print ("Caracter invalido entrar com um dos números validos para a execusão do programa \n")
      menu()
   if (acao == '1'):
      deltaS = int(raw_input('Digite o valor de delta S \n'))
      deltaT = int(raw_input('Digite o valor de delta T \n'))
      if (deltaS == 0): 
                        deltaV = int(raw_input('Digite o valor da Velocidade \n'))
                        if (deltaT == 0):
            				print('Não e permitida divisão por 0!!')
         else:
            deltaSf = deltaV / deltaT
            print deltaSf
      elif (deltaT == 0): 
                        deltaV = int(raw_input('Digite o valor da Velocidade \n'))
                        if (deltaV == 0):
            print ('Não e permitida divisão por 0!!')
         else:
            deltaTf = deltaS / deltaV   
            print deltaTf
      else:
         deltaV = deltaS / deltaT
         print ('A velocidade é %s' % deltaV)
      resposta = (raw_input('Digite s para continuar a calcular ou n para sair!!! \n'))
      if (resposta != 's' and resposta != 'n'):
         print ('Caracter invalido, digitar apenas s ou n para a continuação ou cancelamento do programa')   
      if (resposta == 's'):
         menu()
   if (acao == '2'):
      S  = int(raw_input('Digite o valor de S  \n'))
      So = int(raw_input('Digite o valor de S0 \n'))
      V  = int(raw_input('Digite o valor de V \n'))
      T  = int(raw_input('Digite o valor de T  \n'))
      if (S == 0):
         S = So + V * T
         print ('O espaço é %s' % S)
      elif (T == 0):
         deltaS = S - So
         if (V == 0):
            print ('Operação invalida, nao pode ser efetuada divisao por 0!!')
         else:
            T = deltaS / V
            print ('O tempo é %s' % T)
      elif (V == 0):
         deltaS = S - So
         if (T == 0):
            print ('Operação invalida, nao pode ser efetuada divisao por 0!!')
         else:
            V = deltaS / V
            print ('O tempo é %s' % V)      
      else:
         deltaS = S - So
         result = deltaS + V * T
         print result
      resposta = (raw_input('Digite s para continuar a calcular ou n para sair!!! \n'))
      if (resposta != 's' and resposta != 'n'):
         print ('Caracter invalido, digitar apenas s ou n para a continuação ou cancelamento do programa')   
      if (resposta == 's'):
         menu()         
   if (acao == '3'):
      print('Convesão de kilometro por hora, para metros por segundo \n')
      convert = (raw_input('Digite o tipo de conversao, m = m/s para km/h ou k = km/h para m/s, \n'))
      if (convert != 'm' and convert != 'k'):
         print ('caracter invalido digite apensa k ou m para execusão do programa \n')
         menu()
      if (convert == 'm'):
         ms = int(raw_input('Digite o valor em Metros por segundo \n'))
         change = ms * 3.6
         print ('A velocidade em Kilometros por Hora é %s' % change + 'km/h')
      elif (convert == 'k'):
         km = int(raw_input('Digite o valor em Kilometros por Hora \n'))
         change = km / 3.6
         print ('A velocidade em Metros por segundo é %s' % change + 'm/s')
      resposta = (raw_input('Digite s para continuar a calcular ou n para sair!!! \n'))
      if (resposta != 's' and resposta != 'n'):
         print ('Caracter invalido, digitar apenas s ou n para a continuação ou cancelamento do programa')   
      if (resposta == 's'):
         menu()
   if (acao == '4' or resposta == 'n'):
      print ('bye bye (^_^)')
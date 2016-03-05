#!/usr/bin/python -u
# -*- coding: iso-8859-1 -*-
import sys
import cPickle
import scipy

if __name__ == '__main__':
 f = open(sys.argv[1],'rb')
 md = cPickle.load(f)
 db = cPickle.load(f)
 f.close()

 # nome das figuras
 name_arr = scipy.array(db1.keys())

# dicionario {nome das figuras : classes}
 cl = dict(zip(name_arr,[db1[n][0] for n in name_arr]))

# Acumulador para contabilizar desempenho do experimento
 tt = 0

 #print "Calculando bull eye score"
 for i,nome in zip(scipy.arange(Nobj),name_arr):
 # Para cada linha de md estabelece rank de recuperação
 # ordenando a linha em ordem crescente de similaridade 
 # O primeiro elemento da linha corresponde a forma modelo
  idx = scipy.argsort(md[i])
 # pega classe a qual pertence a imagem modelo
  classe_padrao = cl[nome]
# nome das imagens recuperadas em ordem crescente de similaridade
  name_retr = name_arr[idx]
 # pega classes a qual pertencem as imagens recuperadas
  aux = [cl[j] for j in name_retr]
  # estamos interessados apenas nos Nretr (40) resultados
  classe_retrs = aux[0:Nretr]
  # Contabiliza desempenho contando o número de formas da mesma classe
  # do modelo (tp) dentre as 40 recuperadas
  # Atualiza o resultado acumulado (tt)
  n = scipy.nonzero(scipy.array(classe_retrs) == classe_padrao)
  tp = float(n[0].size)
  tt = tt + tp
    
# Bull eye
 print tt/float(1400*20)  

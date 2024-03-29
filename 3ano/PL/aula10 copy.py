"""
ESI pós-laboral (Processamento de Linguagens)
Aula 10 -   16/março quinta-feira, 20:30-22:30
"""
# -----
# definição do Autómato Finito 
#    AF=(V,Q,delta,q0,F) tal que:
# V = {"0", "1", ... }
V = { str(x) for x in range(0,10)  }  # {x : x pertence a [0,1,2,..]}
Q = { "q0", "q1"}
delta = {   "q0": { "digito":"q1", "0": "q2"           },
	        "q1": { "digito":"q1", "0": "q1" }  ,
			"q2": { } 
         } 
q0 = "q0"
F = {"q1", "q2"}

def  edigito(c):
    return (c in V) and (c != "0") 

print(edigito("0"))
print(edigito("1"))
# -----
# especificação da função para avaliar se uma dada 
# palavra é reconhecida reconhecida no Autómato AF 
def reconhece(palavra:str):
	estado_atual= q0
	tam = len(palavra)
	i = 0
	while (i<tam) and (estado_atual != "Erro"):
		simbolo_atual = palavra[i]
		# print(simbolo_atual)
		# if (simbolo_atual in V) and (simbolo_atual in delta[estado_atual] ):
		# if (simbolo_atual in delta[estado_atual] ):
		if  edigito(simbolo_atual) and ("digito" in delta[estado_atual]) :
			#print("digito")
			estado_atual = delta[estado_atual]["digito"]
		elif (simbolo_atual=="0") and (simbolo_atual in delta[estado_atual]):
			estado_atual = delta[estado_atual]["0"]
		else:
			estado_atual = "Erro"
		i+=1
	return (estado_atual in F) and (i==tam)	

# -----
# Exemp	los de utilização da função reconhece 
for exemplo in ["", "0", "1", "00", "01", "10", "897", "0a"]:
	print(f"'{exemplo}'\t{reconhece(exemplo)}")

# ----- 
# como utilizar 
#  >python3 aula09.py
# resultado apresentado 
#  'ab'    True
#  'aba'   True
#  'abb'   True
#  'a'     False
#  'aa'    False
#  'ba'    False
#  'abc'   False
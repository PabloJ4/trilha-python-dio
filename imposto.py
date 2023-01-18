def SomaImposto(taxaImposto,custo):

  imposto = custo * taxaImposto
  custo_total = custo+imposto

  return imposto,custo_total

  
print(SomaImposto(0.10,250.00))
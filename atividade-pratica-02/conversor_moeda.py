valor_real = 100.00

taxa_dolar = 5.60 
taxa_euro = 6.60

conversao_dolar = valor_real / taxa_dolar 
conversao_euro =  valor_real / taxa_euro

print(f"O valor da conversão de real para dolar é ${conversao_dolar:.2f}")
print(f"O valor da conversão de real para euro é {conversao_euro:.2f} €")

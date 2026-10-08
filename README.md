## Implementar a classe Carrinho em src/carrinho.py, que gerencia itens e calcula o total da compra.

# Requisitos (5)

1. adicionar_item(nome, preco, quantidade=1) adiciona um item. Se o nome já existir, soma a quantidade.
2. remover_item(nome) remove o item. Se não existir, lança ValueError.
3. show mostrando a lista de todos os itens no carrinho.
4. Frete de R$ 20,00, grátis se o total for maior ou igual a R$ 150,00.
5. total() retorna total, arredondado a 2 casas. Carrinho vazio retorna 0.00.
   
# Critérios de conclusão (6)

1. Todos os 5 requisitos implementados.
2. Os testes do pytest passam.
3. Os ValueError são lançados nos casos descritos.
4. Valores monetários arredondados a 2 casas.
5. Os exemplos de entrada e saída abaixo produzem exatamente o resultado indicado.
6. O código roda sem erro com python -m pytest.

# Exemplos de entrada/saída

Entrada: Camiseta 50,00 × 2
Saída: subtotal 100,00; desconto 0; frete 20,00; total 120,00

Entrada: Tênis 220,00 × 1
Saída: subtotal 220,00; desconto 22,00; frete 0 (198,00 ≥ 150); total 198,00

Entrada: Notebook 600,00 × 1
Saída: subtotal 600,00; desconto 90,00; frete 0; total 510,00

Entrada: Carrinho vazio
Saída: total 0,00

Entrada: adicionar_item("x", -5)
Saída: ValueError

# Restrições

1. Apenas Python 3.10+ e biblioteca padrão (o requirements.txt só lista pytest).
2. Não alterar a assinatura dos métodos fornecidos.
3. Não modificar os arquivos em tests/.

# Testes automatizados ()

1. test_subtotal_soma_itens_e_acumula_quantidade
2. test_desconto_10_e_15_por_cento_nas_faixas (incluindo o limite exato de 200 e 500)
3. test_frete_gratis_apos_desconto (caso em que o subtotal é ≥ 150, mas o valor com desconto fica abaixo)
4. test_erros_validacao (ValueError em preço, quantidade e remoção inexistente)
5. test_carrinho_vazio_sem_frete

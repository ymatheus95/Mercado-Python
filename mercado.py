from typing import List, Dict
from time import sleep

from models.produto import Produto
from utils.help import formata_float_str_moeda

produtos: List[Produto] = []
carrinho: List[Dict[Produto, int]] = []

def main() -> None:
    menu()

def menu() -> None:
    print('=======================================')
    print('============ Bem vindo ================')
    print('=========== MasInfo Shop ++++++++++++++')
    print('=======================================')

    print('Selecione uma opção abaixo:')
    print('1 - Cadastrar Produto')
    print('2 - Listar produto')
    print('3 - Comprar produto')
    print('4 - Visualizar produto')
    print('5 - Fechar carrinho')
    print('6 - Sair')
    opcao: int = int(input())
    if opcao == 1:
        cadastrar_produto()
    elif opcao == 2:
        listar_produto()
    elif opcao == 3:
        comprar_produto()
    elif opcao == 4:
        visualizar_carrinho()
    elif opcao == 5:
        fechar_pedido()
    elif opcao == 6:
        print('Volte sempre')
        sleep(2)
    else:
        print('Opção Invalida')
        sleep(1)
        menu()



def cadastrar_produto() -> None:
    print('Cadastro de produto')
    print('====================')
    nome: str = input('Informe o nome do produto: ')
    preco: float = float(input('Informe o preco do produto: '))
    produto: Produto = Produto(nome, preco)
    produtos.append(produto)
    print(f'o produto {produto.nome} foi cadastrado com sucesso.')
    sleep(2)
    menu()

def listar_produto() -> None:
    if len(produtos) > 0:
        print('Listagem de produtos')
        for produto in produtos:
            print(produto)
            print('-----------------')
            sleep(1)
        menu()
    else:
        print('Ainda não existem produtos cadastradors.')
    sleep(3)
    menu()

def comprar_produto() -> None:
    if len(produtos) > 0:
        print('Informe o código do produtod que deseja adicionar no carrinho:')
        print('--------------------------------------------------------------')
        print('############## Produtos Disponíveis ##########################')
        for produto in produtos:
            print(produto)
            print('----------------------------------------------------------')
            sleep(1)
        codigo: int = int(input('Entre com o código do produto: '))
        produto: Produto = pega_produto_por_codigo(codigo)
        if produto:
            if len(carrinho) > 0:
                tem_no_carrinho: bool = False
                for item in carrinho:
                    quant: int = item.get(produto)
                    if quant:
                        item[produto] = quant + 1
                        print(f'O produto {produto.nome} agora possui `{quant + 1 } unidade no carrinho.')
                        sleep(2)
                        menu()
                if not tem_no_carrinho:
                    prod = {produto: 1}
                    carrinho.append(prod)
                    print(f'O produto {produto.nome} foi adicionado.')
            else:
                item = {produto: 1}
                carrinho.append(item)
                print(f'O produto {produto.nome} foi adicionado ao carrinho.')
                sleep(2)
                menu()
        else:
            print(f'O produto com o código {codigo} não foi encontrado.')
            sleep(2)
            menu()

    else:
        print('Ainda não existe produto cadastrado.')
        sleep(3)
        menu()

def visualizar_carrinho() -> None:
    if len(carrinho) > 0:
        print('Produtos no carrinho')
        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'Quantidade: {dados[1]}')
                print('-----------------------')
                sleep(1)
        menu()
    else:
        print('Não existem produtos no carrinho.')
        sleep(2)
        menu()
def fechar_pedido() -> None:
    if len(carrinho) > 0:
        valor_total: float = 0
        print('Produtos do carrinho')
        for item in carrinho:
            for dados in item.items():
                print(f'{dados[0]}\nQuantidade: {dados[1]}.')
                valor_total += dados[0].preco * dados[1]
                print('--------------------------------')
                sleep(1)
        print(f'Sua fatura é {formata_float_str_moeda(valor_total)}.')
        print('Volte sempre')
        carrinho.clear()
        sleep(5)

    else:
        print('Ainda não existem produtos no cariinho.')
        sleep(2)
        menu()

def pega_produto_por_codigo(codigo: int) -> None:
    p: Produto = None
    for produto in produtos:
        if produto.codigo == codigo:
            p = produto
            return p

menu()
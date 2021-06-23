def fisica():
    def title(ttl='Title Not Found', tpl=1):
        print('-' * 10, f'{ttl}', '-' * 10)

    def linha(op, sz=20):
        if op == 1:
            print('_' * sz)
        elif op == 2:
            print('-' * sz)
        elif op == 3:
            print('=' * sz)
        elif op == 4:
            print('=-' * sz)

    def opcoes():
        sleep(1)
        linha(4)
        print('1)Cinemática')
        sleep(0.5)
        linha(2)
        sleep(0.1)
        print('2)Dinâmica')
        sleep(0.5)
        linha(2)
        sleep(0.1)
        print('3)Trabalho, potência e energia')
        sleep(0.5)
        linha(2)
        sleep(0.1)
        print('4)Impulso e Quantidade de Movimento')
        sleep(0.5)
        linha(2)
        sleep(0.1)
        print('5)Hidrostática')
        sleep(0.5)
        linha(2)
        sleep(0.1)
        print('6)Gravitação Universal')
        sleep(0.5)
        linha(2)
        sleep(0.1)
        print('7)Termologia e Termodinâmica')
        sleep(0.5)
        linha(2)
        sleep(0.1)
        print('8)Ondas e Ótica')
        sleep(0.5)
        linha(2)
        sleep(0.1)
        print('9)Eletricidade')
        sleep(0.5)
        linha(2)
        sleep(0.1)
        print('10)Eletromagnetismo')
        linha(4)

    def cinamatica():
        def opcoescnm():
            linha(4)
            print('1)Movimento Retilíneo Uniforme')
            linha(2)
            print('2)Movimento Retilíneo Uniformemente Variado')
            linha(2)
            print('3)Movimento Circular Uniforme')
            linha(2)
            print('4)Lançamento Oblíquo')
            linha(4)

        while True:
            title('Cinemática')
            print('O que você quer calcular?')
            opcoescnm()
            resp = str(input('Sua escolha: '))
            linha(4)
            if resp == '1':
                s0 = float(input('s0= '))
                v = float(input('v='))
                t = float(input('∆t='))
                print(f's={s0 + v * t}')
            elif resp == '<':
                break

    from time import sleep
    print('Bem vindo(a), eu sou a Jade, e estou aqui para te ajudar com seus problemas de física.')
    sleep(1)

    while True:
        print('Escolha a opção digitando o numero respectivo dela:')
        opcoes()
        resp = str(input('Sua escolha:'))
        linha(4)
        if resp == '1':
            cinamatica()
        elif resp == '<':
            confirm = str(input('Já vai?[S/N]:'))
            if confirm == 'S':
                break

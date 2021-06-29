def fisica():
    def title(ttl='Title Not Found', tpl=1):
        print('\n-' * 10, f'{ttl}', '-' * 10)

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
        options = ('Cinemática', 'Dinâmica', 'Trabalho, potência e energia',
                   'Impulso e Quantidade de Movimento', 'Hidrostática', 'Gravitação Universal',
                   'Termologia e Termodinâmica', 'Ondas e Ótica', 'Eletricidade', 'Eletromagnetismo')
        n = 0
        for item in options:
            n += 1
            if n == 1:
                linha(4)
            else:
                linha(2)
            print(f'{n}){item}')
            if n == len(options):
                linha(4)

    def cinamatica():
        def opcoescnm():
            options = ('Movimento Retilíneo Uniforme', 'Movimento Retilíneo Uniformemente Variado',
                       'Movimento Circular Uniforme', 'Lançamento Oblíquo')
            n = 0
            for item in options:
                n += 1
                if n == 1:
                    linha(4)
                else:
                    linha(2)
                print(f'{n}){item}')
                if n == len(options):
                    linha(4)

        while True:
            title('Cinemática')
            print('O que você quer calcular?')
            opcoescnm()
            resp = str(input('Sua escolha: '))
            linha(4)
            if resp == '1':
                s0 = float(input('s0(posição inicial)= '))
                v = float(input('v(velocidade)='))
                t = float(input('∆t(intervalo de tempo)='))
                print(f's(posição final)={s0 + v * t}')
            elif resp == '<':
                break

    from time import sleep
    print('Bem vindo(a), eu sou a Jade, e estou aqui para te ajudar com seus problemas de física.')
    sleep(1)

    while True:
        print('Escolha a opção digitando o respectivo número dela:')
        opcoes()
        resp = str(input('Sua escolha:'))
        linha(4)
        if resp == '1':
            cinamatica()
        elif resp == '<':
            confirm = str(input('Já vai?[S/N]:'))
            if confirm == 'S':
                break

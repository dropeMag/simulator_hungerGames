import random
import time

# LISTAS - CARACTERÍSTICAS TRIBUTOS
# trib_selecionados = [f"trib{x:02}" for x in range(1, 25)]
trib_selecionados = ["trib01", "trib02", "trib03", "trib04", "trib05", "trib06", "trib07", "trib08", "trib09", "trib10", "trib11", "trib12", "trib13", "trib14", "trib15", "trib16", "trib17", "trib18", "trib19", "trib20", "trib21", "trib22", "trib23", "trib24"]
trib_nome_femininos = ["Julia", "Sophia", "Isabella", "Manuela", "Giovanna", "Alice", "Laura", "Beatriz", "Mariana", "Yasmin", "Gabriela", "Rafaela", "Isabelle", "Lara", "Letícia", "Valentina", "Nicole", "Eduarda", "Rebeca", "Amanda", "Alícia", "Bianca", "Lavínia", "Ester", "Carolina", "Emily", "Cecília", "Pietra", "Milena", "Marcela", "Natália", "Maria", "Bruna", "Camila", "Luana", "Catarina", "Olivia", "Agatha", "Mirella", "Sophie", "Stella", "Stefany", "Isabel", "Kamilly", "Elisa", "Joana", "Mariane", "Bárbara", "Juliana", "Rayssa", "Alana", "Caroline", "Brenda", "Evelyn", "Débora", "Raquel", "Maitê", "Ana", "Nina", "Luiza", "Antonella", "Jennifer", "Betina", "Mariah", "Sabrina"]
trib_nome_masculinos = ["Miguel", "Davi", "Gabriel", "Arthur", "Lucas", "Matheus", "Pedro", "Guilherme", "Gustavo", "Rafael", "Felipe", "Bernardo", "Nicolas", "Cauã", "Vitor", "Eduardo", "Daniel", "Henrique", "Thiago", "Theo", "Bruno", "Bryan", "Breno", "Emanuel", "Ryan", "Yuri", "Benjamin", "Erick", "Enzo", "Fernando", "Joaquim", "André", "Tomás", "Francisco", "Rodrigo", "Igor", "Antonio", "Ian", "Juan", "Diogo", "Otávio", "Nathan", "Calebe", "Danilo", "Luan", "Kaique", "Alexandre", "Iago", "Ricardo", "Raul", "Marcelo", "Cauê", "Benício", "Augusto", "Geovanni", "Renato", "Diego", "Renan", "Anthony", "Thales", "Henry", "Kevin", "Levi", "Enrico", "Hugo"]
trib_nome_sobrenomes = ["Silva", "Santos", "Oliveira", "Souza", "Novais", "Cândido", "do Amaral", "Moreira", "Serra", "Abravanel", "Rodrigues", "Mello", "Mel", "Ferreira", "Alves", "Pereira", "Lima", "Gomes", "Alencar", "Costa", "Ribeiro", "Martins", "Carvalho", "Egue", "Almeida", "Lopes", "Soares", "Fernandes", "Vieira", "Barbosa", "Rocha", "Dias", "Nascimento", "Firmino", "Andrade", "Moreira", "Nunes", "Marques", "Machado", "Mendes", "Freitas", "Cardoso", "Villa", "Ramos", "Gonçalves", "Santana", "Pontes", "Teixeira", "Falcão", "Magalhães", "Campos"]
trib_distritos = ["Artigos de Luxo", "Alvenaria e Armamento", "Tecnologia", "Pesca", "Energia", "Transporte", "Madeira", "Industria Téxtil", "Distribuição Agrícola", "Pecuária", "Agricultura", "Mineração"]

# LISTAS - CARACTERÍSTICAS EDIÇÃO
tipos_comidas = ["as carcaças de algum animal", "as fezes de algum animal", "terra do chão", "parte de sua roupa", "suas próprias unhas", "as fezes de outro tributo", "suas próprias fezes", "o corpo morto de {} [DIST. {}]"]
tipos_mortes = ["ao cair de uma grande altura", "ao pisar em uma mina terrestre", "por suicídio"]
tipos_armas = ["uma picareta", "um tridente", "uma foice", "um chakram", "um chicote com lâminas", "uma machete", "uma faca kukri", "um longo bastão", "uma espada larga", "uma espada curta", "um arco e flechas", "um martelo", "uma lança", "uma maça", "uma adaga", "um machado"]
tipos_paraquedas = ["{}", "óculos noturnos", "cordas", "saco de dormir", "escudo", "comida", "água", "remédio", "uma armadura", "um kit de sobrevivência", "um uniforme de camuflagem"]
tipos_idealizadores = []

tipos_arenas = ["Floresta Tropical", "Deserto", "Savana", "Taiga", "Cidade Destruida", "Áreas Úmidas", "Caverna de Mineração", "Navio Abandonado", "Labirinto"]
tipos_edicao = [
    # comidas
    ("uma fruta saborosa", "uma ave que caçou", "um peixe que pescou", "as carcaças de um javali", "algumas nozes", "um lagarto"),
    ("carne de roedor", "galhos de um arbusto", "folhas de palmeira", "uma cobra que caçou", "as carcaças de um coiote", "frutos de um cacto"),
    ("raízes de uma planta", "galhos de um arbusto", "uma ave que caçou", "as carcaças de uma hiena", "as carcaças de uma cobra", "uma fruta podre"),
    ("raízes de uma planta", "algumas bagas", "um coelho que caçou", "um peixe que pescou", "as carcaças de um alce", "uma ave que caçou"),
    ("um rato morto", "pedaços de grama", "alguns cogumelos esquisitos", "umas plantas daninhas", "algumas baratas", "comidas estragadas do lixo"),
    ("um peixe que pescou", "uma vitória régia", "uma ave que caçou", "um sapo estranho", "alguns crustáceos", "umas plantas aquáticas"),
    ("barras nutritivas de um baú", "fruta em um baú", "pão de um baú", "um peixe que pescou", "algumas aranhas", "carne de morcego"),
    ("comida estragada na cozinha", "folhas de uma planta", "pão de uma mala", "uma ave que caçou", "um peixe que pescou", "um peixe morto"),
    ("um rato que caçou", "raízes de uma planta", "pedaços de cipó", "folhas de plantas", "umas frutas estranhas", "algumas bagas"),
    # mortes
    ("por picada de insetos", "ao comer uma planta venenosa", "por infecção bacteriana", "por ataque de javali", "por ataque de jacaré", "por picada de aranha", "de insolação"),
    ("na areia movediça", "por picada de abelha-africanizada", "de hipotermia", "ao comer um cacto venenoso", "por ataque de coiotes", "por picada de escorpião", "por picada de víbora"),
    ("de insolação", "por ataque de hipopótamo", "por ataque de crocodilo", "por ataque de hienas", "ao comer uma planta venenosa", "por picada de insetos", "de infecção bacteriana"),
    ("por picada de víbora", "por ataque de um tigre de Amur", "ao afundar num lago congelado", "de hipotermia", "por ataque de lobos cinzas", "por ataque de urso", "ao comer uma planta venenosa"),
    ("por causa da radiação", "ao se enterrar em entulhos", "por ataque de mutantes", "por asfixia na núvem de poeira", "no fogo de um prédio em chamas", "por ataque de cães mutantes", "ao inalar mofo radioativo"),
    ("por infecção bacteriana", "por picada de insetos", "ao se afogar no lago", "na areia movediça", "por ataque de onça", "por picada de víbora", "por ataque de jacaré"),
    ("ao se afogar num lago da caverna", "de hipotermia", "ao se prender em um buraco sem ar", "no soterramento de pedras", "na queda de estalactites", "ao cair em estalagmites", "por picada de aranha"),
    ("ao inalar mofo venenoso", "ao se afogar no mar", "por picada de insetos", "na explosão de um motor", "em um incêndio", "por infecção bacteriana", "de desidratação"),
    ("ao se afogar em uma onda gigante", "por ataque de cipós mutantes", "na queda de pedras grandes", "por ataque de cobra gigante", "em um incêndio", "por ataque de mutante", "por ataque de abutre gigante"),
    # paraquedas
    ("repelente", "protetor solar", "um spile"),
    ("protetor solar", "óculos solar", "máscara para areia"),
    ("chapéu e óculos", "repelente", "protetor solar"),
    ("uma jaqueta térmica", "uma perdeneira", "combustível para fogueira"),
    ("máscara respiratória", "iodeto de potássio", "purificador de água"),
    ("um bote inflável", "equipamento de mergulho", "repelente"),
    ("um minimapa", "uma lanterna", "um equipamento de exploração"),
    ("uma vara de pesca", "um filtro de água", "equipamento de mergulho"),
    ("um mapa da região", "tênis de corrida", "uma lanterna"),
    # idealizadores
    ("piranhas geneticamente modificadas", "plantas carnívoras gigantes", "aves mutantes"),
    ("vampiros de deserto", "chuva ácida", "cães mutantes"),
    ("arbustos envenenados", "tornado de areia ácida", "formigas alucinógenas"),
    ("chuva de pingente de gelo", "avalanche", "nevoeiro"),
    ("casulos explosivos", "rato gigante mutante", "núvem de gás tóxico"),
    ("zumbis do pântano", "mosquitos mutantes", "inundação"),
    ("morcegos vampiros", "terremoto", "aranha gigante"),
    ("gás tóxico", "chuva ácida", "ratos mutantes"),
    ("trepadeiras carnívoras", "lobos mutantes", "névoa alucinógena"),
    # ações
    ("Tomou banho em um rio", "Fez um chapéu de cipó", "Se refrescou em uma cachoeira", "Levou picadas de formigas", "Ficou olhando as borboletas"),
    ("Fez desenhos na areia", "Se escondeu entre rochas", "Se banhou no oásis", "Se machucou nos cactos", "Fez castelinho de areia"),
    ("Se escondeu de predadores", "Se machucou nos arbustos", "Desconsou em uma árvore", "Caiu em um formigueiro", "Se banhou em um lago"),
    ("Arremessou bolas de neve nas árvores", "Fez um boneco de neve", "Fez anjinho de neve", "Atravessou um lago congelado", "Ficou coletando pinhas"),
    ("Fez desenhos nas paredes", "Ficou preso no lixão", "Tentou achar água nos encanamentos", "Procurou comida em entulhos", "Se escondeu em um carro carbonizado"),
    ("Ficou brincando na lama", "Fez um chapéu com cipós", "Ficou admirando as aves", "Deu uma nadada no lago", "Tomou banho num rio"),
    ("Ficou admirando os cristais brilhantes", "Se escondeu num carrinho de mineração", "Fez desenhos nas paredes", "Se prendeu em um buraco sem saída", "Bebeu água de um lago que achou"),
    ("Revirou os quartos em busca de comida", "Ficou admirando as ondas", "Caiu em uma escada quebrada", "Tomou banho de sol", "Se banhou na chuva"),
    ("Notou que as paredes se moviam", "Se escondeu de algo voador", "Se prendeu em um beco sem saída", "Fez bonecos com cipós", "Correu até cansar")]

# LISTAS - AÇÕES TRIBUTOS
acao_normal = ["Caiu na armadilha de outro tributo", "Ameaçou matar todos da Capital", "Ficou gritando pedindo para morrer", "Cogitou beber a própria urina", "Viu algo se mexendo e correu", "Treinou seus movimentos de luta"]
acao_saude = ["Está tendo diarréia", "Começou a ter náuseas", "Está com febre", "Começou a ter alucinações", "Está com hiperidrose", "Teve aumento excessivo da libido", "Teve sérios delírios", "Está bem de saúde"]
acao_emocao = ["Chorou de medo", "Teve uma crise de ansiedade", "Chorou pedindo a mamãe", "Gritou de raiva", "Gritou prometendo vencer", "Ficou parado olhando para o nada", "Ficou rindo do nada", "Ficou xingando a Capital"]

acao_encontro = ["Observou e imaginou {} [DIST. {}] sem roupas", "Ficou com fome vendo {} [DIST. {}] cagando", "Ficou admirando {} [DIST. {}] mijando", "Pensou ter visto {} [DIST. {}]", "Trombou com {} [DIST. {}] e saiu correndo", "Ficou stalkeando {} [DIST. {}] enquanto banhava", "Afugentou {} [DIST. {}], que estava descansando"]
acao_matar = ["Matou {} [DIST. {}] enquanto dormia", "Matou {} [DIST. {}]", "Peseguiu e matou {} [DIST. {}]", "Matou {} [DIST. {}] enquanto defecava", "Matou {} [DIST. {}], depois de dias tentando"]
acao_cacar = ["Tentou matar {} [DIST. {}], mas falhou", "Coreu atrás de {} [DIST. {}], mas não alcançou", "Pensou em matar {} [DIST. {}], mas desistiu", "Planejou matar {} [DIST. {}], mas não tinha chances"]

acao_cornucopia = ["{}", "Pensou em ir à Cornucópia, mas desistiu", "Voltou à Cornucópia e pegou uma sacola com comida", "Voltou à Cornucópia e pegou uma mochila"]

acao_dormir = ["Dormiu sentado", "Dormiu no chão", "Dormiu de olhos abertos", "Dormiu em uma cabana improvisada", "Dormiu abraçado com uma pedra"]
acao_naoDormir = ["Ficou sem dormir a noite toda", "Fingiu que estava dormindo", "Teve insônia e não dormiu", "Tentou dormir, mas não conseguiu", "Ficou com medo de dormir"]

# REGISTROS - DADOS GERAIS
regis_edicao = [random.randint(15, 74)]
regis_mortos = []
regis_vencedor = []
regis_aposta = []

# DECISÕES - CORNUCÓPIA
deci_cornu = ["Foi lutar na Cornucópia", "Correu para a Cornucópia", "Fugiu para longe da Cornucópia"]


# FUNÇÕES ÚTEIS
def impressor(msg):
    print(f"{msg:^120}")


def narracao(titulo):
    impressor(titulo)

    for nar_trib in trib_selecionados:
        impressor(f"{nar_trib.nome.upper()} {nar_trib.sobrenome.upper()} [DIST.{nar_trib.distrito[:2]:2}]")
        print('')
        for nar_acao in nar_trib.acoes:
            impressor(f"{f'+ {nar_acao}':<60}")

        if nar_trib.morto:
            impressor(f"{f'x {nar_trib.baixa}':<60}")

        if len(regis_mortos) == 23 and not nar_trib.morto:
            impressor(f"{'# Tributo Vencedor dos Jogos Vorazes':<60}")

        nar_trib.acoes.clear()
        impressor('-  ' * 21) if nar_trib != trib_selecionados[-1] else impressor('\n\n')
        time.sleep(0.2)

    remocao_mortos(trib_selecionados[:])


def remocao_mortos(lista_tributos):
    for tributo in lista_tributos:
        if tributo in regis_mortos:
            trib_selecionados.remove(tributo)


def interacoes_tributo(esc_trib, lst_tributos, cornucopia=False, matar=False, cacar=False, encontro=False):
    while True:
        esc_vitima = random.choice(lst_tributos)
        if esc_vitima != esc_trib and esc_trib.assassino != esc_vitima and not esc_vitima.morto:
            break

    if matar:
        esc_trib.vitimas.append(esc_vitima)
        if cornucopia:
            esc_trib.acoes.append(f"Matou {esc_vitima.nome} [DIST. {esc_vitima.distrito[:2]:2}] com {esc_trib.arma}")
        else:
            esc_trib.acoes.append(random.choice(acao_matar).format(esc_vitima.nome, f'{esc_vitima.distrito[:2]:2}'))

        esc_trib.sorte += 10
        esc_vitima.morto = True
        regis_mortos.append(esc_vitima)
        esc_vitima.assassino = esc_trib
        esc_vitima.baixa = f'Morto por {esc_trib.nome} [DIST. {esc_trib.distrito[:2]:2}] com {esc_trib.arma}'

    elif cacar:
        esc_trib.acoes.append(random.choice(acao_cacar).format(esc_vitima.nome, f'{esc_vitima.distrito[:2]:2}'))
        esc_vitima.sorte += 3

    elif encontro:
        esc_trib.acoes.append(random.choice(acao_encontro).format(esc_vitima.nome, f'{esc_vitima.distrito[:2]:2}'))


# CLASSES DE CRIAÇÃO
class Tributo:
    def __init__(self, t_s, t_d):
        if t_s:
            self.nome = random.choice(trib_nome_femininos)
            self.sexo = 'Feminino'
        else:
            self.nome = random.choice(trib_nome_masculinos)
            self.sexo = 'Masculino'

        self.sobrenome = random.choice(trib_nome_sobrenomes)
        self.distrito = f'{t_d:2} - {trib_distritos[t_d-1]}'
        self.idade = random.randint(12, 18)
        self.sorte = random.randint(5, 90)
        self.acoes = list()
        self.vitimas = list()
        self.arma = 'as mãos'
        self.morto = False
        self.baixa = ''
        self.assassino = ''


class Arena:
    def __init__(self):
        esc_are = random.randint(0, 8)
        for obj in tipos_edicao[esc_are]:
            tipos_comidas.append(obj)

        for obj in tipos_edicao[esc_are + 9]:
            tipos_mortes.append(obj)

        for obj in tipos_edicao[esc_are + 18]:
            tipos_paraquedas.append(obj)

        for obj in tipos_edicao[esc_are + 27]:
            tipos_idealizadores.append(obj)

        for obj in tipos_edicao[esc_are + 36]:
            acao_normal.append(obj)

        regis_edicao.append(esc_are)


class Boas_Vindas:
    def __init__(self):
        impressor('=-' * 60)
        impressor(r"""                    _____  ___  _____  ___  ____      __     _____  ____     _  _______ ______ ____
                   |___  |/ _ \|  ___|/ _ \/ ___|     \ \   / / _ \|  _ \   / \ |___  /| _____/ ___|
                    _  | | | | | |  _| | | \___ \      \ \ / | | | | |_| | / _ \   / / |  __| \___ \ 
                   | |_| | | | | |_| | |_| |___| |      \ V /| |_| |  _ < / ___ \ / /__| |____ ___| |
                   |_____|\___/|_____|\___/|____/        \_/  \___/|_| \_/_/   \_\_____|______|____/""")
        print()
        impressor('=-' * 60)
        impressor('Olá, Patrocinador!')
        impressor(f"{f'É um prazer te-lo(a) aqui na {regis_edicao[0]}ª edição dos Jogos Vorazes!':^120}")
        impressor(f"{'Esse ano os tributos competirão sem armas de fogo em uma arena com o tema:':^120}")
        impressor(f"{tipos_arenas[regis_edicao[1]]}.")
        print()
        time.sleep(1)
        impressor(f"{'Veja o que os nossos idealizadores prepararam para a sua diversão:':^120}")
        impressor(f"{tipos_idealizadores[0].capitalize()};")
        impressor(f"{tipos_idealizadores[1].capitalize()};")
        impressor(f"{tipos_idealizadores[2].capitalize()}.")
        print()
        time.sleep(1)
        impressor(f"{'Escolha o número do tributo que deseja apostar e escolha um valor!':^120}")
        print()
        time.sleep(1)
        impressor(f"{'Bons Jogos Vorazes, e que a sorte esteja sempre a seu favor!':^120}")
        impressor('=-' * 60)
        print()
        time.sleep(2)
        print()


class Aposta:
    def __init__(self):
        impressor('CARDÁPIO DE APOSTA')
        impressor('_' * 46)
        impressor(f"|{'ID':^4} {'NOME':^25} {'IDADE':^7} {'SORTE':^7}|")

        cnt_trib = 0
        for trib in trib_selecionados:
            if trib_selecionados.index(trib) % 2 == 0:
                impressor(f"{'|' + ' ' * 46 + '|'}")
                impressor(f"|{'DISTRITO ' + trib.distrito[:3]:^46}|")
            impressor(f"|{cnt_trib + 1:^4}| {trib.nome + ' ' + trib.sobrenome:24}|{trib.idade:^7}|{trib.sorte:>4}%  |")
            cnt_trib += 1

        impressor(f"{'|' + '_' * 46 + '|'}")

        print()
        print(f"{' ':43}EM QUEM VOCÊ APOSTARÁ?")
        while True:
            try:
                aposta_id = int(input(f"{' ':43}ID: "))
                if aposta_id not in range(1, 25):
                    raise Exception
            except Exception:
                impressor('id inválido')
            else:
                regis_aposta.append(trib_selecionados[aposta_id - 1])
                break

        print()
        print(f"{' ':43}QUANTO APOSTARÁ EM {regis_aposta[0].nome} {regis_aposta[0].sobrenome} [DIST. {regis_aposta[0].distrito[:2]:2}]?")
        while True:
            try:
                aposta_valor = float(input(f"{' ':43}R$: ").replace(",", "."))
            except Exception:
                impressor('valor inválido')
            else:
                regis_aposta.append(f"{aposta_valor:.2f}")
                break

        print()
        impressor(f'A SUA APOSTA DE R$ {regis_aposta[1]} EM {regis_aposta[0].nome} {regis_aposta[0].sobrenome} [DIST. {regis_aposta[0].distrito[:2]:2}] FOI SALVA!')
        impressor('BOA SORTE!\n')
        time.sleep(1.5)
        impressor('=-' * 60)
        print()
        time.sleep(1.5)
        print()

    def resultado(self):
        input(f"{'enter para continuar':^120}\n")
        print()
        impressor('=-' * 60)
        impressor('Olá novamente, Patrocinador!')
        impressor('Vim trazer o resultado de sua aposta.\n')
        time.sleep(1.5)

        if regis_aposta[0] == regis_vencedor[0]:
            impressor('Parabéns, você apostou no tributo certo!')
            regis_aposta[1] = regis_aposta[1] * regis_vencedor[0].sorte
            impressor(f'Por isso você ganhou R$ {regis_aposta[1]}!\n')
        else:
            impressor('Infelizmente você apostou no tributo errado.')
            impressor('Por isso você perdeu o dinheiro apostado. Sentimos muito.\n')

        time.sleep(1.5)
        impressor('Esperamos ve-lô novamente no próximo Jogos Vorazes!')
        time.sleep(1.5)
        impressor('Consegue imaginar o que mais pode acontecer?')
        time.sleep(1.5)
        impressor('Até mais! E obrigado por participar!\n')
        input(f"\n{'enter para encerrar':^120}")


class Cornucopia:
    def __init__(self):
        lst_trib = random.sample(trib_selecionados, len(trib_selecionados))
        lst_corn = []

        for esc_inicio in lst_trib:
            if esc_inicio.sorte <= 13:
                esc_inicio.morto = True
                esc_inicio.baixa = "Explodiu na plataforma"
                regis_mortos.append(esc_inicio)
                continue

            esc_acao = random.choice(deci_cornu)
            esc_inicio.acoes.append(esc_acao)
            if "Fugiu" not in esc_acao:
                lst_corn.append(esc_inicio)

        for esc_corn in random.sample(lst_corn[:], len(lst_corn)):
            if esc_corn.sorte >= 40 and 'mãos' in esc_corn.arma:
                esc_corn.arma = random.choice(tipos_armas)
                esc_corn.acoes.append(f"Pegou {esc_corn.arma}")
                esc_corn.sorte += 5

            if random.choice([True, False]):
                interacoes_tributo(esc_corn, lst_corn, cornucopia=True, matar=True)

        for esc_outros in lst_corn:
            if len(esc_outros.acoes) < 3:
                esc_outros.acoes.append("Pegou uma mochila e correu")

        narracao(f"{'#  ' * 10}{'INÍCIO DO JOGO | CORNUCÓPIA'}{'  #' * 10}\n")


class Dias:
    count_dias = 1

    def __init__(self, lst_trib):
        while len(regis_mortos) < 23:
            for esc_trib in random.sample(lst_trib, len(lst_trib)):
                # ações normais, saúde e emoções
                esc_trib.acoes.append(random.choice(acao_normal))
                esc_trib.acoes.append(random.choice(acao_saude))
                esc_trib.acoes.append(random.choice(acao_emocao))

                # comer
                if random.choice([True, False]):
                    esc_canibalismo = random.choice(regis_mortos)
                    esc_trib.acoes.append('Comeu ' + random.choice(tipos_comidas).format(esc_canibalismo.nome.upper(), f'{esc_canibalismo.distrito[:2]:2}'))
                    esc_trib.sorte += 3
                else:
                    esc_trib.sorte -= 5

                # paraquedas / cornucópia
                esc_arma = random.choice(tipos_armas)
                if random.choice([True, False]) and esc_trib.sorte >= (384/Dias.count_dias):
                    esc_paraquedas = random.choice(tipos_paraquedas)
                    if esc_paraquedas == '{}':
                        esc_trib.acoes.append('Recebeu ' + esc_arma)
                        esc_trib.arma = esc_arma
                    else:
                        esc_trib.acoes.append('Recebeu ' + esc_paraquedas)
                    esc_trib.sorte += 8
                else:
                    esc_cornucopia = random.choice(acao_cornucopia)
                    if esc_cornucopia == '{}':
                        esc_trib.acoes.append('Voltou à Cornucópia e pegou ' + esc_arma)
                        esc_trib.arma = esc_arma
                    else:
                        esc_trib.acoes.append(esc_cornucopia)

                # interação com outro tributo
                if len(regis_mortos) < 23:
                    interacoes_tributo(esc_trib, lst_trib[:], encontro=True)

                    if random.choice([True, False]) and esc_trib.sorte >= 65:
                        interacoes_tributo(esc_trib, lst_trib[:], matar=True)
                    else:
                        interacoes_tributo(esc_trib, lst_trib[:], cacar=True)

                # morrer / dormir
                if len(regis_mortos) < 23 and not esc_trib.morto:
                    if random.randint(0, 100) <= 25:
                        esc_trib.baixa = 'Morreu ' + random.choice(tipos_mortes)
                        regis_mortos.append(esc_trib)
                        esc_trib.morto = True

                    if random.choice([True, False]):
                        esc_trib.acoes.append(random.choice(acao_dormir))
                        esc_trib.sorte += 3
                    else:
                        esc_trib.acoes.append(random.choice(acao_naoDormir))
                        esc_trib.sorte -= 5

            input(f"{'enter para continuar':^120}\n")
            print()
            narracao(f"{'#  ' * 20}{f'DIA {Dias.count_dias:02}'}{'  #' * 20}\n")
            Dias.count_dias += 1

        regis_vencedor.append(lst_trib[0])

    def resumo_edicao(self):
        input(f"{'enter para continuar':^120}\n")
        print()
        impressor('=-' * 60)
        impressor('RESUMO DA EDIÇÃO')
        impressor('+' + '-' * 46 + '+')
        impressor(f"|{'ARENA':-^46}|")
        impressor(f"|{f' EDIÇÃO: {regis_edicao[0]}ª':<46}|")
        impressor(f"|{f' TEMA: {tipos_arenas[regis_edicao[1]]}':<46}|")
        impressor(f"|{'':46}|")

        impressor(f"|{'VENCEDOR':-^46}|")
        impressor(f"|{f' NOME: {regis_vencedor[0].nome} {regis_vencedor[0].sobrenome}':<46}|")
        impressor(f"|{f' DISTRITO: {regis_vencedor[0].distrito}':<46}|")
        impressor(f"|{f' MORTES:':<46}|")
        if len(regis_vencedor[0].vitimas) > 0:
            for vitima in regis_vencedor[0].vitimas:
                impressor(f"|{f'  - {vitima.nome} {vitima.sobrenome}':<23} {f'[DIST. {vitima.distrito[:2]:2}]':<22}|")
        else:
            impressor(f"|{f'   - Nenhuma':<46}|")

        impressor(f"|{'':46}|")
        impressor(f"|{' ORDEM DE BAIXAS':-^46}|")
        for ordem, tributo in enumerate(regis_mortos):
            impressor(f"|{f' {ordem + 1:>2}º - {tributo.nome} {tributo.sobrenome}':<30} {f'[DIST. {tributo.distrito[:2]:2}]':<15}|")
        impressor('+' + '-' * 46 + '+')


class Comecar:
    count_trib = 0

    def __init__(self):
        for t_d in range(1, 13):
            for t_s in [True, False]:
                trib_selecionados[Comecar.count_trib] = Tributo(t_s, t_d)
                Comecar.count_trib += 1

        Arena()
        Boas_Vindas()
        user_aposta = Aposta()
        Cornucopia()
        user_edicao = Dias(trib_selecionados)
        user_edicao.resumo_edicao()
        user_aposta.resultado()


try:
    Comecar()
except BaseException:
    print('Olá, patrocinador!')
    print('Sinto muito pelo inconveniênte, mas ocorreu algum erro no jogo.')
    print('Por favor, aguarde o código se corrigido ou entre em contato com o desenvolvedor, ele arrumará rapidinho.')
    print('Obrigado por desejar jogar no nosso simulador!')

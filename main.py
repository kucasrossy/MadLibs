from random import randint
import copy

word_dic = {
    'dia da semana': ["domingo", "segunda", "terça", "quarta", "quinta", "sexta", "sabado"],
    'sentimento': ["Feliz", "Triste", "Confuso", "Irritado"],
    'data especial': ["Aniversario", "Natal", "Velorio"],
    'verbo1': ["estudar", "atacar", "achar"],
    'verbo2': ["viver", "partir", "dividir"],
    'adjetivo diminutivo': ["pequeno", "minimo", "miudo"],
    'local': ["banheiro", "fortaleza", "casa"],
    'verbo3': ["viver", "morrer", "assistir"],
    'substantivo comum': ["pessoas", "homem", "animais"]
}

text = (
    "Hoje é {} e eu estou muito {}. Na verdade " +
    "Eu gostaria que fosse {} para que eu pudesse " +
    "{} e {}. Tenho um amigo famoso, o {} e nós sempre vamos ao {}. " +
    "Quando estamos lá, nós gostamos de {} no {}"
)


def get_word(type, local_dict):
    words = local_dict[type]
    count = len(words)-1
    index = randint(0, count)
    return local_dict[type].pop(index)


def create_story():
    local_dict = copy.deepcopy(word_dic)
    return text.format(
        get_word('dia da semana', local_dict),
        get_word('sentimento', local_dict),
        get_word('data especial', local_dict),
        get_word('verbo1', local_dict),
        get_word('verbo2', local_dict),
        get_word('adjetivo diminutivo', local_dict),
        get_word('local', local_dict),
        get_word('verbo3', local_dict),
        get_word('substantivo comum', local_dict)
    )


story = create_story()
print(story)
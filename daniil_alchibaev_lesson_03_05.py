from random import randint


def get_random_joke(nouns, adverbs, adjectives):
    """
    returns tuple of one random tuple, adverb and adjective
    returns None if any input is empty
    :param nouns: list of nouns
    :param adverbs: list of adverbs
    :param adjectives: list of adjectives
    :return: tuple (noun, adverb, adjective)
    """
    if not (nouns and adverbs and adjectives):
        return None
    random_noun = nouns[randint(0, len(nouns) - 1)]
    random_adverbs = adverbs[randint(0, len(adverbs) - 1)]
    random_adjectives = adjectives[randint(0, len(adjectives) - 1)]
    return random_noun, random_adverbs, random_adjectives


def get_jokes(n_jokes, do_not_repeat=False):
    """
    generates list of jokes like "noun adverb adjective"
    :param n_jokes: number of jokes to return
    :param do_not_repeat: optional; if True, uses every word only once
    :return: list of jokes
    """
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

    NOUN_INDEX = 0
    ADVERBS_INDEX = 1
    ADJECTIVES_INDEX = 2

    list_of_jokes = []  # будем собирать шутки сюда
    for _ in range(n_jokes):
        joke = get_random_joke(nouns, adverbs, adjectives)
        if do_not_repeat and joke:
            # если не хотим повторяющихся слов, то после создания шутки убираем их из списков
            nouns.remove(joke[NOUN_INDEX])
            adverbs.remove(joke[ADVERBS_INDEX])
            adjectives.remove(joke[ADJECTIVES_INDEX])
        if joke:
            # если get_random_joke вернул шутку, то добавляем ее в список
            list_of_jokes.append(joke)
    return list(map(" ".join, list_of_jokes))  # собираем каждый элемент шутки в требуемый формат


print(get_jokes(6))
print(get_jokes(30, do_not_repeat=True))

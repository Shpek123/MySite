import random, os, platform, time

class InvalidChoiceError(Exception):
    pass


class screen:
    @staticmethod
    def clear():
        os.system('cls' if platform.system() == 'Windows' else 'clear')

    @staticmethod
    def header(name):
        screen.clear()
        print('\n'+'='*30)
        print(name.center(30))
        print('='*30)

    @staticmethod
    def footer():
        print('='*30)

class menu:
    def __init__(self):
        self.menu_stress = menu_StressGame()
        self.endless_streak = 0
        self.time_streak = 0

    def menu(self):
        while True:
            screen.header('ТРЕНАЖЕРЫ ЕГЭ')
            print('1. Ударения')
            print('0. Выход')
            screen.footer()
            choice = input('> ')

            if choice == '1':
                self.menu_stress.menu_stress_game()
            elif choice == '0':
                return
            else:
                screen.clear()
                print('ОШИБКА: Введите число (0 - 2)')
                input('Нажмите Enter чтобы продолжить...')

class stat_game:
    def __init__(self):
        self.stress_game = StressGame()

    def menu_stat_game(self):
        while True:
            screen.header('СТАТИСТИКА')
            print(f'|Бесконечный режим: {endless_streak}')
            print(f'|На время (30c): {time_streak}')
            screen.footer()
            input("Нажмите Enter чтобы вернуться...")
            return
class menu_StressGame:
    def __init__(self):
        self.stress_game = StressGame()

    def menu_stress_game(self):
        while True:  # Добавляем цикл для возврата в это меню
            screen.header('РЕЖИМЫ УДАРЕНИЯ')
            print('1. Бесконечный режим')
            print('2. Работа над ошибками')
            print('3. На время')
            print('0. Назад')  # Изменяем на 0 для consistency
            screen.footer()
            choice = input('> ')

            if choice == '1':
                self.stress_game.endless_game()
            elif choice == '2':
                self.stress_game.error_work()
            elif choice == '3':
                self.stress_game.time_game()
            elif choice == '0':
                return  # Возврат в главное меню


class StressGame:
    def __init__(self):
        self.words = {
    'агронОмия': 'агрономИя',
    'акрОполь': 'акропОль',
    'алкогОль': 'алкОголь',
    'алфавИт': 'алфАвит',
    'Амфора': 'амфОра',
    'анАлог': 'аналОг',
    'анАтом': 'анатОм',
    'анонИм': 'анОним',
    'апокАлипсис': 'апокалИпсис',
    'арАхис': 'арахИс',
    'арЕст': 'Арест',
    'аргумЕнт': 'аргУмент',
    'ассиметрИя': 'ассимЕтрия',
    'астрОлог': 'астролОг',
    'астронОм': 'астрОном',
    'атмосфЕра': 'атмОсфера',
    'афЕра': 'Афера',
    'аэропОрты': 'аэропортЫ',
    'бАнты': 'бантЫ',
    'бОроду': 'бородУ',
    'бУнгало': 'бунгАло',
    'балОванный': 'бАлованный',
    'балУясь': 'бАлуясь',
    'баловАть': 'бАловать',
    'блАговест': 'благовЕст',
    'блуднИца': 'блУдница',
    'бралА': 'брАла',
    'бухгАлтеров': 'бухгалтерОв',
    'вЕчеря': 'вечЕря',
    'вОгнутый': 'вогнУтый',
    'валовОй': 'вАловой',
    'вандАлы': 'вАндалы',
    'вдовствО': 'вдОвство',
    'вернА': 'вЕрна',
    'вероисповЕдание': 'вероисповедАние',
    'ветеренАрия': 'ветеренарИя',
    'взАпуски': 'взапУски',
    'взялА': 'взЯла',
    'включЁн': 'вклЮчён',
    'включИм': 'вклЮчим',
    'включИт': 'вклЮчит',
    'влилАсь': 'влИлась',
    'водопровОд': 'водопрОвод',
    'воздухопровОд': 'воздухопрОвод',
    'ворвалАсь': 'ворвАлась',
    'воспринялА': 'воспрИняла',
    'воссоздалА': 'воссоздАла',
    'вручИт': 'врУчит',
    'втрИдорога': 'втридОрога',
    'вчистУю': 'вчИстую',
    'гЕнезис': 'генЕзис',
    'гЕрбовый': 'гербОвый',
    'газопровОд': 'газопрОвод',
    'гастронОмия': 'гастрономИя',
    'гегемОния': 'гегемонИя',
    'гналА': 'гнАла',
    'гомеопАтия': 'гомеопатИя',
    'граждАнство': 'грАжданство',
    'грошОвый': 'грОшовый',
    'дОверху': 'довЕрху',
    'дОгмат': 'догмАт',
    'дОнизу': 'донИзу',
    'дОсуха': 'досУха',
    'дОсыта': 'досЫта',
    'давнИшний': 'дАвнишний',
    'дефИс': 'дЕфис',
    'диалОг': 'диАлог',
    'диспансЕр': 'диспАнсер',
    'добелА': 'дОбела',
    'добралА': 'добрАла',
    'довезЕнный': 'довЕзенный',
    'договОр': 'дОговор',
    'договорЕнность': 'договОренность',
    'дождалАсь': 'дождАлась',
    'дозИровать': 'дозировАть',
    'дозвонИться': 'дозвОниться',
    'докраснА': 'дОкрасна',
    'докумЕнт': 'докУмент',
    'донЕльзя': 'дОнельзя',
    'досУг': 'дОсуг',
    'дремОта': 'дремотА',
    'духовнИк': 'духОвник',
    'евАнгелие': 'евангЕлие',
    'еретИк': 'ерЕтик',
    'жалюзИ': 'жАлюзи',
    'ждалА': 'ждАла',
    'жилОсь': 'жИлось',
    'зАгнутый': 'загнУтый',
    'зАгодя': 'загОдя',
    'зАнял': 'занЯл',
    'зАняло': 'занЯло',
    'зАсветло': 'засвЕтло',
    'зАтемно': 'затЕмно',
    'завИдно': 'зАвидно',
    'завсегдАтай': 'завсегдатАй',
    'задОлго': 'зАдолго',
    'закУпорив': 'закупОрив',
    'занялА': 'зАняла',
    'занятА': 'зАнята',
    'запертА': 'зАперта',
    'запломбировАть': 'запломбИровать',
    'заселЕн': 'засЕлен',
    'звалА': 'звАла',
    'звонИшь': 'звОнишь',
    'зимОвщик': 'зимовщИк',
    'злОба': 'злобА',
    'знАмение': 'знамЕние',
    'знАчимость': 'значИмость',
    'зубчАтый': 'зУбчатый',
    'Издавна': 'издАвна',
    'Иконопись': 'икОнопись',
    'Иксы': 'иксЫ',
    'Искоса': 'искОса',
    'Искра': 'искрА',
    'Исстари': 'исстАри',
    'игУмен': 'Игумен',
    'идеОлог': 'идеолОг',
    'изОгнуты': 'изогнУтый',
    'избалОван': 'избАлован',
    'избаловАть': 'избАловать',
    'издрЕвле': 'Издревле',
    'инсУльт': 'Инсульт',
    'исключИт': 'исклЮчит',
    'искривИться': 'искрИвитсья',
    'исчЕрпать': 'исчерпАть',
        }
        self.mistakes = []
        self.correct_list = list(self.words.keys())

    def endless_game(self):
        self.correct_list = list(self.words.keys())
        streak = 0
        while True:
            if not self.correct_list:
                print(f"\n ПОЗДРАВЛЯЮ! Слова закончились...")
                print(f"🔥 Ваш рекорд: {streak} правильных ответов подряд!")
                input("Нажмите Enter чтобы продолжить...")
                return

            screen.header('ТРЕНАЖЕР УДАРЕНИЙ')
            print(f"(серия: {streak} )".center(30))


            correct = random.choice(self.correct_list)
            incorrect = self.words[correct]
            self.correct_list.remove(correct)

            options = [correct, incorrect]
            random.shuffle(options)

            print('Что верно?')
            print(f'1. {options[0]}')
            print(f'2. {options[1]}')

            answer = 1 if options[0] == correct else 2

            try:
                user_choice = int(input('> '))
                if user_choice not in (1, 2):
                    raise InvalidChoiceError
            except ValueError:
                print('ОШИБКА: ВВЕДИТЕ 1 ИЛИ 2')
                continue
            except InvalidChoiceError:
                print('ОШИБКА: ВВЕДИТЕ 1 ИЛИ 2')
                continue

            if user_choice == answer:
                streak += 1
            else:
                self.mistakes.append([correct, incorrect])
                print(f"\n❌ Неверно! Правильно: {correct}")
                print(f"🔥 Ваш рекорд: {streak} правильных ответов подряд!")
                input("Нажмите Enter чтобы продолжить...")
                return

    def error_work(self):
        while True:
            cnt = len(self.mistakes)
            screen.header('РАБОТА НАД ОШИБКАМИ')
            print(f"(кол-во слов: {cnt} )".center(30))
            if not self.mistakes:
                print('\nУ вас нет ошибок!')
                input("Нажмите Enter чтобы продолжить...")
                return

            correct, incorrect = random.choice(self.mistakes)
            options = [correct, incorrect]
            random.shuffle(options)

            print('Что верно?')
            print(f'1. {options[0]}')
            print(f'2. {options[1]}')

            answer = 1 if options[0] == correct else 2

            try:
                user_choice = int(input('ВВОД: '))
                if user_choice not in (1, 2):
                    raise InvalidChoiceError
            except ValueError:
                print('ОШИБКА: ВВЕДИТЕ 1 ИЛИ 2')
                continue
            except InvalidChoiceError:
                print('ОШИБКА: ВВЕДИТЕ 1 ИЛИ 2')
                continue

            if user_choice == answer:
                self.mistakes.remove([correct,incorrect])
            else:
                print(f"\n❌ Неверно! Правильно: {correct}")
                input("Нажмите Enter чтобы продолжить...")
                return

    def time_game(self):
        screen.header('НА ВРЕМЯ')
        try:
            time_limit = int(input('Введите кол-во секунд: '))
        except ValueError:
            print('ВВЕДИТЕ ЧИСЛО!')
            input("Нажмите Enter чтобы продолжить...")
            return
        screen.footer()
        self.correct_list = list(self.words.keys())
        streak = 0
        lose = 0
        start_time = time.time()
        while True:
            elapsed = time.time() - start_time
            remaining = time_limit - elapsed
            if elapsed > time_limit:
                print(f"\n ВРЕМЯ ВЫШЛО!")
                print(f"🔥 Счет: {streak} правильных ответов, {lose} ошибок!")
                input("Нажмите Enter чтобы продолжить...")
                return
            if not self.correct_list:
                print(f"\n ПОЗДРАВЛЯЮ! Слова закончились...")
                print(f"🔥 Счет: {streak} правильных ответов, {lose} ошибок!")
                input("Нажмите Enter чтобы продолжить...")
                return

            screen.header(f'ОСТАЛОСЬ {int(remaining)} СЕКУНД')
            print(f"({streak} верно, {lose} ошибок)".center(30))

            correct = random.choice(self.correct_list)
            incorrect = self.words[correct]
            self.correct_list.remove(correct)

            options = [correct, incorrect]
            random.shuffle(options)

            print('Что верно?')
            print(f'1. {options[0]}')
            print(f'2. {options[1]}')

            answer = 1 if options[0] == correct else 2


            try:
                user_choice = int(input('> '))
                if user_choice not in (1, 2):
                    raise InvalidChoiceError
            except ValueError:
                print('ОШИБКА: ВВЕДИТЕ 1 ИЛИ 2')
                continue
            except InvalidChoiceError:
                print('ОШИБКА: ВВЕДИТЕ 1 ИЛИ 2')
                continue

            if user_choice == answer:
                streak += 1
            else:
                self.mistakes.append([correct, incorrect])
                lose += 1


if __name__ == '__main__':
    game = menu()
    game.menu()

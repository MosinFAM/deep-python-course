import unittest


from generator import gen


class TestPredict(unittest.TestCase):
    def test_gen(self):
        i_1 = 0
        lst_1 = ['Дремлет за горой мрачный замок мой\n']
        for line in gen('file.txt', ['дремлет', 'за', 'горой']):
            self.assertEqual(line, lst_1[i_1])
            i_1 += 1
        self.assertEqual(i_1, len(lst_1))

        i_2 = 0
        lst_2 = ['Я своих фантазий страждущий герой\n',
                 'Я часто вижу страх в смотрящих на меня глазах\n',
                 'Я их приводил в свой прекрасный дом\n',
                 'Я часто вижу страх в смотрящих на меня глазах\n',
                 'Я пытался их до смерти рассмешить\n',
                 'Я часто вижу страх в смотрящих на меня глазах\n']
        for line in gen('file.txt', ['я', 'Нло']):
            self.assertEqual(line, lst_2[i_2])
            i_2 += 1
        self.assertEqual(i_2, len(lst_2))

        i_3 = 0
        lst_3 = []
        for _ in gen('file.txt', ['углублённый', 'курс', 'питон']):
            i_3 += 1
        self.assertEqual(i_3, len(lst_3))

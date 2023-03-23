import unittest


from GEN import gen



class TestPredict(unittest.TestCase):
    def test_gen(self):
        for line in gen('file.txt', ['дремлет', 'за', 'горой']):
            self.assertEqual(line, 'Дремлет за горой мрачный замок мой\n')

        i = 0
        lst = ['Я своих фантазий страждущий герой\n',
               'Я часто вижу страх в смотрящих на меня глазах\n',
               'Я их приводил в свой прекрасный дом\n',
               'Я часто вижу страх в смотрящих на меня глазах\n',
               'Я пытался их до смерти рассмешить\n',
               'Я часто вижу страх в смотрящих на меня глазах\n']
        for line in gen('file.txt', ['я', 'Нло']):
            self.assertEqual(line, lst[i])
            i += 1

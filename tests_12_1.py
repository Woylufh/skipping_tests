from runner import Runner
import unittest


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_wolk(self):
        masha = Runner(name='Маша')
        for i in range(10):
            i = masha.walk()
        self.assertEqual(i, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        kolya = Runner(name='Коля')
        for i in range(10):
            i = kolya.run()
        self.assertEqual(i, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        kolya = Runner(name='Коля')
        masha = Runner(name='Маша')
        for i in range(10):
            i = kolya.walk() and kolya.run()
        self.assertNotEqual(i, 100)
        for i in range(10):
            i = masha.walk() and masha.run()
        self.assertNotEqual(i, 50)


if __name__ == '__main__':
    unittest.main()

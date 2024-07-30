from tournament import Runner
from tournament import Tournament
import unittest


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls, *a):
        cls.all_results = a
        cls.tearDownClass(cls.all_results)

    def setUp(self):  # создать бегунов
        self.usain = Runner('Усэйн', 10)
        self.andrey = Runner('Андрей', 9)
        self.nik = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls, *a):  # метод, где выводятся all_results по очереди в столбец.
        cls.all_results = a
        for i in cls.all_results:
            for c in i:
                print(c)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_first_tournament(self):
        tournament = Tournament(90, self.usain, self.nik)
        results = tournament.start()
        self.assertTrue(results[2] == self.nik)
        self.setUpClass(results)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_second_tournament(self):
        tournament = Tournament(90, self.andrey, self.nik)
        results = tournament.start()
        self.assertTrue(results[2] == self.nik)
        self.setUpClass(results)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_third_tournament(self):
        tournament = Tournament(90, self.usain, self.andrey, self.nik)
        results = tournament.start()
        self.assertTrue(results[3] == self.nik)
        self.setUpClass(results)


if __name__ == '__main__':
    unittest.main()
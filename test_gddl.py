import unittest
import pandas as pd
from gddl_analisis import *

class TestGDDL(unittest.TestCase):

    def setUp(self):
        self.df_test = pd.DataFrame({
            'ID': [1,2,3],
            'Level Name': ['Level1', 'SongA', 'Level3'],
            'Song': ['SongA', 'SongA', 'SongB'],
            'Tier': [5, 5, 7],
            'Enjoyment': [8, 5, 9],
            'Creator': ['A', 'A', 'B']
        })

    def test_filtrar_expertos(self):
        r = filtrar_expertos(self.df_test, 7, 'SongA')
        self.assertEqual(len(r), 1)

    def test_niveles_homonimos(self):
        r = niveles_homonimos(self.df_test)
        self.assertIn('SongA', r)

    def test_correlacion(self):
        r = correlacion_dificultad_disfrute(self.df_test)
        self.assertIsInstance(r, float)

    def test_media_dificultad(self):
        r = media_disfrute_por_dificultad(self.df_test)
        self.assertTrue(5 in r.index)

    def test_top_canciones(self):
        r = top_canciones_por_disfrute(self.df_test, 1)
        self.assertEqual(len(r), 1)

    def test_global_stats(self):
        r = estadisticas_globales(self.df_test)
        self.assertIn('media', r)

if __name__ == '__main__':
    unittest.main()
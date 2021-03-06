import unittest
from pyspark.sql import SparkSession
from src.jobs.to_trusted import ToTrusted
class ToTrustedTest(unittest.TestCase):

    def test_processo(self):

        spark = SparkSession.builder.getOrCreate()

        fr_path_al = '../tdd/tests/locallake/raw/alunos.csv'
        fr_path_disc = '../tdd/tests/locallake/raw/alunos_diciplina.csv'
        to_path = '../tdd/tests/locallake/trusted/alunos_salvos.csv'
        chamada = ToTrusted(fr_path_al,fr_path_disc,to_path)
        resultado = chamada.processa()

        df = spark.read.format('delta').load(to_path)
        df.show(2)

        values = df.orderBy(['aluno']).collect()

        print(values[0]['Media'], values[1]['Media'])
        self.assertEqual(8.75, values[0]['Media'])
        self.assertEqual(7.5, values[1]['Media'])
        print('passou no teste')
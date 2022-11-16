import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_negatiivisen_tilavuuden_syotto(self):
        varasto = Varasto(-4)

        self.assertEqual(varasto.tilavuus, 0)

    def test_negatiivisen_varasto_lisayksen_syotto(self):
        self.varasto.lisaa_varastoon(-5)

        self.assertEqual(self.varasto.saldo, 0)

    def test_lisaa_varastoon_niin_etta_kaikki_mahtuu(self):
        varasto = Varasto(10)
        varasto.lisaa_varastoon(10)

        self.assertEqual(varasto.saldo, 10)

    def test_lisaa_varastoon_liikaa(self):
        varasto = Varasto(10)
        varasto.lisaa_varastoon(15)

        self.assertEqual(varasto.saldo, 10)

    def test_ota_varastosta_negatiivinen(self):
        self.varasto.ota_varastosta(-1)

        self.assertEqual(self.varasto.saldo, 0)

    def test_ota_varastosta_enemman_kuin_on_saldoa(self):
        varasto = Varasto(10)
        varasto.ota_varastosta(11)

        self.assertEqual(varasto.saldo, 0)

    def test_str(self):
        varasto = Varasto(100)
        self.assertEqual(varasto.__str__(
        ), f"saldo = {varasto.saldo}, vielä tilaa {varasto.paljonko_mahtuu()}")
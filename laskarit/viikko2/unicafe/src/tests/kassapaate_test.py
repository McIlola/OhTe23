import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti


class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate=Kassapaate()
    def test_luotu_kassapaate_toimii(self):
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), "100000")
        self.assertEqual(str(self.kassapaate.edulliset), "0")
        self.assertEqual(str(self.kassapaate.maukkaat), "0")
    
    def test_kateisosto_maukas1(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(500), 100)
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), "100400")
        self.assertEqual(str(self.kassapaate.maukkaat), "1")
            
    def test_kateisosto_maukas2(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(300), 300)
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), "100000")
        self.assertEqual(str(self.kassapaate.maukkaat), "0")

    def test_kateisosto_edullinen1(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(500), 260)
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), "100240")
        self.assertEqual(str(self.kassapaate.edulliset), "1")
            
    def test_kateisosto_edullinen2(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(200), 200)
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), "100000")
        self.assertEqual(str(self.kassapaate.edulliset), "0")

    def test_kortti_maukas1(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(Maksukortti(500)), True)
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), "100000")
        self.assertEqual(str(self.kassapaate.maukkaat), "1")
            
    def test_kortti_maukas2(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(Maksukortti(300)), False)
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), "100000")
        self.assertEqual(str(self.kassapaate.maukkaat), "0")
    
    def test_kortti_edullinen1(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(Maksukortti(500)), True)
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), "100000")
        self.assertEqual(str(self.kassapaate.edulliset), "1")
            
    def test_kortti_edullinen2(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(Maksukortti(200)), False)
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), "100000")
        self.assertEqual(str(self.kassapaate.edulliset), "0")
    
    def test_korttilataus_toimii(self):
        kortti=Maksukortti(500)
        self.kassapaate.lataa_rahaa_kortille(kortti,200)
        self.assertEqual(kortti.saldo, 700)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100200)
        self.kassapaate.lataa_rahaa_kortille(kortti,-200)
        self.assertEqual(kortti.saldo, 700)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100200)
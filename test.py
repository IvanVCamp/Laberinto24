import unittest
from laberinto import Juego

class pruebaJuego(unittest.TestCase):
    
    def test_createRoom_returns_different_rooms(self):
            juego = Juego()
            sala1 = juego.CrearHabitacion(1)
            sala2 = juego.CrearHabitacion(2)

            self.assertNotEqual(sala1, sala2)

    def test_createRoom_returns_room_with_correct_id(self):
        juego = Juego()
        hab = juego.CrearHabitacion(5)
        self.assertEqual(hab.id, 5)
        
    def test_hab_con_paredes(self):
            juego = Juego()
            hab = juego.CrearHabitacion(1)

            self.assertIsNotNone(hab.norte)
            self.assertIsNotNone(hab.sur)
            self.assertIsNotNone(hab.este)
            self.assertIsNotNone(hab.oeste)


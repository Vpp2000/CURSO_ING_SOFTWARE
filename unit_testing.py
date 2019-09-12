import numpy as np
import unittest

# EJECUTAR python3 unit_Test_coord.py -v
# PARA QUE LOS RESULTADOS SEAN ADECUADOS ES NECESARIO LIMITAR EL NUMERO DE DECIMALES DEL PROGRAMA


class XYPolar:

	@classmethod
	def cart_to_pol(cls,x,y):

		rho = round(np.sqrt((x)**2 + (y)**2),2)
		phi = round(np.arctan2(y, x),2)
		return (rho, phi)

	@classmethod
	def pol_to_cart(cls,rho,phi):
		x = round(rho * np.cos(phi),2)
		y = round(rho * np.sin(phi),2)
		return (x, y)



class TestUM(unittest.TestCase):

	def setUp(self):
		pass

	def test_cart_to_polar(self):
		self.assertEqual(XYPolar.cart_to_pol(1.0,np.sqrt(3.0)), (2.0,round(np.pi/(3.0),2)))

	def test_polar_to_cart(self):
		self.assertEqual(XYPolar.pol_to_cart(2.0,np.pi/(3.0)), (1.0,round(np.sqrt(3.0),2)))
        
        
if __name__ == '__main__':
	unittest.main()       

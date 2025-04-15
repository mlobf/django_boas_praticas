from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from main.models import City


class CityPostAPITestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_city(self):
        # Dados para criar uma nova cidade
        data = {'city_name': 'Rio de Janeiro', 'short_name': 'RJ'}

        # Faz uma requisição POST para criar uma nova cidade
        response = self.client.post('/api/cities/', data, format='json')

        # Verifica se a resposta foi 201 CREATED
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Verifica se a cidade foi criada corretamente
        self.assertEqual(response.data['city_name'], 'Rio de Janeiro')
        self.assertEqual(response.data['short_name'], 'RJ')


class CityGetAPITestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        City.objects.create(city_name='Piracicaba', short_name='PIRA')
        City.objects.create(city_name='São Paulo', short_name='SP')

    def test_get_cities(self):
        # Faz uma requisição GET para o endpoint /api/cities/
        response = self.client.get('/api/cities/')

        # Verifica se o status da resposta é 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Verifica se as cidades são retornadas corretamente
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['city_name'], 'Piracicaba')
        self.assertEqual(response.data[1]['city_name'], 'São Paulo')


class CityDeleteAPITestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.city = City.objects.create(city_name='Campinas', short_name='CPS')

    def test_delete_city(self):
        # Realiza uma requisição DELETE no endpoint da cidade criada
        url = f'/api/cities/{self.city.id}/'
        response = self.client.delete(url)

        # Verifica se o status é 204 NO CONTENT (deletado com sucesso)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Verifica se a cidade foi realmente removida do banco de dados
        self.assertFalse(City.objects.filter(id=self.city.id).exists())

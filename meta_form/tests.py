from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse

from meta_form.models import ResearchMetadata


class GetPagesTestCase(TestCase):
    fixtures = ['meta_form_data_format.json', 'meta_form_degree_of_aggregation.json', 'meta_form_research_meta_data.json']

    def test_get_form_page(self):
        path = reverse('meta_form:index')
        response = self.client.get(path)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'index.html')

    def test_get_data_for_form_page(self):
        path = reverse('meta_form:index')
        response = self.client.get(path)
        research = ResearchMetadata.objects.all().select_related('data_format', 'degree_of_aggregation')
        self.assertQuerysetEqual(response.context['research'], research)

    def test_download_meta_data(self):
        path = reverse('meta_form:download_metadata', args=[1])
        response = self.client.get(path)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.headers['Content-Type'], 'application/zip')


class SendFormTestCase(TestCase):
    fixtures = ['meta_form_data_format.json', 'meta_form_degree_of_aggregation.json', 'meta_form_research_meta_data.json']

    def test_meta_data_form_send(self):
        path = reverse('meta_form:index')
        data = {
            'data_provider': 'TestProvider',
            'data_format': 1,
            'degree_of_aggregation': 1,
        }
        response = self.client.post(path, data=data)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, reverse('meta_form:index'))
        self.assertTrue(ResearchMetadata.objects.filter(data_provider=data['data_provider']).exists())

    def test_meta_data_form_send_error(self):
        path = reverse('meta_form:index')
        data = {
            'data_provider': '',
            'data_format': -1,
            'degree_of_aggregation': -1,
        }
        response = self.client.post(path, data=data)
        errors = response.context['form'].errors
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertIn('This field is required.', errors['data_provider'])
        self.assertIn('Select a valid choice. That choice is not one of the available choices.', errors['data_format'])
        self.assertIn('Select a valid choice. That choice is not one of the available choices.', errors['degree_of_aggregation'])

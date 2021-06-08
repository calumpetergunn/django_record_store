from django.test import TestCase
from inventory.models import *

# Create your tests here.

class AlbumTestCase(TestCase):

    def setUp(self):
        self.artist1 = Artist.objects.create(name = "FKA Twigs")
        self.album1 = Album.objects.create(
            title = "EP2", 
            year = 2012, 
            stock_level = 10,
            artist = self.artist1
            )

    def test_artist_saved(self):
        self.assertGreater(self.artist1.pk, 0)

    def test_album_saved(self):
        self.assertGreater(self.album1.pk, 0)

    def test_album_fk(self):
        self.assertEqual(self.album1.artist.pk, self.artist1.pk)

    def test_fka_twigs_still_active(self):
        self.assertTrue(self.artist1.still_active)
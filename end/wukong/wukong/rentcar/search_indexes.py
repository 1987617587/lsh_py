from haystack import indexes
from .models import Car, Category, City


class CarIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return Car

    def index_queryset(self, using=None):
        return self.get_model().objects.all()


class CityIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return City

    def index_queryset(self, using=None):
        return self.get_model().objects.all()


class CategoryIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return Category

    def index_queryset(self, using=None):
        return self.get_model().objects.all()

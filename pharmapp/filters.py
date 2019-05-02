 class medicineFilter(django_filters.filterSet):
      class meta:
        model= Medicine
        fields = ('name','area','insurance'))

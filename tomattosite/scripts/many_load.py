import csv  # https://docs.python.org/3/library/csv.html

# https://django-extensions.readthedocs.io/en/latest/runscript.html

# python3 manage.py runscript many_load

from unesco.models import Category, States, Region, Iso, Site

def run():
    fhand = open('unesco/whc-sites-2018-clean.csv')
    reader = csv.reader(fhand)
    csv_columns = next(reader) # [name,description,justification,year,longitude,latitude, area_hectares,category,states,region,iso]

    # Clean past data
    Site.objects.all().delete()
    Category.objects.all().delete()
    States.objects.all().delete()
    Region.objects.all().delete()
    Iso.objects.all().delete()

    for row in reader:
        # print(row)
        c, created_c = Category.objects.get_or_create(name=row[csv_columns.index('category')])
        s, created_s = States.objects.get_or_create(name=row[csv_columns.index('states')])
        r, created_r = Region.objects.get_or_create(name=row[csv_columns.index('region')])
        i, created_i = Iso.objects.get_or_create(name=row[csv_columns.index('iso')])

        try:
            year = int(row[csv_columns.index('year')])
        except:
            year = None
        try:
            longitude = float(row[csv_columns.index('longitude')])
        except:
            longitude = None
        try:
            latitude = float(row[csv_columns.index('latitude')])
        except:
            latitude = None
        try:
            area_hectares = float(row[csv_columns.index('area_hectares')])
        except:
            area_hectares = None

        m = Site(
            name=row[csv_columns.index('name')] or None,
            description=row[csv_columns.index('description')] or None,
            justification=row[csv_columns.index('justification')] or None,
            year=year,
            longitude=longitude,
            latitude=latitude,
            area_hectares=area_hectares,
            category=c,
            state=s,
            region=r,
            iso=i
        )
        m.save()

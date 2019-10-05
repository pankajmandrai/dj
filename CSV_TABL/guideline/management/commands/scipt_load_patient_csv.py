import csv
import datetime
import os

from book_show.settings import BASE_DIR
from guideline.models import Patientdata, Patientguidelines, Recommendations

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, **options):
        file_path = os.path.join(BASE_DIR,'guideline\Patient_data.csv')
        with open(file_path) as f:
            reader = csv.reader(f)
            for i, row in enumerate(reader):
                if ( i != 0):
                    gender = 'f' if (row[2] == 'Female') else 'm'
                    date = datetime.datetime.strptime(row[0], '%d-%b-%y')

                    _, created = Patientdata.objects.get_or_create(
                        date=date,
                        name=row[1],
                        gender=gender,
                        systolic_BP=row[3],
                        diastolic_BP=row[4],
                        smoking_years=row[5],
                        no_of_packs=row[6],
                        fasting_blood_sugar=row[3],
                        hypothyroid=bool(row[8]),
                        obese=bool(row[9]),
                        intravenous_drug_abuse=bool(row[10])
                    )

        f.close()


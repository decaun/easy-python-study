import json
from schematics.transforms import blacklist
from schematics.types import StringType, DateTimeType
import datetime
from schematics.models import Model
from schematics.types import StringType, DecimalType, DateTimeType


class WeatherReport(Model):
    city = StringType()
    temperature = DecimalType()
    taken_at = DateTimeType(default=datetime.datetime.now)

# WeatherReport.get_mock_object().to_primitive()


class Movie(Model):
    name = StringType()
    director = StringType()
    release_date = DateTimeType
    personal_thoughts = StringType()

    class Options:
        roles = {'public': blacklist('personal_thoughts')}


trainspotting = Movie()
trainspotting.name = u'Trainspotting'
trainspotting.director = u'Danny Boyle'
trainspotting.release_date = datetime.datetime(1996, 7, 19, 0, 0)
trainspotting.personal_thoughts = 'This movie was great!'
trainspotting.to_native()
trainspotting.to_primitive()
json.dumps(trainspotting.to_primitive())

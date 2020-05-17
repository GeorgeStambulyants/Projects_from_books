from unittest.mock import patch
from mailinglist.models import Subscriber
import factory




class SubscriberFactory(factory.DjangoModelFactory):
    email = factory.Sequence(lambda n: f'foo.{n}@example.com')

    class Meta:
        model = Subscriber
    
    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        with \
        patch('mailinglist.models.tasks.send_confirmation_email_to_subscriber'):
            return super()._create(
                model_class=model_class,
                *args, **kwargs,
            )
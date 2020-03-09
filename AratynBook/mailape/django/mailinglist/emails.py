from django.conf import settings
from django.template import Context, engines
from django.shortcuts import reverse
from django.core.mail import send_mail
from datetime import datetime
from django.utils.datetime_safe import datetime


CONFIRM_SUBSCRIPTION_HTML = 'mailinglist/email/confirmation.html'
CONFIRM_SUBSCRIPTION_TXT = 'mailinglist/email/confirmation.txt'
SUBSCRIBER_MESSAGE_HTML = 'mailing/email/subscriber_message.html'
SUBSCRIBER_MESSAGE_TXT = 'mailing/email/subscriber_message.txt'


class EmailTemplateContext(Context):

    @staticmethod
    def make_link(path):
        return settings.MAILING_LIST_LINK_DOMAIN + path
    
    def __init__(self, subscriber, dict_=None, **kwargs):
        if dict_ is None:
            dict_ = {}
        email_ctx = self.common_context(subscriber)
        email_ctx.update(dict_)
        super().__init__(email_ctx, **kwargs)
    SUBSCRIBER_MESSAGE_TXT = 'mailing/email/subscriber_message.txt'
    def common_context(self, subscriber):
        subscriber_pk_kwargs = {'pk': subscriber.id}
        unsubscribe_path = reverse(
            'mailinglist:unsubscribe',
            kwargs=subscriber_pk_kwargs,
        )
        return {
            'subscriber': subscriber,
            'mailing_list': subscriber.mailing_list,
            'unsubscribe_link': self.make_link(unsubscribe_path)
        }


def send_confirmation_email(subscriber):
    mailing_list = subscriber.mailing_list
    confirmation_link = EmailTemplateContext.make_link(
        reverse(
            'mailinglist:confirm_subscribtion',
            kwargs={'pk': subscriber.id}
        )
    )
    context = EmailTemplateContext(
        subscriber,
        {'confirmation_link': confirmation_link}
    )
    subject = f'Confirming subscription to {mailing_list.name}'

    dt_engine = engines['django'].engine
    text_body_template = dt_engine.get_template(CONFIRM_SUBSCRIPTION_TXT)
    text_body = text_body_template.render(context=context)
    html_body_template = dt_engine.get_template(CONFIRM_SUBSCRIPTION_HTML)
    html_body = html_body_template.render(context=context)

    send_mail(
        subject=subject,
        message=text_body,
        from_email=settings.MAILING_LIST_FROM_EMAIL,
        recipient_list=(subscriber.email,),
        html_message=html_body,
    )


def send_subscriber_message(subscriber_message):
    message = subscriber_message.message
    context = EmailTemplateContext(subscriber_message.subscriber, {
        'body': message.body,
    })

    dt_engine = engines['django'].engine
    text_body_template = dt_engine.get_template(SUBSCRIBER_MESSAGE_TXT)
    text_body = text_body_template.render(context=context)
    html_body_tempalte = dt_engine.get_template(SUBSCRIBER_MESSAGE_HTML)
    html_body = html_body_tempalte.render(context=context)

    utcnow = datetime.utcnow()

    subscriber_message.last_attempt = utcnow
    subscriber_message.save()

    success = send_mail(
        subject=message.subject,
        message=text_body,
        from_email=settings.MAILING_LIST_FROM_EMAIL,
        recipient_list=(subscriber_message.subscriber.email,),
        html_message=html_body,
    )

    if success == 1:
        subscriber_message.sent = utcnow
        subscriber_message.save()

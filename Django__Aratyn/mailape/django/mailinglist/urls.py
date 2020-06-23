from django.urls import path

from . import views


app_name = 'mailinglist'

urlpatterns = [
    path(
        '',
        views.MailingListListView.as_view(),
        name='mailinglists',
    ),
    path(
        'new',
        views.CreateMailingListView.as_view(),
        name='create_mailinglist',
    ),
    path(
        '<uuid:pk>/delete',
        views.DeleteMailingListView.as_view(),
        name='delete_mailinglist',
    ),
    path(
        '<uuid:pk>/manage/',
        views.MailingListDetailView.as_view(),
        name='manage_mailinglist',
    ),
    path(
        '<uuid:mailinglist_pk>/subscribe',
        views.SubscribeToMailingListView.as_view(),
        name='subscribe',
    ),
    path(
        '<uuid:pk>/thankyou/',
        views.ThankYouForSubscribingView.as_view(),
        name='subscriber_thankyou',
    ),
    path(
        'subscribe/confirmation/<uuid:pk>',
        views.ConfirmSubscriptionView.as_view(),
        name='confirm_subscription',
    ),
    path(
        'unsubscribe/<uuid:pk>',
        views.UnsubscribeView.as_view(),
        name='unsubscribe',
    ),
    path(
        '<uuid:mailinglist_pk>/message/new',
        views.CreateMessageView.as_view(),
        name='create_message',
    ),
    path(
        'message/<uuid:pk>/',
        views.MessageDetailView.as_view(),
        name='view_message',
    ),
    path(
        'api/v1/mailing-list',
        views.MailingListCreateListView.as_view(),
        name='api-mailing-list-list'
    ),
    path(
        'api/v1/mailinglist/<uuid:pk>',
        views.MailingListRetrievUpdateDestroyView.as_view(),
        name='api-mailing-list-detail',
    ),
    path(
        'api/v1/mailinglist/<uuid:mailing_list_pk>/subscribers',
        views.SubscriberListCreateView.as_view(),
        name='api-subscriber-list'
    ),
    path(
        'api/v1/subscriber/<uuid:pk>',
        views.SubscriberRetrievUpdateDestroyView.as_view(),
        name='api-subscriber-detail',
    ),
]

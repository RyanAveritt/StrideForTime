from django.urls import path
from .views import (
    my_profile_view, 
    invites_received_view, 
    sent_invites_view, 
    ProfileDetailView,
    ProfileListView,
    SearchView,
    send_invatation,
    remove_from_friends,
    accept_invatation,
    reject_invatation,
    )

app_name = 'profiles'

urlpatterns = [
    path("search/", SearchView.as_view(), name="search-view"),
    path('', ProfileListView.as_view(), name='all-friends-view'),
    path('myprofile/', my_profile_view, name='my-profile-view'),
    path('my-invites/', invites_received_view, name='my-invites-view'),
    path('invited/', sent_invites_view, name='invited-profiles-view'),
    path('send-invite/', send_invatation, name='send-invite'),
    path('remove-friend/', remove_from_friends, name='remove-friend'),
    path('remove-friend/', remove_from_friends, name='remove-friend'),
    path('<slug>/', ProfileDetailView.as_view(), name='profile-detail-view'),
    path('my-invites/accept/', accept_invatation, name='accept-invite'),
    path('my-invites/reject/', reject_invatation, name='reject-invite'),
]
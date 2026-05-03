# from django.urls import path
# from . import views

# urlpatterns = [
#     path('snippets/', views.snippet_list),
#     path('snippets/<int:pk>/', views.snippet_detail)

# ]


"""Refactoring as per the implemented class type View"""

from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    path("", views.api_root, name="api-root"),
    path("snippets/", views.SnippetList.as_view(), name="snippet-list"),
    path("snippets/<int:pk>/", views.SnippetDetail.as_view(), name="snippet-detail"),
    path("users/", views.UserList.as_view(), name="user-list"),
    path("users/<int:pk>/", views.UserDetail.as_view(), name="user-detail"),
    path(
        "snippets/<int:pk>/highlight/",
        views.SnippetHighlight.as_view(),
        name="snippet-highlight",
    ),
    path("api-auth/", include("rest_framework.urls")),
]

urlpatterns = format_suffix_patterns(urlpatterns)

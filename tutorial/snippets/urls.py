# from django.urls import path
# from . import views

# urlpatterns = [
#     path('snippets/', views.snippet_list),
#     path('snippets/<int:pk>/', views.snippet_detail)

# ]


"""Refactoring as per the implemented class type View"""
"""
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    path("snippets/", views.SnippetList.as_view()),
    path("snippets/<int:pk>", views.SnippetDetail.as_view()),
    path("api-auth/", include("rest_framework.urls")),
    path("", views.api_root),
    path("snippets/<int:pk>/highlight/", views.SnippetHighlight.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
 """

from rest_framework import renderers
from .views import api_root, SnippetViewSet, UserViewSet
from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path

snippet_list = SnippetViewSet.as_view({"get": "list", "post": "create"})
snippet_detail = SnippetViewSet.as_view({"get":"retrieve",
                                         "put":"update",
                                         "patch": "partial_update",
                                         "delete":"destroy"})
snippet_highlight = SnippetViewSet.as_view(
    {"get":"highlight"},
    renderer_classes=[renderers.StaticHTMLRenderer]
)
user_list = UserViewSet.as_view({"get":"list"})
user_detail = UserViewSet.as_view({"get":"retrieve"})


urlpatterns = format_suffix_patterns([

    path("", api_root),
    path("snippets/", snippet_list, name="snippet-list"),
    path("snippets/<int:pk>", snippet_detail, name= "snippet-detail"),
    path(
        "snippets/<int:pk>/highlight/", snippet_highlight, name="snippet-highlight"
    ),
    path("users/", user_list, name= "user-list"),
    path("user/<int:pk>", user_detail, name= "user-detail"),
])

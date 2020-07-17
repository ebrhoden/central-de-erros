from django.urls import path

from .views import (
    listLog,
    detailLog,
    updateLog,
    deleteLog,
    createLog,
    ApiLogListView,
)

app_name = 'logs'

urlpatterns = [
    path('', ApiLogListView.as_view(), name='log-list-all'),
    path('log-list', listLog, name='log-list'),
    path('<str:pk>/log-detail', detailLog, name='log-detail'),
    path('<str:pk>/log-update', updateLog, name='log-update'),
    path('<str:pk>/log-delete', deleteLog, name='log-delete'),
    path('log-create', createLog, name='log-create'),
]
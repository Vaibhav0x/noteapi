from django.urls import path
from .views import CreateNoteView, RetrieveNoteView, QueryNotesView, UpdateNoteView

urlpatterns = [
    path('notes/', CreateNoteView.as_view(), name='create-note'),
    path('notes/<int:pk>/', RetrieveNoteView.as_view(), name='retrieve-note'),
    path('notes/query/', QueryNotesView.as_view(), name='query-notes'),
    path('notes/<int:pk>/update/', UpdateNoteView.as_view(), name='update-note'),
]

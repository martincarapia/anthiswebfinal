"""Defines URL patterns for myfinalweb."""
from django.urls import path
from . import views
app_name = 'myfinalweb'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),

    # Page that shows all topics.
    #path('topics/', views.topics, name='topics'),
    # Detail page for a single topic.
    #path('topics/<int:topic_id>/', views.topic, name='topic'),
    # Page for adding a new topic.
    #path('new_topic/', views.new_topic, name='new_topic'),

    # Page for the blog and viewing all entries
    path('blog/', views.show_entries, name='show_entries'),
    # Page for adding a new entry.
    path('new_entry/', views.new_entry, name='new_entry'),
    # Page for editing an entry.
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
    path('about/', views.about, name='about'),
]
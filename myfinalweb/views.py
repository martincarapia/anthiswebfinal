from django.shortcuts import redirect, render
from .models import Entry
from .forms import EntryForm
from django.contrib.auth.decorators import login_required
from django.http import Http404

# Create your views here.
def index(request):
    """The home page for Learning Log."""
    return render(request, 'myfinalweb/index.html')

'''
@login_required
def topics(request):
    """Show all topics."""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}
    return render(request, 'myfinalweb/topics.html', context)

@login_required
def topic(request, topic_id):
    """Show a single topic and all its entries."""
    topic = Topic.objects.get(id=topic_id)
    # Make sure the topic belongs to the current user.
    if topic.owner != request.user:
        raise Http404
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'myfinalweb/topic.html', context)

@login_required
def new_topic(request):
    """Add a new topic."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = TopicForm()
    else:
        # POST data submitted; process data.
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect('myfinalweb:topics')
    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'myfinalweb/new_topic.html', context)
'''

def show_entries(request):
    """Show all entries."""
    entries = Entry.objects.order_by('-date_added')
    context = {'entries': entries}
    return render(request, 'myfinalweb/blog.html', context)

@login_required
def new_entry(request):
    """Add a new entry for a particular topic."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = EntryForm()
    else:
        # POST data submitted; process data.
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.owner = request.user
            new_entry.save()
            return redirect('myfinalweb:show_entries')
    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'myfinalweb/new_entry.html', context)

@login_required
# def edit_entry(request, entry_id, user_id):
def edit_entry(request, entry_id):
    """Edit an existing entry."""

    entry = Entry.objects.get(id=entry_id)

    # Make sure the topic belongs to the current user.
    if entry.owner != request.user:
        raise Http404
    #if entry.entry_user_id != user_id:
    #    return redirect('accounts:login')
    if request.method != 'POST':
        # Initial request; pre-fill form with the current entry.
        form = EntryForm(instance=entry)
    else:
        # POST data submitted; process data.
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('myfinalweb:show_entries')
    
    context = {'entry': entry, 'form': form}
    return render(request, 'myfinalweb/edit_entry.html', context)

def about(request):
    return render(request, 'myfinalweb/about.html')
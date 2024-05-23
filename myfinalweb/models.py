from django.db import models
from django.contrib.auth.models import User

class Entry(models.Model):
    """Something specific learned about a topic."""
    # topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    # entry_user_id = User.get_username
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = 'entries'
    def __str__(self):
        """Return a simple string representing the entry."""
        if len(list(self.text)) >= 50:

            return f"{self.text[:50]}..."
        
        return self.text
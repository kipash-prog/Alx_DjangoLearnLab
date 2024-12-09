from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from bookshelf.models import Book  # Replace with the appropriate model
from django.db.models import Q

def create_groups_and_permissions(sender, **kwargs):
    # Example: If you're creating a permission for the 'Book' model
    content_type = ContentType.objects.get_for_model(Book)
    
    # Define permissions
    permissions = [
        ('can_create', 'Can create books'),
        ('can_edit', 'Can edit books'),
        ('can_delete', 'Can delete books'),
    ]
    
    for codename, name in permissions:
        permission, created = Permission.objects.get_or_create(
            codename=codename,
            name=name,
            content_type=content_type  # Ensure content type is set
        )
        if created:
            print(f"Permission created: {name}")

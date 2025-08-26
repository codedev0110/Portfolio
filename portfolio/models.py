from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    technologies = models.CharField(max_length=300)
    github_url = models.URLField()
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    detail_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    featured = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
    @property
    def tech_list(self):
        return [tech.strip() for tech in self.technologies.split(',') if tech.strip()]

class Experience(models.Model):
    EXPERIENCE_TYPES = (
        ('work', 'Work Experience'),
        ('education', 'Education'),
    )
    
    type = models.CharField(max_length=10, choices=EXPERIENCE_TYPES)
    title = models.CharField(max_length=200)
    organization = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField()
    current = models.BooleanField(default=False)

    class Meta:
        ordering = ['-start_date']

    def __str__(self):
        return f"{self.title} at {self.organization}"

class Profile(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    bio = models.TextField()
    cv_url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    twitter_url = models.URLField(blank=True)
    email = models.EmailField()

    def __str__(self):
        return self.name
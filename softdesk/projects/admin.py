from django.contrib import admin


from django.contrib import admin

from softdesk.projects.models import (Project,
                                      Contributor,
                                      Issue, Comment)


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description',
                    'type', 'author',
                    'created_time']


class ContributorAdmin(admin.ModelAdmin):
    list_display = ['user', 'project_name',
                    'created_time']

    @admin.display(description='Project')
    def project_name(self, obj):
        return obj.project.name


class IssueAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description',
                    'project_name', 'assigned_to',
                    'priority', 'tag', 'status',
                    'author', 'created_time']

    @admin.display(description='Project')
    def project_name(self, obj):
        return obj.project.name

    # @admin.display(description='Assigned To')
    # def assigned_to_name(self, obj):
    #     return obj.assigned_to.user.username


class CommentAdmin(admin.ModelAdmin):
    list_display = ['issue', 'description', 'author', 'created_time']
    
    
admin.site.register(Comment, CommentAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Contributor, ContributorAdmin)
admin.site.register(Issue, IssueAdmin)

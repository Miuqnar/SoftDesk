from django.shortcuts import get_object_or_404
from rest_framework import permissions

from softdesk.projects.models import Project


class ProjectPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        if view.action in ['list', 'create', 'retrieve']:
            return request.user.is_authenticated
        else:
            if view.action in ['update', 'partial_update', 'destroy']:
                project_id = view.kwargs.get('pk')
                project = get_object_or_404(Project, pk=project_id)
                return (
                    request.user in project.contributors.all() or
                    request.user == project.author
                )
  
    
class IsProjectOwer(permissions.BasePermission):
  def has_permission(self, request, view):
      if view.action in ['list', 'retrieve']:
            return request.user.is_authenticated
      project = view.project
      return project.author == request.user
  
  def has_object_permission(self, request, view, obj):
      return obj.project.author == request.user


class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user

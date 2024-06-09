from rest_framework import permissions


class IsProjectContributor(permissions.BasePermission):
    def has_permission(self, request, view):
        # Permettre l'accès seulement aux utilisateurs authentifiés
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # Les contributors prevent voir les projects
        return (
                request.user in obj.contributors.all() or
                request.user == obj.author
        )


class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Autoriser l'accès en lecture à tous
        if request.method in permissions.SAFE_METHODS:
            return True
        # Autoriser l'accès en écriture seulement à l'auteur
        return obj.author == request.user

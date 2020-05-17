from rest_framework import permissions

class isInstanceOwnerPermission(permissions.BasePermission):

    def __init__(self):
        if not hasattr(self, 'get_owner'):
            raise NotImplementedError(
                "{} : not implemented get_owner() method".format(self.__class__.__name__ )
            )

    def has_object_permission(self, request, view, obj):
        return self.get_owner(obj) == request.user

class isOwner(isInstanceOwnerPermission):

    def get_owner(self, obj): 
        return obj.user


class isEntryOwner(isInstanceOwnerPermission):

    def get_owner(self, obj):
        return obj.entry.sheet.user


class isSheetOwner(isInstanceOwnerPermission):

    def get_owner(self, obj): 
        return obj.sheet.user

class isCategoryOwner(isInstanceOwnerPermission):

    def get_owner(self, obj):
        return obj.category.sheet.user
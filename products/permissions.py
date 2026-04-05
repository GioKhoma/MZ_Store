from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsObjectOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return request.user == obj.user
    


















    

# class IsOwnerOrStaffOrReadOnly(BasePermission):
#     def has_object_permission(self, request, view, obj):
#         if request.method in SAFE_METHODS:
#             return True
        
#         is_owner = request.user == obj.created_by
#         is_staff = request.user.groups.filter(name='StaffGroup').exists()
        
#         return is_owner or is_staff
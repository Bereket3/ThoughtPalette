from .permissions import IsStaffPermission
from rest_framework.permissions import IsAuthenticated


class StaffPermissionMixin:
    permission_classes = [IsAuthenticated, IsStaffPermission]
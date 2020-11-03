import csv

from django.contrib import admin
from django.http import HttpResponse
from django.contrib import admin
from import_export import resources
from .models import Employee
from import_export.admin import ImportExportModelAdmin
from import_export.fields import Field

from main.models import Employee, Company

# Register your models here.
# THIS IS WHERE I STARTED THE TUTORIAL
class EmployeeResource(resources.ModelResource):
    first_name = Field(attribute='first_name', column_name='First Name')
    last_name = Field(attribute='last_name', column_name='Last Name')
    email = Field(attribute='email', column_name='Email Address')


    # id = Field(attribute='id', column_name='Employee ID')

    class Meta:
        model = Employee
        #exclude = ('employee', 'id')


class EmployeeAdmin(ImportExportModelAdmin):
    resource_class = EmployeeResource
    search_fields = ("last_name__startswith",)
    list_display = ("last_name", "first_name")

#
    def first_name(self):
        return self.first_name
    first_name.short_description = 'Employees'

admin.site.register(Employee, EmployeeAdmin)


# THIS IS THE END OF THE NEW  STUFF
# @admin.register(Employee)
# class EmployeeAdmin(admin.ModelAdmin):
# list_display = ("last_name", "first_name")
# search_fields = ("last_name__startswith",)
# This was redundant since I registered it with ImportExport

#@admin.register(MaritalStatus)
#class MaritalStatusAdmin(admin.ModelAdmin):
  #  list_display = ("person", "status")
  #  search_fields = ("last_name__startswith",)


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    pass
    search_fields = ("company__startswith",)


#@admin.register(Salary)
#class SalaryAdmin(admin.ModelAdmin):
 #   list_display = ("person", "salary", "currency")
 #   search_fields = ("currency",)

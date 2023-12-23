from django.contrib import admin

from apps.secondary.models import Place, Slide, Projects,PlaceInlineInfo, GalleryImage,Gallery, Main,MainImage, Main2, MainImage2, EnvironmentImage, Environment, Street, Reach,ReachText,ApartmentPluse ,Apartment
# Register your models here.
class SlideFilterAdmin(admin.ModelAdmin):
    list_filter = ('title', )
    list_display = ('title', )
    search_fields = ('title', )

class ProjectsFilterAdmin(admin.ModelAdmin):
    list_filter = ('image', )
    list_display = ('image', )
    search_fields = ('image', )

class PlaceInfoInline(admin.TabularInline):
    model = PlaceInlineInfo
    extra = 1

class PlaceFilterAdmin(admin.ModelAdmin):
    list_filter = ('name', )
    list_display = ('name', )
    search_fields = ('name', )
    inlines = [PlaceInfoInline]

class GalleryImageInline(admin.TabularInline):
    model = GalleryImage
    extra = 1

class GalleryFilterAdmin(admin.ModelAdmin):
    list_filter = ('title', )
    list_display = ('title', )
    search_fields = ('title', )
    inlines = [GalleryImageInline]

class MainImageInline(admin.TabularInline):
    model = MainImage
    extra = 1

class MainFilterAdmin(admin.ModelAdmin):
    list_filter = ('title', )
    list_display = ('title', )
    search_fields = ('title', )
    inlines = [MainImageInline]


class MainImageInline2(admin.TabularInline):
    model = MainImage2
    extra = 1

class MainFilterAdmin2(admin.ModelAdmin):
    list_filter = ('title', )
    list_display = ('title', )
    search_fields = ('title', )
    inlines = [MainImageInline2]


class EnvironmentImageInline(admin.TabularInline):
    model = EnvironmentImage
    extra = 1

class EnvironmentFilterAdmin(admin.ModelAdmin):
    list_filter = ('title', )
    list_display = ('title', )
    search_fields = ('title', )
    inlines = [EnvironmentImageInline]

class StreetFilterAdmin(admin.ModelAdmin):
    list_filter = ('title', )
    list_display = ('title', )
    search_fields = ('title', )


class ReachTextInline(admin.TabularInline):
    model = ReachText
    extra = 1

class ReachTextFilterAdmin(admin.ModelAdmin):
    list_filter = ('name', )
    list_display = ('name', )
    search_fields = ('name', )
    inlines = [ReachTextInline]


class ApartmentPluseInline(admin.TabularInline):
    model = ApartmentPluse
    extra = 1

class ApartmentFilterAdmin(admin.ModelAdmin):
    list_filter = ('title', )
    list_display = ('title', )
    search_fields = ('title', )
    inlines = [ApartmentPluseInline]

admin.site.register(Apartment, ApartmentFilterAdmin)
admin.site.register(Reach, ReachTextFilterAdmin )
admin.site.register(Street,StreetFilterAdmin )
admin.site.register(Environment, EnvironmentFilterAdmin)
admin.site.register(Main2, MainFilterAdmin2)
admin.site.register(Main, MainFilterAdmin)
admin.site.register(Slide, SlideFilterAdmin)
admin.site.register(Projects, ProjectsFilterAdmin)
admin.site.register(Place, PlaceFilterAdmin)
admin.site.register(Gallery, GalleryFilterAdmin)
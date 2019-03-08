# -*- coding: utf-8 -*-
from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from .models import Post, Category, Tag

from .adminforms import PostAdminForm

from PP_blog.custom_site import custome_site
from PP_blog.base_admin import BaseOwnerAdmin
# Register your models here.

class CategoryOwnerFilter(admin.SimpleListFilter):
    '''自定义过滤器只展示当前用户分类'''
    title = '分类过滤器'
    parameter_name = 'owner_category'

    def lookups(self, request, model_admin):
        return Category.objects.filter(owner=request.user).values_list('id', 'name')

    def queryset(self, request, queryset):
        category_id = self.value()
        if category_id:
            return queryset.filter(category_id=self.value())
        return queryset

# inline
class PostInline(admin.TabularInline):
    fields = ('title', 'desc')
    extra = 1  # 额外增加几篇文章
    model = Post

@admin.register(Category)
class CategoryAdmin(BaseOwnerAdmin):
    list_display = ('name', 'status', 'is_nav', 'created_time', 'owner')
    fields = ('name', 'status', 'is_nav')
    inlines = [PostInline, ]

    # list_filter = [CategoryOwnerFilter]
    # def save_model(self, request, obj, form, change):
    #     obj.owner = request.user
    #     return super(CategoryAdmin, self).save_model(request, obj, form, change)
    #
    # def get_queryset(self, request):
    #     qs = super(CategoryAdmin, self).get_queryset(request)
    #     return qs.filter(owner=request.user)

@admin.register(Tag)
class TagAdmin(BaseOwnerAdmin):
    list_display = ('name', 'status', 'created_time')
    fields = ('name', 'status')

    # def save_model(self, request, obj, form, change):
    #     obj.owner = request.user
    #     return super(TagAdmin, self).save_model(request, obj, form, change)


@admin.register(Post, site=custome_site)
class PostAdmin(BaseOwnerAdmin):
    list_display = [
        'title', 'category', 'status', 'created_time', 'owner', 'operator'
    ]

    list_display_links = []
    # list_filter = ['category', ]
    # list_filter = [CategoryOwnerFilter]
    search_fields = ['title', 'category__name']

    actions_on_top = True
    actions_on_bottom = False

    # 编辑页面
    save_on_top = False

    exclude = ('owner',)

    # fields = (
    #     ('category', 'title'),
    #     'desc',
    #     'status',
    #     'content',
    #     'tag',
    # )

    form = PostAdminForm

    fieldsets = (
        ('基础配置', {
            'description': '基础配置描述',
            'fields': (
                ('title', 'category'),
                'status',
            ),
        }),
        ('内容', {
            'fields': (
                'desc',
                'content',
            ),
        }),
        ('额外信息', {
            'classes': ('collapse', ),
            'fields': ('tag', ),
        })
    )

    # 自定义静态资源引入
    class Media:
        css = {'all': (),}
        js = ()

    def operator(self, obj):
        return format_html('<a href="{}">编辑</a>', reverse('cus_admin:blog_post_change', args=(obj.id, )))

    operator.short_description = '操作'

    # def save_model(self, request, obj, form, change):
    #     obj.owner = request.user
    #     return super(PostAdmin, self).save_model(request, obj, form, change)
    #
    # def get_queryset(self, request):
    #     qs = super(PostAdmin, self).get_queryset(request)
    #     return qs.filter(owner=request.user)

# 日志配置
from django.contrib.admin.models import LogEntry
@admin.register(LogEntry, site=custome_site)
class LogEntryAdmin(admin.ModelAdmin):
    list_display = ('id', 'action_time', 'object_id', 'object_repr', 'change_message', 'user')
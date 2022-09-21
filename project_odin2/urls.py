from stock.views import contact, home, stok
from django.contrib import admin
from django.urls import path
from stock import views
from stock.views import CreateStock, UpdateStock, DeleteStock, SignUpView
from django.contrib.auth.decorators import permission_required
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('stock/', stok, name='stok'),
    path('contact/', contact, name='contact'),
    # Stock
    path('createstock/', permission_required('admin.can_addstock')
         (CreateStock.as_view()), name="createstock"),

    path('detail/<int:pk>', views.DetailStock.as_view(), name='detailstock'),
    path('detail/<int:pk>/update/', permission_required('admin.can_updatestock')
         (UpdateStock.as_view()), name="updatestock"),
    path('detail/<int:pk>/delete/', permission_required('admin.can_updatestock')
         (DeleteStock.as_view()), name="deletestock"),
    # Registration
    path("signup/", SignUpView.as_view(), name="signup"),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),




]

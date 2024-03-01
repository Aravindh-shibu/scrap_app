from django.urls import path
from scrapeeze import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
  path("signup/",views.RegisterView.as_view(),name="sign_up"),
  path("signin",views.Sign_inView.as_view(),name="sign_in"),
  path("add/<int:pk>",views.ProfileUpdateview.as_view(),name="update"),
  path("list/",views.ProfileListView.as_view(),name="list"),
  path("logout/",views.SignOutView.as_view(),name="logout"),
  path("product_add/",views.ProductAddView.as_view(),name="product_add"),
  path("ProductList/",views.ProductListView.as_view(),name="product_list"),
  path("ProductUpdate/",views.ProductUpdateView.as_view(),name="product_update"),
  path("productdetail/<int:pk>",views.ProductDetailView.as_view(),name="product-detail"),
  path("product/<int:pk>/delete",views.ScrapDeleteView.as_view(),name="delete"),
  path("product/<int:pk>/wishlist/",views.WishListView.as_view(),name="wishlist"),
  path("product/wishlist/list",views.WishListdetailView.as_view(),name="wishlistdetail"),

 ]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

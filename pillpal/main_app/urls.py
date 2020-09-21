from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('main/', views.main, name='main'),
  path('prescriptions/', views.prescriptions_index, name='index'),
  path('prescriptions/<int:prescription_id>/', views.prescriptions_detail, name='detail'),
  path('prescriptions/create/', views.PrescriptionCreate.as_view(), name='prescriptions_create'),
  path('prescriptions/<int:pk>/update/', views.PrescriptionUpdate.as_view(), name='prescriptions_update'),
  path('prescriptions/<int:pk>/delete/', views.PrescriptionDelete.as_view(), name='prescriptions_delete'),
  path('prescriptions/<int:prescription_id>/add_dosing/', views.add_dosing, name='add_dosing'),
  path('prescriptions/<int:prescription_id>/add_note/', views.add_note, name='add_note'),
  path('prescriptions/<int:prescription_id>/add_medication/', views.add_medication, name='add_medication'),
  path('prescriptions/<int:prescription_id>/medications/search/', views.medications_search, name='medication_search'),
  path('accounts/signup/', views.signup, name='signup'),
]
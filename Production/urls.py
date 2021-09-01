from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import *

router = DefaultRouter()

# router.register('Products', ProductViews, basename='Products')


urlpatterns = [
    path('viewset/', include(router.urls)),
    path('viewset/<str:pk>/', include(router.urls)),
    #------------------Batch Issuence Request--------------------#
    path('PlanNo/', PlanNoView.as_view()),
    path('ProductByPlanNo/<int:planNo>/', ProductByPlanNoView.as_view()),
    path('SBS/<str:PCode>/', SBSView.as_view()),
    path('BatchIssuenceRequest/', BatchIssuenceRequestView.as_view()),
    path('PlanNoBIR/', PlanNoBIRView.as_view()),
    path('PCodeBIR/<int:planNo>/', PCodeBIRView.as_view()),
    path('IssueBatchNo/', IssueBatchNoView.as_view()),
    path('Formulation/', FormulationView.as_view()),
    path('BPRLog/', BPRLogView.as_view()),

    #----------- Batch Track --------------#

    path('PCodeBPR/', PCodeBPRView.as_view()),
    path('BatchNoBPR/<str:PCode>/', BatchNoBPRView.as_view()),
    path('GeneralDataBPRLog/',GeneralDataBPRLogView.as_view()),
    path('BatchStages/',BatchStagesView.as_view()),
    path('DataFromBPR/<str:PCode>/',DataFromBPRView.as_view()),

    #----------- Packing --------------#
    # path('PlanNo/', PlanNoView.as_view()),
    # path('ProductByPlanNo/<int:planNo>/', ProductByPlanNoView.as_view()),
    path('PackSizeDosage/<str:PCode>/', PackSizeDosageView.as_view()),
    path('BatchNoFromBPR/<str:PCode>/', BatchNoFromBPRView.as_view()),
    path('PackingLog/', PackingLogView.as_view()),

    #---------------- Close Order --------------------#
    path('PlanItems/',PlanItemsView.as_view()),
    path('PlanStatus/',PlanStatusView.as_view()),
]
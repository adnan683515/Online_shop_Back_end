
from . import views
from django.urls import path






urlpatterns = [

    path('delivery/',views.DeliveryView.as_view(),name='delivery'),
    path('viewproduct/',views.viewModelObject.as_view()),
    path('viewDelete/<int:pk>/',views.ViewMOdelapiview.as_view()),
    path('brandpost/',views.BrandPost.as_view()),
    path('cetagorypost/',views.CetagoryPost.as_view()),
    path('courntrypost/',views.CountryPost.as_view()),
    path('colourpost/',views.ColourPost.as_view()),
    path('sizepost/',views.SizePOst.as_view()),
    path('deletecolourput/<int:pk>/',views.DeletePUtColour.as_view()),
    path('brandPutDelte/<int:pk>/',views.BrandDeletePUT.as_view()),
    path('countryPutDelet/<int:pk>/',views.CountryPUTDelete.as_view()),
    path('cetagoryputdelete/<int:pk>/',views.CetagoryPUTDelete.as_view()),
    path('allteam/',views.AllTeam.as_view()),
    path('teamputdelte/<int:pk>/',views.TeamNameDeleteAndPut.as_view()),
    path('mainmetarials/',views.MainMetarialsApiView.as_view()),
    path('editdeletemeta/<int:pk>/',views.EditMetaDelete.as_view()),
    path('versionpost/',views.VersionPost.as_view())
    ]

from rest_framework import serializers
from product_app.models import Product,review,Team,version,MainMetariails
from man.serializer import BrandSerializer,CetagorySerializer

class football_serializer(serializers.ModelSerializer):
    football_cetagory = serializers.CharField(read_only=True)
    class Meta:
        model = Product
        exclude = ['Movement_Watch','Strap_metarail_watch','warenty_watch','size']
    
    
class versionSerailizer(serializers.ModelSerializer):
    class Meta:
        model = version
        fields = '__all__'
        
        
class review_football_serializer(serializers.ModelSerializer):
    class Meta:
        model = review
        exclude = ['rating']
        
class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'
        
class JurseySerializer(serializers.ModelSerializer):
    version=serializers.CharField(read_only=True)
    class Meta:
        model = Product
        fields = ['id','type_your_product','sports_Type','version','product_title','display_image','font_image','back_image','quantity','range_of_price','fixed_price','colour','country','description','abailable','eyes','team']
        
        
        
class CricketProductSerializer(serializers.ModelSerializer):
    CricketBatBrand = serializers.CharField(read_only=True)
    MainMetariails = serializers.CharField(read_only=True)
    version = serializers.CharField(read_only=True)
    country = serializers.CharField(read_only=True)
    colour = serializers.CharField(read_only=True)
    Brand = BrandSerializer()
    class Meta:
        model = Product
        fields =['id','Brand','type_your_product','sports_Type','product_title','display_image','font_image','back_image','quantity','range_of_price','fixed_price','colour','country','description','abailable','eyes','MainMetariails','version']
        

class MainMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainMetariails
        fields = '__all__'
    


class FootballSerializer(serializers.ModelSerializer):
    version = serializers.CharField(read_only=True)
    Brand = BrandSerializer()
    cetagory = CetagorySerializer()
    class Meta:
        model = Product
        fields = ['id','product_title','cetagory','type_your_product','version','sports_Type','display_image','font_image','back_image','quantity','range_of_price','fixed_price','colour','country','description','abailable','eyes','warenty_watch','Brand']
        
class JurseySerializer(serializers.ModelSerializer):
    colour = serializers.CharField(read_only=True)
    team = serializers.CharField(read_only=True)
    version = serializers.CharField(read_only=True)
    country = serializers.CharField(read_only=True)
    
    class Meta:
        model = Product
        fields = ['id','product_title','type_your_product','sports_Type','display_image','font_image','back_image','quantity','range_of_price','fixed_price','colour','country','description','abailable','eyes','team','version']
    
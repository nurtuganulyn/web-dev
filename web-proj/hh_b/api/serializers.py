from rest_framework import serializers
from api.models import Company, Vacancy, Category, Product, Card


class CompanySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField()
    city = serializers.CharField()
    address = serializers.CharField()

    def create(self, validated_data):
        company = Company.objects.create(name=validated_data('name'),
                                         description=validated_data('description'),
                                         city=validated_data('city'),
                                         address=validated_data('address'))
        return company

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.city = validated_data.get('city', instance.city)
        instance.address = validated_data.get('address', instance.address)
        instance.save()
        return instance


class VacancySerializer(serializers.ModelSerializer):
    company_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Vacancy
        fields = ('id', 'name', 'description', 'salary', 'company_id')


class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()

    def create(self, validated_data):
        category = Category.objects.create(name=validated_data('name'))

        return category

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)

        instance.save()
        return instance


class ProductSerializer(serializers.ModelSerializer):
    category_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Product
        fields = ('id', 'name', 'imageLink1', 'imageLink2', 'description', 'price', 'category_id')


class CardSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)

    class Meta:
        model = Card
        fields = {'id', 'products'}

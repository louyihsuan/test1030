import graphene
from graphene_django import DjangoObjectType
#from graphene_django import DjangoListField
from .models import Category
#edit by yhlou 20211031
class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ("id","name")

#get
class Query(graphene.ObjectType):
    all_categorys = graphene.List(CategoryType)
    categorys = graphene.Field(CategoryType, id=graphene.Int())
    
    def resolve_all_categorys(root, info):
        return Category.objects.all()
    def resolve_categorys(root, info, id):
        return Category.objects.get(pk=id)

#post
class CreateCategoryMutation(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
    category = graphene.Field(CategoryType)

    @classmethod
    def mutate(cls, root, info, name):
        category = Category(name=name)
        category.save()
        return CreateCategoryMutation(category=category)

#put
class UpdateCategoryMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        name = graphene.String(required=True)
    category = graphene.Field(CategoryType)

    @classmethod
    def mutate(cls, root, info, name, id):
        category = Category.objects.get(id=id)
        category.name = name
        category.save()
        return UpdateCategoryMutation(category=category)

#delete
class DeleteCategoryMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        #name = graphene.String(required=True)
    category = graphene.Field(CategoryType)

    @classmethod
    def mutate(cls, root, info, id):
        category = Category.objects.get(id=id)
        category.delete()
        return DeleteCategoryMutation(category=category)

class Mutation(graphene.ObjectType):
    create_category = CreateCategoryMutation.Field()
    update_category = UpdateCategoryMutation.Field()
    delete_category = DeleteCategoryMutation.Field()
    print ("debug")
schema = graphene.Schema(query=Query, mutation=Mutation)

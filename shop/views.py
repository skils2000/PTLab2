import copy

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView

from .models import Product, Purchase, ProductToPurchase

# Create your views here.
def index(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'shop/index.html', context)


class PurchaseCreate(CreateView):
    model = Purchase
    fields = ['person', 'address']

    def form_valid(self, form):
        self.object = form.save()
        allProducts = Product.objects.all()
        requestBuyList = self.request.POST['products'].split(",")
        finalBuyList = []
        #print(len(requestBuyList))
        #print("------------------------------")
        for pi in range(len(requestBuyList)):
            for p in allProducts:
                if str(p.id) == str(requestBuyList[pi]):
                    finalBuyList.append(copy.deepcopy(p))

        #print(finalBuyList)

        buyListTypes = []
        buyListTypesCount = []

        for product in finalBuyList:
            j = -1
            for idType, line in enumerate(buyListTypes):
                if str(line) == str(product.type.id):
                    j = idType
                    break;

            if j != -1:
                buyListTypesCount[j] = buyListTypesCount[j]+1
            else:
                buyListTypes.append(product.type.id)
                buyListTypesCount.append(1)

        items_with_discount = 0

        if len(buyListTypesCount)>2:
            buyListTypesCount.sort()
            items_with_discount = buyListTypesCount[0]

            finalBuyList.sort(key=lambda x: x.price)


        for idproduct, product in enumerate(finalBuyList):
            if items_with_discount > 0 and idproduct < items_with_discount:
                product.price = product.price/10*6

            #print(product.price)
            ProductToPurchase.objects.create(product=Product.objects.get(pk=product.id), purchase=self.object, finalPrice=product.price)

        return HttpResponse(f'Спасибо за покупку, {self.object.person}!')


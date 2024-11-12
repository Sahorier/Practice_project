from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

product_dict = {
    "mouse" : ["PCM001-(MOUSE)", "PCM002-(MOUSE)", "PCM003-(MOUSE)"],
    "keyboard" : ["PCK001-(KEYBOARD)", "PCK002-(KEYBOARD)", "PCK003-(KEYBOARD)"],
    "actionfigure" : ["PAF001-(ANIME ACTION FIGURE)", "PAF002-(ANIME ACTION FIGURE)", "PAF003-(ANIME ACTION FIGURE)"],
}


pages = [
    "index",
    "products",
    "cart",
    "checkout",
    "contact",
]

def shop_page(request):
    return render(request, "shop/index.html", {
        "shopname":"myshop",
        "pages": pages,
    })
    
def redirect_pages(request, page):
    try:
        if page in pages:
            redirect_path = reverse("shop_main", args=[page])
            # if not redirect_path.endswith("/"):
            #     redirect_path += "/"
            return HttpResponseRedirect(redirect_path)
    
    except:
        return HttpResponseNotFound("invalid page")
def redirect_slash_product(request):
    redirect_path = reverse("product_page")
    return HttpResponse(redirect_path)


def product_list_page(request):
    try:
        return render(request, "shop/products.html", {
            "products": list(product_dict.keys())
        })
    except:
        return HttpResponseNotFound("not found")

def product_pages(request, product_page):
    try:
        product_list = product_dict[product_page]
        page_response = " , ".join(product_list)
        return HttpResponse(page_response)
    except:
        return HttpResponseNotFound("Product Not available")
    
    
# def page(request , shop_page):
#     try:
#         page_response = pages[shop_page]
#     except:
#         return HttpResponseNotFound("Page not found")
#     return HttpResponse(page_response)

def specific_productint(request,product_page, product):
    try:
        page_response = product_dict[product_page]
        spec_product = page_response[product - 1]
        return HttpResponse(spec_product)
    except:
        return HttpResponseNotFound("Product Not available")


# def specific_productstr(request,product_page, product):
#     try:
#         products = product_dict[product_page]
#         page_response = 
#         return HttpResponse(page_response)
#     except:
#         return HttpResponseNotFound("Product Not available")

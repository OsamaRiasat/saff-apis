from .models import *



def demandedItemsCodesList(DNo):
    data = RMDemandedItems.objects.filter(DNo=DNo)  # This will give objects of approved items having this SID
    l=[]
    for obj in data:
            code = obj.RMCode.RMCode
            l.append(code)
    return l


# def approvedItems(SID):
#     data = SupplierApprovedItems.objects.filter(S_ID=SID)  # This will give objects of approved items having this SID
#     l = []
#     for obj in data:
#         dic = {}
#         Materials = RawMaterials.objects.filter(pk=obj.MCode).only('Material')
#         dic["Material"] = Materials.get().Material
#         l.append(dic)
#     return l


import json
from .OrderMangementException import OrderManagementException
from .OrderRequest import OrderRequest

class OrderManager:
    def __init__(self):
        pass

    def validateEAN13(self, eAn13):
        # PLEASE INCLUDE HERE THE CODE FOR VALIDATING THE GUID
        # RETURN TRUE IF THE GUID IS RIGHT, OR FALSE IN OTHER CASE
        try:
            number = eAn13[:-1]
            check = 10 - int(eAn13[-1])
            count = 0
            mult = 1
            for i in number:
                count += int(i)*mult
                mult = 1 if mult == 3 else 3
            if count % 10 != check:
                return False
            return True
        except:
            raise Exception("Variable contains incorrect characters")



    def readproductcodefromJSON(self, fi):

        try:
            with open(fi) as f:
                Data = json.load(f)
        except FileNotFoundError as e:
            raise OrderManagementException("Wrong file or file path") from e
        except json.JSONDecodeError as e:
            raise OrderManagementException("JSON Decode Error - Wrong JSON Format") from e


        try:
            Product = Data["id"]
            Ph = Data["phoneNumber"]
            req = OrderRequest(Product, Ph)
        except KeyError as e:
            raise OrderManagementException("JSON Decode Error - Invalid JSON Key") from e
        if not self.validateEAN13(Product):
            raise OrderManagementException("Invalid PRODUCT code")

        # Close the file
        return req
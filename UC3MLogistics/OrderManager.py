import json
from .OrderMangementException import OrderManagementException
from .OrderRequest import OrderRequest

class OrderManager:
    def __init__(self):
        pass

    def ValidateEAN13( self, eAn13 ):
        # PLEASE INCLUDE HERE THE CODE FOR VALIDATING THE GUID
        # RETURN TRUE IF THE GUID IS RIGHT, OR FALSE IN OTHER CASE
        print(eAn13)
        print(type(eAn13))
        try:
            number = eAn13[:-1]
            check = int(eAn13[-1])
            count = 0
            for i in number:
                count += int(i)
            if not count % 10 == check:
                return False
            return True
        except:
            raise Exception("Variable contains incorrect characters")



    def ReadproductcodefromJSON( self, fi ):

        try:
            with open(fi) as f:
                DATA = json.load(f)
        except FileNotFoundError as e:
            raise OrderManagementException("Wrong file or file path") from e
        except json.JSONDecodeError as e:
            raise OrderManagementException("JSON Decode Error - Wrong JSON Format") from e


        try:
            PRODUCT = DATA["id"]
            PH = DATA["phoneNumber"]
            req = OrderRequest(PRODUCT, PH)
        except KeyError as e:
            raise OrderManagementException("JSON Decode Error - Invalid JSON Key") from e
        if not self.ValidateEAN13(PRODUCT):
            raise OrderManagementException("Invalid PRODUCT code")

        # Close the file
        return req
from .utils import FormValidator
from .models import Location

from authentication.models import AdmCustomer

class CreateLocationForm(FormValidator):
    
    def validate_customer_id(self):

        customerid = self.data.get("customerid", None)

        print("customer id :: ",customerid)

        if not customerid:
            return self.errors.update({"customer" : "The customerid feild is required."})

        if not AdmCustomer.objects.filter(id=customerid).exists():

            return self.errors.update({"customer" : "Customer {customerid} does not exist".format(customerid=customerid)})
        
        self.cleaned_data["customerid"] = customerid

    def validate_name(self):
        name = self.data.get("name", None)
        if not name:
            return self.errors.update({"name":"The name feild is required."})
        if len(name) < 5:
            return self.errors.update({"name":"Name is too short."})
        
        self.cleaned_data["name"] = name


    def save(self):
        data = self.data
        data.update(self.cleaned_data)
        
        print(type(data))

        location = Location()

        for key, val in data.items():
            print("key val ", key , val)
            setattr(location, key, val)

        customerid = AdmCustomer.objects.get(id=data.customerid)
        setattr(location,"customer", customerid)

        '''location = Location(
            name = data.name,
            hotspotenable = data.hotspotenable,
            autologinenable = data.autologinenable,
            automacregister = data.automacregister,
            autologinvalidity = data.autologinvalidity,
            autologinvalidity_unit = data.autologinvalidity_unit,
            interiminterval = data.interiminterval,
            customer = customerid
        )'''

        location.save()

        return location
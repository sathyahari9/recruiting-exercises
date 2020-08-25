import os
import json
import collections

# Class to implement Inventory Allocator
class InventoryAllocator:
    def __init__(self, quantities, inventory):        
        self.quantities = quantities
        self.inventory = inventory

    # Create a dictionary of allocated resources
    # Returns: (dict) of allocated resource
    def allocate_resources(self):
        # Create a dictionary with the each warehouse as a key, and the share of items shipped as the value
        quantities_shipped = collections.defaultdict(dict)

        # Go through each item, and split the quantity across the warehouses
        for item in self.quantities.keys():
            amount = 0

            for warehouse in self.inventory:
                # If item not in warehouse, check next
                if item not in warehouse["inventory"]:
                    continue

                # If the warehouse has a less than the amount required, take everything and move to the next
                if self.quantities[item] >= warehouse["inventory"][item]:
                    quantities[item] -= warehouse["inventory"][item]
                    amount = warehouse["inventory"][item]
                    warehouse["inventory"][item] = 0
                else:
                    # If warehouse has a surplus of item, reduce quantity required to 0 and proceed to the next item
                    warehouse["inventory"][item] -= self.quantities[item]
                    amount = self.quantities[item]
                    self.quantities[item] = 0
                
                # check amount left, if 0, proceed to next item
                if not amount:
                    break
                # track amounts shipped per item for each warehouse
                quantities_shipped[warehouse["name"]][item] = amount
            
            # If items are still required, return an empty dictionary as the allocation is not valid
            if self.quantities[item]:
                return {}

        return dict(quantities_shipped)

    # Output in the form of an array
    # Returns: (list) of allocation of items by warehouse
    def allocation_result(self):
        quantities_shipped = self.allocate_resources()
        # Convert dict to array
        result = []
        for warehouse in quantities_shipped.keys():
            result.append({warehouse: quantities_shipped[warehouse]})
        
        return result

if __name__ == '__main__':
    quantities_dir = 'tests/quantities/'
    inventory_dir = 'tests/inventory/'
    quantities_string = ""
    inventory_string = ""

    # Run test suite
    for test in os.listdir(quantities_dir):
        with open(quantities_dir + test) as f:
            quantities_string = f.read()

        with open(inventory_dir + test) as f:
            inventory_string = f.read()

        quantities = json.loads(quantities_string)
        inventory = json.loads(inventory_string)

        allocator_instance = InventoryAllocator(quantities, inventory)

        print(test + ": " + str(allocator_instance.allocation_result()))
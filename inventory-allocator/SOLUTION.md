### InventoryAllocator class
This class is implemented to have the following class variables:
- quantities - quantities of items required
- inventory - description of the items present at each warehouse

The class has the following class methods:
- allocate_resources - Computes the best way an order can be shipped (called shipments) given inventory across a set of warehouses (called inventory distribution)
- allocation_result - Formats the output in the form of a list

### Testing
The test scenarios are autmatically run, and the result of each test is printed along with the corresponding input file name.
To add more tests:
Input the quantities of each item in the form of a json file.
- For example, "inventory/testx.json" will contain - {"apple" : 10}
Similarly, input the inventory present of each item in the inventory folder in this manner: \\
[{ "name": "owd", "inventory": { "apple": 5 } }, { "name": "dm", "inventory": { "apple": 5 }}] \\
Make sure to give the same file name for both the quantities and inventory files. For example: "test1.json"
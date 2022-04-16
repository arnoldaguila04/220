from sales_person import SalesPerson


class SalesForce:

    def __init__(self):
        self.sales_people = []

    def add_data(self, file_name):
        file = open(file_name, "r")
        for line in file.readlines():
            line = line.split(",")
            employee = SalesPerson(int(line[0]), line[1].strip())
            sales = line[2].split()
            for sale in sales:
                employee.enter_sale(float(sale))
            self.sales_people.append(employee)

    def quota_report(self, quota):
        outer_list = []
        inner_list = []
        for person in self.sales_people:
            identification = person.get_id()
            name = person.get_name()
            total = person.total_sales()
            true_false = person.met_quota(quota)
            inner_list.append(identification)
            inner_list.append(name)
            inner_list.append(total)
            inner_list.append(true_false)
            outer_list.append(inner_list)
            inner_list = []
        return outer_list

    def top_seller(self):
        empty_list = []
        other_person = self.sales_people[0]
        for person in self.sales_people:
            if person.compare_to(other_person) == 1:
                other_person = person
        for person in self.sales_people:
            if person.compare_to(other_person) == 0:
                empty_list.append(other_person)
        return empty_list

    def individual_sales(self, employee_id):
        for person in self.sales_people:
            if person.get_id() == employee_id:
                return person

    def get_sale_frequencies(self):
        dictionary = {}
        for person in self.sales_people:
            sales = person.get_sales()
            for sale in sales:
                dictionary.setdefault(sale, 0)
                dictionary[sale] += 1
        return dictionary

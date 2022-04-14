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
        return outer_list

    def top_seller(self):
        empty_list = []
        for person in self.sales_people:
            for other_person in self.sales_people:
                # print(person)
                # print(other_person)
                # print(person.compare_to(other_person))
                if person != other_person:
                    test = person.compare_to(other_person)
                    if test == 1:
                        empty_list.append(person)
                    elif test == -1:
                        empty_list.append(other_person)
                    elif test == 0:
                        empty_list.append(person)
                        empty_list.append(other_person)

    def individual_sales(self, employee_id):
        for person in self.sales_people:
            if person.get_id == employee_id:
                return person.get_name

    def get_sale_frequencies(self):
        pass

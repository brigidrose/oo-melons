"""Classes for melon orders."""

class AbstractMelonOrder(object): 
    """An abstract melon class the other classes inherit from"""
    def __init__(self, species, qty, order_type, tax):
        self.species = species
        self.qty = qty
        self.shipped = False
        self.order_type = order_type
        self.tax = tax

    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5 
        if self.species == "Christmas Melon":
            base_price = base_price * 1.51

        total = (1 + self.tax) * self.qty * base_price


        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True



class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""
        #change order type and tax
        super(DomesticMelonOrder, self).__init__(species, qty, "Domestic", 0.08)


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""
        #change order type and tax
        super(InternationalMelonOrder, self).__init__(species, 
                                                 qty,
                                                 "international", 
                                                 0.17)
        self.country_code = country_code
   
    

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

    def get_total(self):
        """Calculate price, including tax."""
        total = super(InternationalMelonOrder, self).get_total()

        if self.qty < 10: 
           total += 3

        return total

        #Im a lazy child

class GovernmentMelonOrder(AbstractMelonOrder):
    """ A melon order from the government."""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""
        #change order type and tax
        super(GovernmentMelonOrder, self).__init__(species, qty, "Domestic", 0)

        self.passed_inspection = False

    def mark_inspection(self, passed):
        """Record the fact than an order has been shipped."""

        self.passed_inspection = passed
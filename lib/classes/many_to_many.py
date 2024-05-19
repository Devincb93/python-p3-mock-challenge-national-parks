class NationalPark:

    def __init__(self, name):
        self.name = name
        self._trips = []
        self._visitors = {}

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if hasattr(self, 'name'):
            raise Exception("Cannot modify name after instantiation")
        else:
            if isinstance(value, str) and len(value) >= 3:
                self._name = value
               
    def trips(self):
        self._trips = [trip for trip in Trip.all if trip.national_park == self]
        return self._trips
        
    
    def visitors(self):
        
        for visitor in Trip.all:
            if visitor.national_park == self:
                if visitor.visitor in self._visitors:
                    self._visitors[visitor.visitor] += 1
                else:
                    self._visitors[visitor.visitor] = 1
        return list(self._visitors)
        # self._visitors = [visitor.visitor for visitor in Trip.all if visitor.national_park == self]
        # return self._visitors

        
    
    def total_visits(self):
        return len(self.trips())
    
        
        
    
    def best_visitor(self):
        visitors = [trip.visitor for trip in self.trips()]
        return max(set(visitors), key= visitors.count)
        


class Trip:
    all = []
    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        Trip.all.append(self)

    @property
    def start_date(self):
        return self._start_date
    
    @start_date.setter
    def start_date(self, value):
        if isinstance(value, str) and len(value) >= 7:
            self._start_date = value

    @property
    def end_date(self):
        return self._end_date
    
    @end_date.setter
    def end_date(self, value):
        if isinstance(value, str) and len(value) >= 7:
            self._end_date = value

    @property
    def visitor(self):
        return self._visitor
    
    @visitor.setter
    def visitor(self, value):
        if isinstance(value, Visitor):
            self._visitor = value

    @property
    def national_park(self):
        return self._national_park
    

    @national_park.setter
    def national_park(self, value):
        if isinstance(value, NationalPark):
            self._national_park = value
    



class Visitor:
    
    def __init__(self, name):
        self.name = name
        self._trips = []
        self._parks = []
        
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 15:
            self._name = name
        else:
            raise Exception
        
        
        
    def trips(self):
        # if isinstance(self, Visitor):
        #     for i in Trip.all:
        #         if i.visitor == self:
        #             self._trips.append(i)
        # return self._trips
        
        self._trips = [trip for trip in Trip.all if trip.visitor == self]
        return self._trips
        
    
    def national_parks(self):
        # if isinstance(self.national_park, NationalPark):
        #     self._parks = [park for park in Trip.all if park.national_park == self and park.visitor == self]
        # return self._parks

        # for i in self.trips():
        #     if i.national_parks == self:
        #         self._parks.append(i)
        return list({trip.national_park for trip in self.trips()})
        
    
    def total_visits_at_park(self, park):
        if not park.visitors():
            return 0
        return len([trip for trip in self.trips() if trip.national_park == park])
        
       
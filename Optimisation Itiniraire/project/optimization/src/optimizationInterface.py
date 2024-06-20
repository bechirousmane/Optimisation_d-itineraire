from abc import ABC, abstractmethod

class optimizationInterface(ABC) :

    @abstractmethod
    def optimizationAlgo(self,breakpoint, start) :
        pass

    def itinerary(self, Breakpoint, start) : 
        itinerary = self.optimizationAlgo(Breakpoint, start)
        return itinerary
from .data import Data
from .platform import API

class ActApis(Data):
    platform: API
    manually_cut_beef: bool

    def supply_beef(self):
        if self.manually_cut_beef:


    def supply_cucumber(self):
        ...

    def supply_cream(self):
        ...

    def supply_fries_potato(self):
        ...

    def supply_kibbeh(self):
        ...

    def supply_orange_juice(self):
        ...

    def wrap_shawarma(self):
        ...

    def pack_shawarma(self):
        ...

    def cut_potato(self):
        ...

    def give_shawarma_to(self, consumer):
        ...

__author__ = 'h.rouhani'


class Office:
    def _getCode(self):
        return self.code

    def _setCode(self, code):
        self.code = code

    def _setUnitNumber(self, unitNumber):
        self.unitNumber = unitNumber

    def _getUnitNumber(self):
        return self.unitNumber

    def _getFloorNo(self):
        return self.floorNo

    def _setFloorNo(self, floorNo):
        self.floorNo = floorNo

    def _getSectionNo(self):
        return self.sectionNo

    def _setSectionNo(self, sectionNo):
        self.sectionNo = sectionNo

    def _get_date(self):
        if hasattr(self, "date"):
            return self.date
        return None

    def _set_date(self, date):
        self.date = date

    Code = property(_getCode, _setCode)
    UnitNumber = property(_getUnitNumber, _setUnitNumber)
    FloorNo = property(_getFloorNo, _setFloorNo)
    SectionNo = property(_getSectionNo, _setSectionNo)
    Date = property(_get_date, _set_date)

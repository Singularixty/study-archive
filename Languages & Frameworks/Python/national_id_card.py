class NationalIDCard:
    def __init__(self, first_name, last_name, birth_date, address):
        self._first_name = first_name
        self._last_name = last_name
        self._birth_date = birth_date
        self._address = address
        self._nationality = self._determine_nationality()
        self._scan_id()
    def _determine_nationality(self):
        return 'Unknown'
    def _scan_id(self):
        print('---------[ ID SCANNED ]---------')
        print(f'First Name: {self._first_name}')
        print(f'Last Name: {self._last_name}')
        print(f'Nationality: {self._nationality}')
        print(f'Date of Birth: {self._birth_date}')
        print(f'Address: {self._address}')
class USACard(NationalIDCard):
    def _determine_nationality(self):
        return 'American'
class ThaiCard(NationalIDCard):
    def _determine_nationality(self):
        return 'Thai'
usa_id_card = USACard('Emily', 'Johnson', '1/5/1999', '123 Fake Street, Washington D.C. 123545')
thai_id_card = ThaiCard('Somsak', 'Sompong', '1/1/1990', '123 Bangkok Street, Bangkok 123455')

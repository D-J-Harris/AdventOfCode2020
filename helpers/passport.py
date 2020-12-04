class Passport:

    def __init__(self, passport_dict):
        self.byr = passport_dict['byr'] if 'byr' in passport_dict else None
        self.iyr = passport_dict['byr'] if 'byr' in passport_dict else None
        self.eyr = passport_dict['byr'] if 'byr' in passport_dict else None
        self.hgt = passport_dict['byr'] if 'byr' in passport_dict else None
        self.hcl = passport_dict['byr'] if 'byr' in passport_dict else None
        self.ecl = passport_dict['byr'] if 'byr' in passport_dict else None
        self.pid = passport_dict['byr'] if 'byr' in passport_dict else None
        self.cid = passport_dict['byr'] if 'byr' in passport_dict else None
        self.num_keys = len(passport_dict)
        self.dict_repr = passport_dict

    def is_valid(self):
        return self.num_keys == 8 or (self.num_keys == 7 and not self.cid)

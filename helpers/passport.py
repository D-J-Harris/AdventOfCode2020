import re


class Passport:

    def __init__(self, passport_dict):
        self.byr = passport_dict['byr'] if 'byr' in passport_dict else None
        self.iyr = passport_dict['iyr'] if 'iyr' in passport_dict else None
        self.eyr = passport_dict['eyr'] if 'eyr' in passport_dict else None
        self.hgt = passport_dict['hgt'] if 'hgt' in passport_dict else None
        self.hcl = passport_dict['hcl'] if 'hcl' in passport_dict else None
        self.ecl = passport_dict['ecl'] if 'ecl' in passport_dict else None
        self.pid = passport_dict['pid'] if 'pid' in passport_dict else None
        self.cid = passport_dict['cid'] if 'cid' in passport_dict else None
        self.num_keys = len(passport_dict)
        self.dict_repr = passport_dict

    def is_valid(self):
        return self.num_keys == 8 or (self.num_keys == 7 and not self.cid)

    def is_valid_with_checks(self):
        return self.year_check() and self.id_check() and self.color_check() and self.height_check()

    def year_check(self):
        byr_valid = 1920 <= int(self.byr) <= 2002 if self.byr else 0
        iyr_valid = 2010 <= int(self.iyr) <= 2020 if self.iyr else 0
        eyr_valid = 2020 <= int(self.eyr) <= 2030 if self.eyr else 0
        return byr_valid and iyr_valid and eyr_valid

    def id_check(self):
        pid_valid = bool(re.match("^[0-9]{9}$", self.pid)) if self.pid else 0
        cid_valid = 1
        return pid_valid and cid_valid

    def color_check(self):
        valid_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        hcl_valid = (bool(re.match("^#[A-Za-z0-9]{6}$", self.hcl))) if self.hcl else 0
        ecl_valid = self.ecl in valid_colors if self.ecl else 0
        return hcl_valid and ecl_valid

    def height_check(self):
        hgt_valid = (("cm" in self.hgt and 150 <= int(self.hgt.replace("cm", "")) <= 193) or
                     ("in" in self.hgt and 59 <= int(self.hgt.replace("in", "")) <= 76))
        return hgt_valid

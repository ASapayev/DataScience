class MySelectQuery:
    def __init__(self, csv_matn):
        """CSV formatiga o'xshash matn qabul qiladi.
        Satrlar "," bilan, ustunlar "\n" bilan ajiratilgan.
        Matnning birinchi (\n gacha bo'lgan) satrida ma'lumot turi beriladi."""
        self.satr = csv_matn.split("\n")
        self.ustun = self.satr[0]
        self.matn = self.satr[1:]


    def where(self, malumot_turi, qiymat):
        """Bizga ma'lumot turi beriladi.
        Shuni ichida berilgan qiymatga teng javob topilsa,
        shu satr to'liq chop etilishi kerak."""
        ind = self.ustun.index(malumot_turi)
        javob = []
        for qator in self.matn:
            malumotlar = qator.split(",")
            if malumotlar[ind] == qiymat:
                javob.append(qator)
                return javob
names = []
notes = []
firstperson = []
secoundperson = []
thirtperson = []
sozluk = {}
i = 1

while i < 4:
    name = input("{0}. öğrencinin ismini  ve soyismini giriniz: ".format(i))

    midterm = input("{0}. öğrencinin yarıyıl notu giriniz: ".format(i))
    final = input("{0}. öğrencinin final notunu giriniz: ".format(i))
    homework = input("{0}. öğrencinin ödev notunu giriniz: ".format(i))

    try:
        assert len(name) != 0, "İsim bölümü veya soyisim bölümü boş olamaz."
        names.append(name)
        midterm = int(midterm)
        final = int(final)
        homework = int(homework)
        assert midterm != 0, "Yarıyıl değerine 0 değeri girildi. Lütfen doğru aralık içerisinde değer giriniz. (0-100)"
        assert midterm > 0, "Yarıyıl değerine 0'dan küçük girildi. Lütfen doğru aralık içerisinde değer giriniz. (0-100)"
        assert midterm <= 100, "Yarıyıl değerine 100'den büyük girildi. Lütfen doğru aralık içerisinde değer giriniz. (0-100)"
        assert final != 0, "Final değerine 0 değeri girildi. Lütfen doğru aralık içerisinde değer giriniz. (0-100)"
        assert final > 0, "Final değerine 0'dan küçük girildi. Lütfen doğru aralık içerisinde değer giriniz. (0-100)"
        assert final <= 100, "Final değerine 100'den büyük girildi. Lütfen doğru aralık içerisinde değer giriniz. (0-100)"
        assert homework != 0, "Ödev değerine 0 değeri girildi. Lütfen doğru aralık içerisinde değer giriniz. (0-100)"
        assert homework > 0, "Ödev değerine 0'dan küçük girildi. Lütfen doğru aralık içerisinde değer giriniz. (0-100)"
        assert homework <= 100, "Ödev değerine 100'den büyük girildi. Lütfen doğru aralık içerisinde değer giriniz. (0-100)"

        sum1 = (midterm + final + homework)
        average1 = (sum1 / 3)
        notes.append(midterm)
        notes.append(final)
        notes.append(homework)
        notes.append(average1)
        sozluk[name] = midterm, final, homework, average1

        i += 1
    except ValueError:
        print("Lütfen sadece sayı girin!")
    except AssertionError as error:
        print(error)

firstperson.append(names[0:1])
firstperson.append(notes[0:4])

secoundperson.append(names[1:2])
secoundperson.append(notes[4:8])

thirtperson.append(names[2:3])
thirtperson.append(notes[8:12])

average = notes[3:12:4]
maxscore = max(average)

print(sozluk)

if maxscore == average[0]:
    print("{1} tebrik ederiz {0} puan ile birincisiniz.".format(average[0], names[0]))
elif maxscore == average[1]:
    print("{1} tebrik ederiz {0} puan ile birincisiniz.".format(average[1], names[1]))
else:
    print("{1} tebrik ederiz {0} puan ile birincisiniz.".format(average[2], names[2]))
#print(names)
#print(notes)
#print(firstperson)
#print(secoundperson)
#print(thirtperson)
#print(average)
#print(maxscore)
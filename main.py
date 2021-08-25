print("Podaj kwotę kredytu")
credit = int(input())
print("Podaj ratę")
principal = int(input())
print("Podaj oprocentowanie")
interest = int(input())

Styczen1 = 1.592824484
Luty1 = -0.453509101
Marzec1 = 2.324671717
Kwiecien1 = 1.261254407
Maj1 = 1.782526286
Czerwiec1 = 2.329384541
Lipiec1 = 1.502229842
Sierpien1 = 1.782526286
Wrzesien1 = 2.328848994
Pazdziernik1 = 0.616921348
Listopad1 = 2.352295886
Grudzien1 = 0.337779545
Styczen2 = 1.577035247
Luty2 = -0.292781443
Marzec2 = 2.48619659
Kwiecien2 = 0.267110318
Maj2 = 1.417952672
Czerwiec2 = 1.054243267
Lipiec2 = 1.480520104
Sierpien2 = 1.577035247
Wrzesien2 = -0.07742069
Pazdziernik2 = 1.165733399
Listopad2 = -0.404186718
Grudzien2 = 1.499708521

print("********************\nKredyt na kwotę: {}".format(credit) + "\nRata: {}".format(principal) +  "\nOprocentowanie: {}".format(interest))

kwota0 = credit
kwotaStyczen1 = (1 + (Styczen1 + interest)/1200) * credit - principal
kwotaLuty1 = (1 + (Luty1 + interest)/1200) * kwotaStyczen1 - principal
kwotaMarzec1 = (1 + (Marzec1 + interest)/1200) * kwotaLuty1 - principal
kwotaKwiecien1 = (1 + (Kwiecien1 + interest)/1200) * kwotaMarzec1 - principal
kwotaMaj1 = (1 + (Maj1 + interest)/1200) * kwotaKwiecien1 - principal
kwotaCzerwiec1 = (1 + (Czerwiec1 + interest)/1200) * kwotaMaj1 - principal
kwotaLipiec1 = (1 + (Lipiec1 + interest)/1200) * kwotaCzerwiec1 - principal
kwotaSierpien1 = (1 + (Sierpien1 + interest)/1200) * kwotaLipiec1 - principal
kwotaWrzesien1 = (1 + (Wrzesien1 + interest)/1200) * kwotaSierpien1 - principal
kwotaPazdziernik1 = (1 + (Pazdziernik1 + interest)/1200) * kwotaWrzesien1 - principal
kwotaListopad1 = (1 + (Listopad1 + interest)/1200) * kwotaPazdziernik1 - principal
kwotaGrudzien1 = (1 + (Grudzien1 + interest)/1200) * kwotaListopad1 - principal

kwotaStyczen2 = (1 + (Styczen2 + interest)/1200) * kwotaGrudzien1 - principal
kwotaLuty2 = (1 + (Luty2 + interest)/1200) * kwotaStyczen2 - principal
kwotaMarzec2 = (1 + (Marzec2 + interest)/1200) * kwotaLuty2 - principal
kwotaKwiecien2 = (1 + (Kwiecien2 + interest)/1200) * kwotaMarzec2 - principal
kwotaMaj2 = (1 + (Maj2 + interest)/1200) * kwotaKwiecien2 - principal
kwotaCzerwiec2 = (1 + (Czerwiec2 + interest)/1200) * kwotaMaj2 - principal
kwotaLipiec2 = (1 + (Lipiec2 + interest)/1200) * kwotaCzerwiec2 - principal
kwotaSierpien2 = (1 + (Sierpien2 + interest)/1200) * kwotaLipiec2 - principal
kwotaWrzesien2 = (1 + (Wrzesien2 + interest)/1200) * kwotaSierpien2 - principal
kwotaPazdziernik2 = (1 + (Pazdziernik2 + interest)/1200) * kwotaWrzesien2 - principal
kwotaListopad2 = (1 + (Listopad2 + interest)/1200) * kwotaPazdziernik2 - principal
kwotaGrudzien2 = (1 + (Grudzien2 + interest)/1200) * kwotaListopad2 - principal

print("Twoja pozostała kwota kredytu to {}, to {} mniej niż w poprzednim miesiącu.".format(kwotaStyczen1, kwota0 - kwotaStyczen1))
print("Twoja pozostała kwota kredytu to {}, to {} mniej niż w poprzednim miesiącu.".format(kwotaLuty1, kwotaStyczen1 - kwotaLuty1))
print("Twoja pozostała kwota kredytu to {}, to {} mniej niż w poprzednim miesiącu.".format(kwotaMarzec1, kwotaLuty1 - kwotaMarzec1))
print("Twoja pozostała kwota kredytu to {}, to {} mniej niż w poprzednim miesiącu.".format(kwotaKwiecien1, kwotaMarzec1 - kwotaKwiecien1))
print("Twoja pozostała kwota kredytu to {}, to {} mniej niż w poprzednim miesiącu.".format(kwotaMaj1, kwotaKwiecien1 - kwotaMaj1))
print("Twoja pozostała kwota kredytu to {}, to {} mniej niż w poprzednim miesiącu.".format(kwotaCzerwiec1, kwotaMaj1 - kwotaCzerwiec1))
print("Twoja pozostała kwota kredytu to {}, to {} mniej niż w poprzednim miesiącu.".format(kwotaLipiec1, kwotaCzerwiec1 - kwotaLipiec1))
print("Twoja pozostała kwota kredytu to {}, to {} mniej niż w poprzednim miesiącu.".format(kwotaSierpien1, kwotaLipiec1 - kwotaSierpien1))
print("Twoja pozostała kwota kredytu to {}, to {} mniej niż w poprzednim miesiącu.".format(kwotaWrzesien1, kwotaSierpien1 - kwotaWrzesien1))
print("Twoja pozostała kwota kredytu to {}, to {} mniej niż w poprzednim miesiącu.".format(kwotaPazdziernik1, kwotaWrzesien1 - kwotaPazdziernik1))
print("Twoja pozostała kwota kredytu to {}, to {} mniej niż w poprzednim miesiącu.".format(kwotaListopad1, kwotaPazdziernik1 - kwotaListopad1))
print("Twoja pozostała kwota kredytu to {}, to {} mniej niż w poprzednim miesiącu.".format(kwotaGrudzien1, kwotaListopad1 - kwotaGrudzien1))

print("Twoja pozostała kwota kredytu to {}, to {} mniej niż w poprzednim miesiącu.".format(kwotaStyczen2, kwotaGrudzien1 - kwotaStyczen2))
print("Twoja pozostała kwota kredytu to {}, to {} mniej niż w poprzednim miesiącu.".format(kwotaLuty2, kwotaStyczen2 - kwotaLuty2))
print("Twoja pozostała kwota kredytu to {}, to {} mniej niż w poprzednim miesiącu.".format(kwotaMarzec2, kwotaLuty2 - kwotaMarzec2))
print("Twoja pozostała kwota kredytu to {}, to {} mniej niż w poprzednim miesiącu.".format(kwotaKwiecien2, kwotaMarzec2 - kwotaKwiecien2))
print("Twoja pozostała kwota kredytu to {}, to {} mniej niż w poprzednim miesiącu.".format(kwotaMaj2, kwotaKwiecien2 - kwotaMaj2))
print("Twoja pozostała kwota kredytu to {}, to {} mniej niż w poprzednim miesiącu.".format(kwotaCzerwiec2, kwotaMaj2 - kwotaCzerwiec2))
print("Twoja pozostała kwota kredytu to {}, to {} mniej niż w poprzednim miesiącu.".format(kwotaLipiec2, kwotaCzerwiec2 - kwotaLipiec2))
print("Twoja pozostała kwota kredytu to {}, to {} mniej niż w poprzednim miesiącu.".format(kwotaSierpien2, kwotaLipiec2 - kwotaSierpien2))
print("Twoja pozostała kwota kredytu to {}, to {} mniej niż w poprzednim miesiącu.".format(kwotaWrzesien2, kwotaSierpien2 - kwotaWrzesien2))
print("Twoja pozostała kwota kredytu to {}, to {} mniej niż w poprzednim miesiącu.".format(kwotaPazdziernik2, kwotaWrzesien2 - kwotaPazdziernik2))
print("Twoja pozostała kwota kredytu to {}, to {} mniej niż w poprzednim miesiącu.".format(kwotaListopad2, kwotaPazdziernik2 - kwotaListopad2))
print("Twoja pozostała kwota kredytu to {}, to {} mniej niż w poprzednim miesiącu.".format(kwotaGrudzien2, kwotaListopad2 - kwotaGrudzien2))
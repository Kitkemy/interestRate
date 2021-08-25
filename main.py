print("Podaj kwotę kredytu")
credit = int(input())
print("Podaj ratę")
principal = int(input())
print("Podaj oprocentowanie")
interest = int(input())

Styczen1 = 1.592824484
Luty1 = -0.453509101
Marzec1 = 2.324671717
Kwiecien1c = 1.261254407
Maj1 = 1.782526286
Czerwiec1 = 2.329384541
Lipiec1 = 1.502229842
Sierpnien1 = 1.782526286
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
Sierpnien2 = 1.577035247
Wrzesien2 = -0.07742069
Pazdziernik2 = 1.165733399
Listopad2 = -0.404186718
Grudzien2 = 1.499708521

print("********************\nKredyt na kwotę: {}".format(credit) + "\nRata: {}".format(principal) +  "\nOprocentowanie: {}".format(interest))

kwota0 = credit
kwotaStyczen1 = (1 + (Styczen1 + interest)/1200) * credit - principal
'''
kwotaLuty1 = -0.453509101
kwotaMarzec1 = 2.324671717
kwotaKwiecien1c = 1.261254407
kwotaMaj1 = 1.782526286
kwotaCzerwiec1 = 2.329384541
kwotaLipiec1 = 1.502229842
kwotaSierpnien1 = 1.782526286
kwotaWrzesien1 = 2.328848994
kwotaPazdziernik1 = 0.616921348
kwotaListopad1 = 2.352295886
kwotaGrudzien1 = 0.337779545
kwotaStyczen2 = 1.577035247
kwotaLuty2 = -0.292781443
kwotaMarzec2 = 2.48619659
kwotaKwiecien2 = 0.267110318
kwotaMaj2 = 1.417952672
kwotaCzerwiec2 = 1.054243267
kwotaLipiec2 = 1.480520104
kwotaSierpnien2 = 1.577035247
kwotaWrzesien2 = -0.07742069
kwotaPazdziernik2 = 1.165733399
kwotaListopad2 = -0.404186718
kwotaGrudzien2 = 1.499708521
'''

print("Twoja pozostała kwota kredytu to {}, to {} mniej niż w poprzednim miesiącu.".format(kwotaStyczen1, kwota0-kwotaStyczen1))
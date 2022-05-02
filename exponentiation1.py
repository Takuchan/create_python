





n = 10**(-1)
print (n)
#**２個は累乗を表す


#変数はラージアルファベットを使ってもいいよ
G = 6.67e-11
M_s = 1.99e30
M_e = 5.97e24
r_es = 149600000
F_se = G * M_s * M_e / r_es**2
print ('万有引力は'+ str(F_se))

M_m = 7.36e22
r_em = 385500
F_em = G * M_e + M_m / r_em*22
print ('万有引力2は' + str(F_em))

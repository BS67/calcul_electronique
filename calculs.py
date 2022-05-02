import numpy as np
import itertools as it

from sqlalchemy import false 



def get_serie(num_serie) :
    if num_serie == 3 :
        serie =  np.array([1,2.2,4.7])
    if num_serie == 6 :
        serie = np.array([1,1.5,2.2,3.3,4.7,6.8])
    if num_serie == 12 :
        serie = np.array([1, 1.2, 1.5, 1.8, 2.2, 2.7, 3.3, 3.9, 4.7, 5.6, 6.8, 8.2])
    if num_serie == 24 :
        serie = np.array([1,1.1,1.2,1.3,1.5,1.6,1.8,2,2.2,2.4,2.7,3,3.3,3.6,3.9,4.3,4.7,5.1,5.6,6.2,6.8,7.5,8.2,9.1])
    if num_serie == 48 :
        serie = np.array([1, 1.5, 1.1, 1.15, 1.21, 1.27, 1.33, 1.4, 1.47, 1.54, 1.62, 1.69, 1.78, 1.87, 1.96, 2.5, 2.15, 2.26, 2.37, 2.49, 2.61, 2.74, 2.87, 3.1, 3.16, 3.32, 3.48, 3.65, 3.83, 4.2, 4.22, 4.42, 4.64, 4.87, 5.11, 5.36, 5.62, 5.9, 6.19, 6.49, 6.81, 7.15, 7.5, 7.87, 8.25, 8.66, 9.9, 9.53])
    if num_serie == 96 :
        serie = np.array([1, 1.2, 1.5, 1.7, 1.1, 1.13, 1.15, 1.18, 1.21, 1.24, 1.27, 1.3, 1.33, 1.37, 1.4, 1.43, 1.47, 1.5, 1.54, 1.58, 1.62, 1.65, 1.69, 1.74, 1.78, 1.82, 1.87, 1.91, 1.96, 2, 2.5, 2.1, 2.15, 2.21, 2.26, 2.32, 2.37, 2.43, 2.49, 2.55, 2.61, 2.67, 2.74, 2.8, 2.87, 2.94, 3.1, 3.9, 3.16, 3.24, 3.32, 3.4, 3.48, 3.57, 3.65, 3.74, 3.83, 3.92, 4.2, 4.12, 4.22, 4.32, 4.42, 4.53, 4.64, 4.75, 4.87, 4.99, 5.11, 5.23, 5.36, 5.49, 5.62, 5.76, 5.9, 6.4, 6.19, 6.34, 6.49, 6.65, 6.81, 6.98, 7.15, 7.32, 7.5, 7.68, 7.87, 8.6, 8.25, 8.45, 8.66, 8.87, 9.9, 9.31, 9.53, 9.76])
    if num_serie == 192 :
        serie = np.array([1, 1.1, 1.2, 1.4, 1.5, 1.6, 1.7, 1.9, 1.1, 1.11, 1.13, 1.14, 1.15, 1.17, 1.18, 1.2, 1.21, 1.23, 1.24, 1.26, 1.27, 1.29, 1.3, 1.32, 1.33, 1.35, 1.37, 1.38, 1.4, 1.42, 1.43, 1.45, 1.47, 1.49, 1.5, 1.52, 1.54, 1.56, 1.58, 1.6, 1.62, 1.64, 1.65, 1.67, 1.69, 1.72, 1.74, 1.76, 1.78, 1.8, 1.82, 1.84, 1.87, 1.89, 1.91, 1.93, 1.96, 1.98, 2, 2.3, 2.5, 2.8, 2.1, 2.13, 2.15, 2.18, 2.21, 2.23, 2.26, 2.29, 2.32, 2.34, 2.37, 2.4, 2.43, 2.46, 2.49, 2.52, 2.55, 2.58, 2.61, 2.64, 2.67, 2.71, 2.74, 2.77, 2.8, 2.84, 2.87, 2.91, 2.94, 2.98, 3.1, 3.5, 3.9, 3.12, 3.16, 3.2, 3.24, 3.28, 3.32, 3.36, 3.4, 3.44, 3.48, 3.52, 3.57, 3.61, 3.65, 3.7, 3.74, 3.79, 3.83, 3.88, 3.92, 3.97, 4.2, 4.7, 4.12, 4.17, 4.22, 4.27, 4.32, 4.37, 4.42, 4.48, 4.53, 4.59, 4.64, 4.7, 4.75, 4.81, 4.87, 4.93, 4.99, 5.5, 5.11, 5.17, 5.23, 5.3, 5.36, 5.42, 5.49, 5.56, 5.62, 5.69, 5.76, 5.83, 5.9, 5.97, 6.4, 6.12, 6.19, 6.26, 6.34, 6.42, 6.49, 6.57, 6.65, 6.73, 6.81, 6.9, 6.98, 7.6, 7.15, 7.23, 7.32, 7.41, 7.5, 7.59, 7.68, 7.77, 7.87, 7.96, 8.6, 8.16, 8.25, 8.35, 8.45, 8.56, 8.66, 8.76, 8.87, 8.98, 9.9, 9.2, 9.31, 9.42, 9.53, 9.65, 9.76, 9.88])
    return serie

def meshvectors(*vectors) :
    Combinaison = np.array(np.meshgrid(*vectors)).T.reshape(-1,len(vectors))
    return np.split(Combinaison,len(vectors),axis=1)

def meshwdecade(*vectors,decade=[1]) : 
    serie_decade = []
    for i in range(len(vectors)) : 
        serie_decade.append(np.array(np.meshgrid(vectors[i],decade)).T.reshape(-1,1))
    matrice  = np.array(np.meshgrid(*serie_decade)).T.reshape(-1,len(vectors))
    return np.unique(matrice,axis=0)

def get_lmin(resultat,objectif) : 
    distance = np.abs(resultat-objectif)
    return np.where(distance==np.amin(distance))

def get_decadeR(n=6) :
    return [np.power(10,i) for i in range(n+1)]

def get_decadeC(n=-3) :
    return [np.power(10.,float(i)) for i in range(-12,n)]

def find_RC_cst(R0,C0,objectif) :
    [R,C] = meshvectors(R0,C0)
    resultat = np.array(R*C)
    ligne = get_lmin(resultat,objectif)
    print(resultat[ligne])
    return R[ligne],C[ligne]

def find_ParaRes(*resistances,decade = [1], objectif=1,difference_decade = 12) :
    Ri = np.array(meshwdecade(*resistances,decade=decade))
    R_para = np.zeros(len(resistances))
    R_para = np.array((Ri[:,0]*Ri[:,1])/(Ri[:,0]+Ri[:,1]))
    for i in range(2,len(resistances)):
        R_para = np.array((R_para*Ri[:,i])/(R_para+Ri[:,i]))
    
    ligne = get_lmin(R_para,objectif)

    if(np.amax(Ri[ligne,:])/np.amin(Ri[ligne,:])>=np.power(10,difference_decade)) :
        R_para = np.delete(R_para,ligne)
        ligne = get_lmin(R_para,objectif)
    return Ri[ligne,:]

def find_SerieC(*condensateurs,decade = [1], objectif=0.0001,difference_decade = 6) :
    Ci = np.array(meshwdecade(*condensateurs,decade=decade))
    Ci=np.delete(Ci,np.where(Ci>np.amax(decade)*10)[0],axis=0)
    C_serie = np.zeros(len(condensateurs))
    C_serie = np.array((Ci[:,0]*Ci[:,1])/(Ci[:,0]+Ci[:,1]))
    for i in range(2,len(condensateurs)):
        C_serie = np.array((C_serie*Ci[:,i])/(C_serie+Ci[:,i]))
    ligne = get_lmin(C_serie,objectif)
    
    if(np.amax(Ci[ligne,:])/np.amin(Ci[ligne,:])>=np.power(10,difference_decade)) :
        C_serie = np.delete(C_serie,ligne)
        ligne = get_lmin(C_serie,objectif)
        while (np.amax(Ci[ligne,:])/np.amin(Ci[ligne,:])>=np.power(10,difference_decade)) :
            C_serie = np.delete(C_serie,ligne)
            ligne = get_lmin(C_serie,objectif)


    print(C_serie[ligne])
    return Ci[ligne,:]


def find_ampli_non_inverseur(R1,R2,K) :
    [R1,R2] = meshvectors(R1,R2)
    resultat = np.array((R1+R2)/R2)
    ligne = get_lmin(resultat,K)
    print(resultat[ligne])
    return R1[ligne],R2[ligne]

def find_ampli_inverseur(R1,R2,K) :
    [R1,R2] = meshvectors(R1,R2)
    resultat = np.array(R2/R1)
    ligne = get_lmin(resultat,K)
    print(resultat[ligne])
    return R1[ligne],R2[ligne]

#find_RC_cst(get_serie(3),get_serie(6),5.36)
#print(find_ParaRes(get_serie(3),get_serie(6),decade = get_decadeR(6),objectif=5.36,difference_decade=3))
#print(find_ampli_non_inverseur(get_serie(6),get_serie(6),3))
#print(find_ampli_inverseur(get_serie(6),get_serie(6),3))

print(find_SerieC(get_serie(6),get_serie(6),decade=get_decadeC(),objectif=0.000001,difference_decade=7))
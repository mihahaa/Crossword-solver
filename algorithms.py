import copy

class Algorithm:
    def get_algorithm_steps(self, tiles, variables, words):
        pass

class ExampleAlgorithm(Algorithm):

    def get_algorithm_steps(self, tiles, variables, words):
        moves_list = [['0h', 0], ['0v', 2], ['1v', 1], ['2h', 1], ['4h', None],
                 ['2h', None], ['1v', None], ['0v', 3], ['1v', 1], ['2h', 1],
                 ['4h', 4], ['5v', 5]]
        domains = {var: [word for word in words] for var in variables}
        solution = []
        for move in moves_list:
            solution.append([move[0], move[1], domains])
        return solution

class Backtracking(Algorithm):
    def get_algorithm_steps(self, tiles, variables, words):
        domains = {var: [word for word in words] for var in variables}
        my_domains=copy.deepcopy(domains)
        for key in domains:
            for rec in domains[key]:
                if len(rec)!=variables[key]:
                    my_domains[key].remove(rec)
        koordinats={}
        karakters=list()
        kolkos=list()
        for a in domains:
            b=str(a)
            temp=b[0:(len(b)-1)]
            c=int(temp)
            k1=int(c/(len(tiles[0])))
            k2=c%(len(tiles[0]))
            temp=list()
            temp.append(k1)
            temp.append(k2)
            koordinats[a]=temp
        for a in tiles:
            temp=list()
            temp2=list()
            for b in a:
                if b:
                    temp.append('.')
                else:
                    temp.append('/')
                temp2.append(0)
            karakters.append(temp)
            kolkos.append(temp2)
        solution=[]
        def backtrack(lvl,sol,dom):
            bio=1
            if(lvl==len(variables)):
                 return True
            i=0
            for key in variables:
                if i==lvl:
                    v=key
                    break
                i=i+1
            q=0
            for val in dom[v]:
                temp=str(val)
                if variables[v]!=len(temp):
                    q=q+1
                    continue
                k1=koordinats[v][0]
                k2=koordinats[v][1]
                zemo=0
                if v[len(v)-1:len(v)]=='h':
                    for i in range(variables[v]):
                        k1t=k1
                        k2t=k2+i
                        if(karakters[k1t][k2t]!='/' and karakters[k1t][k2t]!=val[i]):
                            zemo=1
                            break
                else:
                    for i in range(variables[v]):
                        k1t=k1+i
                        k2t=k2
                        if(karakters[k1t][k2t]!='/' and karakters[k1t][k2t]!=val[i]):
                            zemo=1
                            break
                if zemo==0:
                    bio=1
                    if v[len(v)-1:len(v)]=='h':
                        for i in range(variables[v]):
                            k1t=k1
                            k2t=k2+i
                            karakters[k1t][k2t]=val[i]
                            kolkos[k1t][k2t]=kolkos[k1t][k2t]+1
                    else:
                        for i in range(variables[v]):
                            k1t=k1+i
                            k2t=k2
                            karakters[k1t][k2t]=val[i]
                            kolkos[k1t][k2t]=kolkos[k1t][k2t]+1
                    daj=list()
                    daj.append(v)
                    daj.append(q)
                    daj.append(dom)
                    sol.append(daj)
                    if backtrack(lvl+1,sol,dom):
                        return True
                    
                    if v[len(v)-1:len(v)]=='h':
                        for i in range(variables[v]):
                            k1t=k1
                            k2t=k2+i
                            kolkos[k1t][k2t]=kolkos[k1t][k2t]-1
                            if kolkos[k1t][k2t]==0:
                                karakters[k1t][k2t]='/'
                    else:
                        for i in range(variables[v]):
                            k1t=k1+i
                            k2t=k2
                            kolkos[k1t][k2t]=kolkos[k1t][k2t]-1
                            if kolkos[k1t][k2t]==0:
                                karakters[k1t][k2t]='/'
                q=q+1
            if bio!=0:
                daj=list()
                daj.append(v)
                daj.append(None)
                daj.append(dom)
                sol.append(daj)
            return False
        level=0
        backtrack(level,solution,my_domains)
        return solution


class ForwardChecking(Algorithm):
    def get_algorithm_steps(self, tiles, variables, words):
        domains = {var: [word for word in words] for var in variables}
        my_domains=copy.deepcopy(domains)
        indekss={}
        madaj=0
        for key in variables:
            indekss[key]=madaj
            madaj=madaj+1
        for key in domains:
            for rec in domains[key]:
                if len(rec)!=variables[key]:
                    my_domains[key].remove(rec)
        koordinats={}
        karakters=list()
        kolkos=list()
        for a in domains:
            b=str(a)
            temp=b[0:(len(b)-1)]
            c=int(temp)
            k1=int(c/(len(tiles[0])))
            k2=c%(len(tiles[0]))
            temp=list()
            temp.append(k1)
            temp.append(k2)
            koordinats[a]=temp
        for a in tiles:
            temp=list()
            temp2=list()
            for b in a:
                if b:
                    temp.append('.')
                else:
                    temp.append('/')
                temp2.append(0)
            karakters.append(temp)
            kolkos.append(temp2)
        solution=[]
        ogranicenjas={}
        for a in variables:
            ogranicenjas[a]=list()
            for b in variables:
                if a!=b:
                    if a[len(a)-1:len(a)]=='h':
                        if b[len(b)-1:len(b)]=='v':
                            if koordinats[a][1]+variables[a]>koordinats[b][1] and koordinats[a][1]<=koordinats[b][1] and koordinats[b][0]+variables[b]>koordinats[a][0] and koordinats[b][0]<=koordinats[a][0]:
                                if indekss[a]<indekss[b]:
                                    ogranicenjas[a].append(b)
                    if a[len(a)-1:len(a)]=='v':
                        if b[len(b)-1:len(b)]=='h':
                            if koordinats[b][1]+variables[b]>koordinats[a][1] and koordinats[b][1]<=koordinats[a][1] and koordinats[a][0]+variables[a]>koordinats[b][0] and koordinats[a][0]<=koordinats[b][0]:
                                if indekss[a]<indekss[b]:
                                    ogranicenjas[a].append(b)         
        def backtrack(lvl,sol,dom):
            bio=1
            if(lvl==len(variables)):
                 return True
            i=0
            for key in variables:
                if i==lvl:
                    v=key
                    break
                i=i+1
            q=0
            for val in dom[v]:
                temp=str(val)
                if variables[v]!=len(temp):
                    q=q+1
                    continue
                k1=koordinats[v][0]
                k2=koordinats[v][1]
                zemo=0
                if v[len(v)-1:len(v)]=='h':
                    for i in range(variables[v]):
                        k1t=k1
                        k2t=k2+i
                        if(karakters[k1t][k2t]!='/' and karakters[k1t][k2t]!=val[i]):
                            zemo=1
                            break
                else:
                    for i in range(variables[v]):
                        k1t=k1+i
                        k2t=k2
                        if(karakters[k1t][k2t]!='/' and karakters[k1t][k2t]!=val[i]):
                            zemo=1
                            break
                if zemo==0:
                    bio=1
                    upao=0
                    new_dom=copy.deepcopy(dom)
                    if v[len(v)-1:len(v)]=='h':
                        for dajmi in ogranicenjas[v]:
                            for reci in dom[dajmi]:
                                if reci[k1-koordinats[dajmi][0]]!=val[koordinats[dajmi][1]-k2]:
                                    new_dom[dajmi].remove(reci)
                            if len(new_dom[dajmi])==0:
                                upao=1
                        if upao==0:
                            for i in range(variables[v]):
                                k1t=k1
                                k2t=k2+i
                                karakters[k1t][k2t]=val[i]
                                kolkos[k1t][k2t]=kolkos[k1t][k2t]+1
                    else:
                        for dajmi in ogranicenjas[v]:
                            for reci in dom[dajmi]:
                                if reci[k2-koordinats[dajmi][1]]!=val[koordinats[dajmi][0]-k1]:
                                    new_dom[dajmi].remove(reci)
                            if len(new_dom[dajmi])==0:
                                upao=1
                        if upao==0:
                            for i in range(variables[v]):
                                k1t=k1+i
                                k2t=k2
                                karakters[k1t][k2t]=val[i]
                                kolkos[k1t][k2t]=kolkos[k1t][k2t]+1
                    daj=list()
                    daj.append(v)
                    daj.append(q)
                    daj.append(new_dom)
                    sol.append(daj)
                    if upao==1:
                        q=q+1
                        continue

                    if backtrack(lvl+1,sol,new_dom):
                        return True
                    if v[len(v)-1:len(v)]=='h':
                        for i in range(variables[v]):
                            k1t=k1
                            k2t=k2+i
                            kolkos[k1t][k2t]=kolkos[k1t][k2t]-1
                            if kolkos[k1t][k2t]==0:
                                karakters[k1t][k2t]='/'
                    else:
                        for i in range(variables[v]):
                            k1t=k1+i
                            k2t=k2
                            kolkos[k1t][k2t]=kolkos[k1t][k2t]-1
                            if kolkos[k1t][k2t]==0:
                                karakters[k1t][k2t]='/'
                q=q+1
            if bio!=0:
                daj=list()
                daj.append(v)
                daj.append(None)
                daj.append(dom)
                sol.append(daj)
            return False
        level=0
        backtrack(level,solution,my_domains)
        return solution

class ArcConsistencying(Algorithm):
    def get_algorithm_steps(self, tiles, variables, words):
        domains = {var: [word for word in words] for var in variables}
        my_domains=copy.deepcopy(domains)
        indekss={}
        madaj=0
        for key in variables:
            indekss[key]=madaj
            madaj=madaj+1
        for key in domains:
            for rec in domains[key]:
                if len(rec)!=variables[key]:
                    my_domains[key].remove(rec)
        koordinats={}
        karakters=list()
        kolkos=list()
        for a in domains:
            b=str(a)
            temp=b[0:(len(b)-1)]
            c=int(temp)
            k1=int(c/(len(tiles[0])))
            k2=c%(len(tiles[0]))
            temp=list()
            temp.append(k1)
            temp.append(k2)
            koordinats[a]=temp
        for a in tiles:
            temp=list()
            temp2=list()
            for b in a:
                if b:
                    temp.append('.')
                else:
                    temp.append('/')
                temp2.append(0)
            karakters.append(temp)
            kolkos.append(temp2)
        solution=[]
        ogranicenjas={}
        svaogranicenjas={}
        for a in variables:
            ogranicenjas[a]=list()
            for b in variables:
                if a!=b:
                    if a[len(a)-1:len(a)]=='h':
                        if b[len(b)-1:len(b)]=='v':
                            if koordinats[a][1]+variables[a]>koordinats[b][1] and koordinats[a][1]<=koordinats[b][1] and koordinats[b][0]+variables[b]>koordinats[a][0] and koordinats[b][0]<=koordinats[a][0]:
                                if indekss[a]<indekss[b]:
                                    ogranicenjas[a].append(b)
                    if a[len(a)-1:len(a)]=='v':
                        if b[len(b)-1:len(b)]=='h':
                            if koordinats[b][1]+variables[b]>koordinats[a][1] and koordinats[b][1]<=koordinats[a][1] and koordinats[a][0]+variables[a]>koordinats[b][0] and koordinats[a][0]<=koordinats[b][0]:
                                if indekss[a]<indekss[b]:
                                    ogranicenjas[a].append(b)  
        for a in variables:
            svaogranicenjas[a]=list()
            for b in variables:
                if a!=b:
                    if a[len(a)-1:len(a)]=='h':
                        if b[len(b)-1:len(b)]=='v':
                            if koordinats[a][1]+variables[a]>koordinats[b][1] and koordinats[a][1]<=koordinats[b][1] and koordinats[b][0]+variables[b]>koordinats[a][0] and koordinats[b][0]<=koordinats[a][0]:
                                    svaogranicenjas[a].append(b)
                    if a[len(a)-1:len(a)]=='v':
                        if b[len(b)-1:len(b)]=='h':
                            if koordinats[b][1]+variables[b]>koordinats[a][1] and koordinats[b][1]<=koordinats[a][1] and koordinats[a][0]+variables[a]>koordinats[b][0] and koordinats[a][0]<=koordinats[b][0]:
                                    svaogranicenjas[a].append(b)     

        def backtrack(lvl,sol,dom):
            bio=1
            if(lvl==len(variables)):
                 return True
            i=0
            for key in variables:
                if i==lvl:
                    v=key
                    break
                i=i+1
            q=0
            for val in dom[v]:
                temp=str(val)
                if variables[v]!=len(temp):
                    q=q+1
                    continue
                k1=koordinats[v][0]
                k2=koordinats[v][1]
                zemo=0
                if v[len(v)-1:len(v)]=='h':
                    for i in range(variables[v]):
                        k1t=k1
                        k2t=k2+i
                        if(karakters[k1t][k2t]!='/' and karakters[k1t][k2t]!=val[i]):
                            zemo=1
                            break
                else:
                    for i in range(variables[v]):
                        k1t=k1+i
                        k2t=k2
                        if(karakters[k1t][k2t]!='/' and karakters[k1t][k2t]!=val[i]):
                            zemo=1
                            break
                if zemo==0:
                    bio=1
                    upao=0
                    new_dom=copy.deepcopy(dom)
                    if v[len(v)-1:len(v)]=='h':
                        for dajmi in ogranicenjas[v]:
                            for reci in dom[dajmi]:
                                if reci[k1-koordinats[dajmi][0]]!=val[koordinats[dajmi][1]-k2]:
                                    new_dom[dajmi].remove(reci)
                            if len(new_dom[dajmi])==0:
                                upao=1
                    else:
                        for dajmi in ogranicenjas[v]:
                            for reci in dom[dajmi]:
                                if reci[k2-koordinats[dajmi][1]]!=val[koordinats[dajmi][0]-k1]:
                                    new_dom[dajmi].remove(reci)
                            if len(new_dom[dajmi])==0:
                                upao=1
                    if upao==1:
                        daj=list()
                        daj.append(v)
                        daj.append(q)
                        daj.append(new_dom)
                        sol.append(daj) 
                        q=q+1
                        continue
                    kolkoih=0
                    while(kolkoih==0):
                        kolkoih=1
                        new_domac=copy.deepcopy(new_dom)
                        domac=copy.deepcopy(new_dom)
                        for kac in domac:
                            nemojto=0
                            for reciac in domac[kac]:
                                if indekss[kac]<=lvl:
                                    nemojto=1
                                    break
                                for sac in svaogranicenjas[kac]:
                                    nemojto1=0
                                    for ureciac in domac[sac]:
                                        if indekss[sac]<=lvl:
                                            nemojto1=1
                                            break
                                        kolkoih=0
                                        if kac[len(kac)-1:len(kac)]=='h':
                                            if reciac[koordinats[sac][1]-koordinats[kac][1]]==ureciac[koordinats[kac][0]-koordinats[sac][0]]:
                                                kolkoih=1
                                                break
                                        else:
                                            if reciac[koordinats[sac][0]-koordinats[kac][0]]==ureciac[koordinats[kac][1]-koordinats[sac][1]]:
                                                kolkoih=1
                                                break
                                    if nemojto1==1:
                                        continue
                                    if kolkoih==0:
                                        break
                                if kolkoih==0:
                                    new_domac[kac].remove(reciac)
                                    break
                            if nemojto==1:
                                continue
                            if kolkoih==0:
                                break
                        new_dom=copy.deepcopy(new_domac)
                    mojneki=copy.deepcopy(new_dom)
                    for xyz in mojneki:
                        if len(mojneki[xyz])==0:
                            upao=1
                            break
                    daj=list()
                    daj.append(v)
                    daj.append(q)
                    daj.append(mojneki)
                    sol.append(daj)
                    if upao==1: 
                        q=q+1
                        continue
                    else:
                        if v[len(v)-1:len(v)]=='h':
                            for i in range(variables[v]):
                                k1t=k1
                                k2t=k2+i
                                karakters[k1t][k2t]=val[i]
                                kolkos[k1t][k2t]=kolkos[k1t][k2t]+1
                        else:
                            for i in range(variables[v]):
                                k1t=k1+i
                                k2t=k2
                                karakters[k1t][k2t]=val[i]
                                kolkos[k1t][k2t]=kolkos[k1t][k2t]+1
                    if backtrack(lvl+1,sol,mojneki):
                        return True
                    if v[len(v)-1:len(v)]=='h':
                        for i in range(variables[v]):
                            k1t=k1
                            k2t=k2+i
                            kolkos[k1t][k2t]=kolkos[k1t][k2t]-1
                            if kolkos[k1t][k2t]==0:
                                karakters[k1t][k2t]='/'
                    else:
                        for i in range(variables[v]):
                            k1t=k1+i
                            k2t=k2
                            kolkos[k1t][k2t]=kolkos[k1t][k2t]-1
                            if kolkos[k1t][k2t]==0:
                                karakters[k1t][k2t]='/'
                q=q+1
            if bio!=0:
                daj=list()
                daj.append(v)
                daj.append(None)
                daj.append(dom)
                sol.append(daj)
            return False
        level=0
        backtrack(level,solution,my_domains)
        return solution
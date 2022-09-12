
class Scheduling_Algo:
    # process = []
    def __init__(self):
        self.process = []
        self.time_slice = 0
        self.nprocess = 0

    def input(self):
        self.nprocess = int(input("Enter number of processes: "))
        for i in range(self.nprocess):
            at, bt, p = map(int,
                            input("Enter arrival time and burst time and priority for the process:a b p: ").split())
            lst = [at, bt, p, i]
            # print(lst)
            self.process.append(lst)
            # print(self.process)
        self.time_slice = int(input("Enter times slice for round robin algo: "))

        # for i in range(self.nprocess):
        #     self.proc.append([[0]*4])

    def display(self):
        # print(self.process)
        for i in range(self.nprocess):
            print(self.process[i][1], self.process[i][2])

    def fcfs(self, ca = 0):
        tmp = self.process.copy()
        tmp.sort()
        ct = [0] * self.nprocess
        tat = [0] * self.nprocess
        wt = [0] * self.nprocess

        tot_tat = 0
        tot_wt = 0
        t = 0
        for i in range(self.nprocess):
            id = tmp[i][3]
            if (i == 0):
                t = tmp[i][0] + tmp[i][1]
            else:
                if (t >= tmp[i][0]):
                    t += tmp[i][1]
                else:
                    t += tmp[i][0] + tmp[i][1]

            ct[id] = t
            tat[id] = ct[id] - self.process[id][0]
            wt[id] = tat[id] - self.process[id][1]

            tot_tat += tat[id]
            tot_wt += wt[id]

        avg_tat = tot_tat / self.nprocess
        avg_wt = tot_wt / self.nprocess
        # print(ct)
        if(ca == 1):
            return avg_tat, avg_wt
        Scheduling_Algo.ga(self.process, tat, wt, avg_tat, avg_wt)

    def sjf(self,ca = 0):
        tmp = self.process.copy()
        tmp.sort()
        # print(tmp)
        complete = 0
        ct = [0] * self.nprocess
        tat = [0] * self.nprocess
        wt = [0] * self.nprocess
        t = 0

        btleft = [0]*self.nprocess
        # print(self.process)
        for i in range(self.nprocess):
            btleft[i] = self.process[i][1]

        tot_tat = 0
        tot_wt = 0

        i = 0
        pendinglst = []
        pendinglst.append(tmp[0])
        t += tmp[0][0]
        i+=1
        while (complete != self.nprocess):
            t += 1
            # print(i, t)
            if (len(pendinglst) == 1):
                id = pendinglst[0][3]
                btleft[id] -= 1
                if (btleft[id] == 0):
                    ct[id] = t
                    complete += 1
                    tat[id] = ct[id] - self.process[id][0]
                    wt[id] = tat[id] - self.process[id][1]
                    tot_tat += tat[id]
                    tot_wt += wt[id]
                    del pendinglst[0]

            else:
                leastbt, leastid = 99999999, 99999999
                for j in pendinglst:
                    id = j[3]
                    if (leastbt > btleft[id]):
                        leastbt = btleft[id]
                        leastid = id

                btleft[leastid] -= 1
                if (btleft[leastid] == 0):
                    ct[leastid] = t
                    complete += 1
                    tat[leastid] = ct[leastid] - self.process[leastid][0]
                    wt[leastid] = tat[leastid] - self.process[leastid][1]
                    tot_tat += tat[leastid]
                    tot_wt += wt[leastid]

                    for k in range(len(pendinglst)):
                        if pendinglst[k][3] == leastid:
                            del pendinglst[k]
                            break

            while(i < self.nprocess and tmp[i][0] <= t):
                # print(tmp[i][0], tmp[i][3])
                pendinglst.append(tmp[i])
                i+=1

        avg_tat = tot_tat / self.nprocess
        avg_wt = tot_wt / self.nprocess
        # print(ct)
        if ca == 1:
            return avg_tat, avg_wt
        Scheduling_Algo.ga(self.process, tat, wt, avg_tat, avg_wt)

    def rr(self, ca = 0):
        q = self.process.copy()
        q.sort()
        # print(q)
        # print(self.process)
        ct = [0] * self.nprocess
        tat = [0] * self.nprocess
        wt = [0] * self.nprocess
        btleft = []
        for i in range(self.nprocess):
            btleft.append(self.process[i][1])

        t = 0
        tot_tat = 0
        tot_wt = 0
        i = 0
        complete = 0
        while complete != self.nprocess:
            front = q[i]
            id = front[3]
            if(btleft[id] == 0):
                i = (i+1)%self.nprocess

            if (btleft[id] > self.time_slice):
                btleft[id] -= self.time_slice
                t += self.time_slice
                i = (i+1)%self.nprocess

            elif btleft[id] == self.time_slice:
                t += self.time_slice
                btleft[id] -= self.time_slice
                ct[id] = t
                tat[id] = ct[id] - self.process[id][0]
                tot_tat += tat[id]
                wt[id] = tat[id] - self.process[id][1]
                tot_wt += wt[id]
                complete += 1
                i = (i+1)%self.nprocess

            else:
                t += btleft[id]
                # front[1] = 0
                ct[id] = t
                tat[id] = ct[id] - self.process[id][0]
                tot_tat += tat[id]
                wt[id] = tat[id] - self.process[id][1]
                tot_wt += wt[id]
                complete +=1
                i = (i+1)%self.nprocess

        # print(self.process)

        avg_tat = tot_tat / self.nprocess
        avg_wt = tot_wt / self.nprocess
        if(ca == 1):
            return avg_tat, avg_wt
        Scheduling_Algo.ga(self.process, tat, wt, avg_tat, avg_wt)


    def priority(self, ca = 0):
        accprior = []
        for i in self.process:
            accprior.append([i[0], i[2], i[3], i[1]])  # at, prior, id, bt

        accprior.sort()
        ct = [0] * self.nprocess
        tat = [0] * self.nprocess
        wt = [0] * self.nprocess

        sum, tot_tat, tot_wt = 0, 0, 0
        complete = 0
        i = 0
        t = 0
        pendinglst = []

        while(complete != self.nprocess):
            if(len(pendinglst) == 0):
                if(i < self.nprocess):
                    t += accprior[i][0] + accprior[0][3]
                    id =accprior[i][2]
                    ct[id] = t
                    tat[id] = ct[id] - accprior[i][0]
                    wt[id] = tat[id] - accprior[i][3]
                    tot_tat += tat[id]
                    tot_wt += wt[id]
                    i+=1
                    complete+=1

            elif(len(pendinglst) == 1):
                if(t >= pendinglst[0][0]):
                    t += pendinglst[0][3]
                else:
                    t += pendinglst[0][0] + pendinglst[0][3]

                id = pendinglst[0][2]
                ct[id] = t
                tat[id] = ct[id] -  self.process[id][0]
                wt[id] = tat[id] - self.process[id][1]
                tot_tat +=tat[id]
                tot_wt += wt[id]

                del pendinglst[0]

                complete +=1


            else:
                leastprior, leastid = 99999999,999999999
                for j in pendinglst:
                    id = j[2]
                    prior = j[1]
                    if(leastprior > prior):
                        leastprior = prior
                        leastid = id

                complete += 1

                for k in range(len(pendinglst)):
                    id = pendinglst[k][2]
                    if(id == leastid):
                        t += pendinglst[k][3]
                        ct[id] = t
                        tat[id] = ct[id] - self.process[id][0]
                        wt[id] = ct[id] - self.process[id][1]
                        tot_tat += tat[id]
                        tot_wt += wt[id]
                        del pendinglst[k]
                        break

            while(i < self.nprocess and accprior[i][0] <= t):
                pendinglst.append(accprior[i])
                i+=1



        avg_tat = tot_tat / self.nprocess
        avg_wt = tot_wt / self.nprocess
        # print(ct)
        if ca == 1:
            return avg_tat, avg_wt
        Scheduling_Algo.ga(self.process, tat, wt, avg_tat, avg_wt)


    @staticmethod
    def ga(process, tat, wt, avg_tat, avg_wt):
        print("\nP_id\tAT\tBT\tTAT\tWT")
        proc = []
        # for i in Scheduling_Algo.process:
        for i in process:
            proc.append([i[3], i[0], i[1], i[2]])  # id, at, bt, prio

        proc.sort()

        # for i in proc:
        #     print(i)

        for i in proc:
            # print(i[0],"\t",i[1], "\t", i[2], "\t", i[3], "\t", tat[i], "\t", wt[i])
            print(i[0], end="\t")
            print(i[1], end="\t")
            print(i[2], end="\t")
            print(tat[i[0]], end="\t")
            print(wt[i[0]])

        print("Average TAT =", avg_tat)
        print("Average WT =", avg_wt)

    def completeAnalysis(self):
        print("\nAlgos\tAvg TAT\tAvg WT")
        lst = []

        t1,w1 = self.fcfs(ca = 1)
        t2, w2 = self.sjf(ca=1)
        t3, w3 = self.rr(ca=1)
        t4, w4 = self.priority(ca=1)
        lst.append(["FCFS", t1, w1])
        lst.append(["SJF.", t2, w2])
        lst.append(["R.R.", t3, w3])
        lst.append(["PRIO", t4, w4])

        leastTAT = min([t1,t2,t3,t4])
        leastWT = min([w1,w2,w3,w4])

        leastTATAlgo = ""
        leastWTAlgo = ""

        for i in range(4):
            for j in range(3):
                if(j == 1):
                    print(lst[i][j], end="\t\t")
                    if(leastTAT == lst[i][j]):
                        leastTATAlgo = lst[i][0]
                else:
                    print(lst[i][j], end="\t")

                if(j == 2):
                    if(leastWT == lst[i][j]):
                        leastWTAlgo = lst[i][0]
            print("")


        print("According to AvgTAT, " + leastTATAlgo + " is best for given process with having Avg TAT =", leastTAT)
        print("According to AvgWT, " + leastWTAlgo + " is best for given process with having Avg WT =", leastWT)





algo = Scheduling_Algo()
algo.input()
algo.fcfs()
algo.sjf()
algo.rr()
algo.priority()
algo.completeAnalysis()



'''
5
0 3 3
1 6 4
3 1 9
2 2 7
4 4 8
2
'''

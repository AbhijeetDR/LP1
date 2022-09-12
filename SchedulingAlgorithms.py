from calendar import leapdays


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

    def fcfs(self):
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
        Scheduling_Algo.ga(self.process, tat, wt, avg_tat, avg_wt)

        # return avg_tat, avg_wt

    def sjf(self):
        tmp = self.process.copy()
        tmp.sort()
        print(tmp)
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
                    tot_tat = tat[id]
                    tot_wt = wt[id]
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
        Scheduling_Algo.ga(self.process, tat, wt, avg_tat, avg_wt)

    def rr(self):
        q = self.process.copy()
        q.sort()
        # print(q)
        ct = [0 for i in range(self.nprocess)]
        tat = [0] * self.nprocess
        wt = [0] * self.nprocess

        t = 0
        while len(q) != 0:
            front = q.pop(0)
            if (front[1] > self.time_slice):
                front[1] -= self.time_slice
                t += self.time_slice
                q.append(front)
            elif front[1] == self.time_slice:
                t += self.time_slice
                ct[front[3]] = t
            else:
                t += front[1]
                front[1] = 0
                ct[front[3]] = t

        tot_tat = 0
        tot_wt = 0

        for i in range(self.nprocess):
            tat[i] = ct[i] - self.process[i][0]
            wt[i] = ct[i] - self.process[i][0] - self.process[i][1]
            tot_tat += tat[i]
            tot_wt += wt[i]

        avg_tat = tot_tat / self.nprocess
        avg_wt = tot_wt / self.nprocess
        Scheduling_Algo.ga(self.process, tat, wt, avg_tat, avg_wt)
        # return avg_tat, avg_wt

    def priority(self):
        accprior = []
        for i in self.process:
            accprior.append([i[0], i[2], i[3], i[1]])  # at, prior, id, bt

        accprior.sort()
        ct = [0] * self.nprocess
        tat = [0] * self.nprocess
        wt = [0] * self.nprocess

        sum, tot_tat, tot_wt = 0, 0, 0

        for i in accprior:
            id = i[2]
            sum = ct[id] = sum + i[3]
            tat[id] = ct[id] - i[0]
            wt[id] = tat[id] - i[3]

            tot_wt += wt[id]
            tot_tat += tat[id]

        avg_tat = tot_tat / self.nprocess
        avg_wt = tot_wt / self.nprocess

        # return avg_tat, avg_wt
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


algo = Scheduling_Algo()
algo.input()
# algo.fcfs()
algo.sjf()
# algo.rr()
# algo.priority()
# algo.priority()


# process no-> 1 2 3 4 5
# arrival time-> 0 1 3 2 4
# burst time-> 3 6 1 2 4
# priority-> 3 4 9 7 8

# Enter arrival time and burst time and priority for the process:a b p: 0 5 1
# Enter arrival time and burst time and priority for the process:a b p: 1 3 2
# Enter arrival time and burst time and priority for the process:a b p: 2 1 3
# Enter arrival time and burst time and priority for the process:a b p: 3 2 4
# Enter arrival time and burst time and priority for the process:a b p: 4 3 5
# Enter times slice for round robin algo: 2

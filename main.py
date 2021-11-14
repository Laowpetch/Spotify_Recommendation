import pandas as pd

class Song:
    def __init__(self,Name,ENE,PC1,PC2,PC3):
        self.name = Name
        self.Data = [int(ENE),float(PC1),float(PC2),float(PC3)]

def Pearson(li1,li2):
    x = list(li1)
    y = list(li2)
    mX = sum(x)/len(x)
    mY = sum(y)/len(y)
    cov = sum((a - mX) * (b - mY) for (a,b) in zip(x,y)) / len(x)
    stdevX = (sum((a - mX)**2 for a in x)/len(x))**0.5
    stdevY = (sum((b - mY)**2 for b in y)/len(y))**0.5
    return round(cov/(stdevX*stdevY),8)
    
df = pd.read_excel(r'D:\\Work\\Python\\Linear\\Data.xlsx')
nump = df.to_numpy()
Song_ = []
Name = []
Pearson_ = []
Pearson_2 = []
Max = []
DisplayPearson = []
for i in range(0,len(nump)):
    Song_.append(Song(nump[i][0],nump[i][1],nump[i][2],nump[i][3],nump[i][4]))
    Name.append(nump[i][0])

if __name__ == '__main__':
    inp = input('Song Name : ')
    if inp in Name:
        ind = Name.index(inp)
        if Song_[ind].Data[0] < 73:
            slow = True
        else:
            slow = False
        if slow:
            for i in range(0,len(nump)):
                if Song_[i].Data[0] < 73 and Song_[i].name != inp:
                    Pearson_.append(Pearson(Song_[ind].Data[1:],Song_[i].Data[1:]))
                    Pearson_2.append(Pearson(Song_[ind].Data[1:],Song_[i].Data[1:]))
                else:
                    Pearson_.append(-1)
                    Pearson_2.append(-1)
        else:
            for i in range(0,len(nump)):
                if Song_[i].Data[0] > 72 and Song_[i].name != inp:
                    Pearson_.append(Pearson(Song_[ind].Data[1:],Song_[i].Data[1:]))
                    Pearson_2.append(Pearson(Song_[ind].Data[1:],Song_[i].Data[1:]))
                else:
                    Pearson_.append(-1)
                    Pearson_2.append(-1)
        
        Pearson_.sort(reverse=True)
        print('---------Recommend---------')
        for i in range(0,3):
            Max.append(Pearson_2.index(Pearson_[i]))
            Pearson_2[Pearson_2.index(Pearson_[i])] = -1
            if Pearson_[i] > 0:
                print(Song_[Max[i]].name,'Pearsonsimilarity =',Pearson_[i])               
    else:
        print('Invalid input')
class Solution:
    def spiralOrder(self, mat: List[List[int]]) -> List[int]:
        i,j=0,0
        d={}
        k=1
        c=len(mat)
        r=len(mat[0])
        ans=[]
        while True:
            d[(i,j)]=1
            ans.append(mat[i][j])
            if k%4==1:
                if j+1<r and (i,j+1) not in d:
                    j+=1
                else:
                    i+=1
                    k+=1
            elif k%4==2:
                if i+1<c and (i+1,j) not in d:
                    i+=1
                else:
                    j-=1
                    k+=1
            elif k%4==3:
                if j-1>=0 and (i,j-1) not in d:
                    j-=1
                else:
                    i-=1
                    k+=1
            else:
                if i-1>=0 and (i-1,j) not in d:
                    i-=1
                else:
                    j+=1
                    k+=1
            if (i,j) in d:
                break
        return ans


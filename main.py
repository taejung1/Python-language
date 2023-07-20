공, 바구니 = map(int, input().split(" "));
























"""
Input , Input_2 = map(int , input().split(" ")); # N K 
String = list(input());

Temp = 0
for i in range(Input) :
    if String[i] == 'P' :
        for j in range(max(i-Input_2, 0) , min(i + Input_2 + 1 , Input)) :
            if String[j] == 'H':
                String[j] = '0';
                Temp+=1;
                break;
print(Temp)
"""

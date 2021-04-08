def function(N,card_list):
    alice_s = 0
    bob_s = 0
    while(1):
        max_v_index = card_list.index(max(card_list))
        alice_s += card_list[max_v_index]
        card_list.pop(max_v_index)

        if len(card_list) == 0:
            break

        max_v_index = card_list.index(max(card_list))
        bob_s += card_list[max_v_index]
        card_list.pop(max_v_index)

        if len(card_list) == 0:
            break

    rslt = alice_s - bob_s 
    
    return rslt




N = int(input())
tmp = input()
tmp2 = tmp.split()
card_list = []
[ card_list.append(int(tmp2[i])) for i in range(0,len(tmp2))]

ans = function(N,card_list)
print(ans)
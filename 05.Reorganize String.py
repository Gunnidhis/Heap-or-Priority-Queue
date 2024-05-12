 # question: Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.

 #           Return any possible rearrangement of s or return "" if not possible.

def reOrganizeString(s):
    max_heap = list()
    d = dict()

    for i in range(len(s)):
        curr = s[i]
        if curr not in d:
            d[curr] = 0
        d[curr] += 1

    for key,value in d.items():
        heappush(max_heap,[-value,key])

    res = ""
    prev_char = None
    prev_freq = 0
    while max_heap:
        v,k = heappop(max_heap)
        v *= -1
        curr_char = k
        curr_freq = v
        res += k
        if prev_freq > 0 :
            heappush(max_heap,[-prev_freq,prev_char])
        prev_char = curr_char
        prev_freq = curr_freq - 1

    if len(res) == len(s):
        return res
    return ""

if __name__=="__main__":
  s = "aab"
  ans = reOrganizeString(s)
  print(ans)

#output : aba

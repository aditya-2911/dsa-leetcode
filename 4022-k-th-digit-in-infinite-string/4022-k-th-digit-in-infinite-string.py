class Solution:
    def kthDigit(self, k: int) -> int:
        k=k-1

        if k<9:
            b=0
            return 1+k

        k=k-9
        d=2

        while True:
            total_digits_in_d= (9*(10**(d-2)))*(10*d)

            if k<total_digits_in_d:
                break
            k-=total_digits_in_d

            d+=1

        curr_b=(10**(d-2))+ (k//(10*d))

        rem=k%(10*d)

        num_idx=rem//d

        idx=rem%d

        if curr_b%2==0:
            num=10*curr_b+num_idx
        else:
            num=10*curr_b+9-num_idx

        ans=str(num)

        return int(ans[idx])
        
        

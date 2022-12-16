class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        li = [i for i in range(1,n+1)]
        out_li = []
        for i in li:
            if i%3==0 and i%5==0:
                out_li.append('FizzBuzz')
            elif i%3==0:
                out_li.append('Fizz')
            elif i%5==0:
                out_li.append('Buzz')
            else:
                out_li.append(str(i))
        return out_li

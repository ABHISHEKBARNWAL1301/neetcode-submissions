class Solution:
    def validPalindrome(self, s: str) -> bool:
        

        def try_left():
            l, r = 0, len(s) - 1
            delete  = False
            while l<r:
                if s[l] != s[r]:
                    if delete:
                        return False
                    else:
                        l += 1
                        delete = True
                        continue
                else:
                    l += 1
                    r -= 1

            return True


        l, r = 0, len(s) - 1
        delete  = False
        while l<r:
            if s[l] != s[r]:
                if delete:
                    return try_left()
                else:
                    r -= 1
                    delete = True
                    continue
            else:
                l += 1
                r -= 1

        return True
             

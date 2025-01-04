class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        for i in range(len(secret)):
            bulls += int(secret[i] == guess[i])
        
        cows = 0
        for i in set(secret):
            cows += min(secret.count(i), guess.count(i))
        
        return f"{bulls}A{cows - bulls}B"

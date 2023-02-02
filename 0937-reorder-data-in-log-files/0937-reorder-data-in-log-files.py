class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs = []
        digit_logs = []
        
        for i,log in enumerate(logs):
            detail = log.split()
            identifier,content = detail[0], detail[1:]

            if all([c.isnumeric() for c in content]):
                digit_logs.append(log)
            else:
                letter_logs.append((content,identifier,log))

        return [l[2] for l in sorted(letter_logs)] + digit_logs
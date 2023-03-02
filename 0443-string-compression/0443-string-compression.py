class Solution:
    def compress(self, chars: List[str]) -> int:
        self.chars_i = cnt = 1
        prev_ch = chars[0]
        for i in range(1, len(chars)):
            if prev_ch == chars[i]:
                cnt += 1
            else:
                self._append_cnt(cnt, chars)
                chars[self.chars_i] = chars[i]
                self.chars_i += 1
                cnt = 1
                prev_ch = chars[i]
        
        self._append_cnt(cnt, chars)
        return self.chars_i
              
    def _append_cnt(self, cnt, chars):
        if cnt > 1:
            if cnt < 10:
                chars[self.chars_i] = str(cnt)
                self.chars_i += 1
            else:
                for x in list(str(cnt)):
                    chars[self.chars_i] = str(x)
                    self.chars_i += 1
        return self.chars_i
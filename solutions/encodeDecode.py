import re
class Codec:
    def encode(self, strs: [str]) -> str:
        """Encodes a list of strings to a single string.
        """
        final_strs = []
        for s in strs:
            length = len(s)
            curr_str = "{},{}".format(str(length), s)
            final_strs.append(curr_str)
        
        return ''.join(final_strs)
            
    # "3,abc6,23yxm"
    def decode(self, s: str) -> [str]:
        """Decodes a single string to a list of strings.
        """       
        index = 0
        final_strs = []
        num_regex = re.compile('\d')
        
        while index < len(s):
            start_index = index
            while num_regex.match(s[index]):
                index += 1
            
            str_len = int(s[start_index:index])
            #comma delim
            index += 1
            final_strs.append(s[index:index+str_len])
            index += str_len
            
        return final_strs
    
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))


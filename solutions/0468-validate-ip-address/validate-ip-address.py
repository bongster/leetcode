# Given a string queryIP, return "IPv4" if IP is a valid IPv4 address, "IPv6" if IP is a valid IPv6 address or "Neither" if IP is not a correct IP of any type.
#
# A valid IPv4 address is an IP in the form "x1.x2.x3.x4" where 0 <= xi <= 255 and xi cannot contain leading zeros. For example, "192.168.1.1" and "192.168.1.0" are valid IPv4 addresses but "192.168.01.1", while "192.168.1.00" and "192.168@1.1" are invalid IPv4 addresses.
#
# A valid IPv6 address is an IP in the form "x1:x2:x3:x4:x5:x6:x7:x8" where:
#
#
# 	1 <= xi.length <= 4
# 	xi is a hexadecimal string which may contain digits, lower-case English letter ('a' to 'f') and upper-case English letters ('A' to 'F').
# 	Leading zeros are allowed in xi.
#
#
# For example, "2001:0db8:85a3:0000:0000:8a2e:0370:7334" and "2001:db8:85a3:0:0:8A2E:0370:7334" are valid IPv6 addresses, while "2001:0db8:85a3::8A2E:037j:7334" and "02001:0db8:85a3:0000:0000:8a2e:0370:7334" are invalid IPv6 addresses.
#
#  
# Example 1:
#
#
# Input: queryIP = "172.16.254.1"
# Output: "IPv4"
# Explanation: This is a valid IPv4 address, return "IPv4".
#
#
# Example 2:
#
#
# Input: queryIP = "2001:0db8:85a3:0:0:8A2E:0370:7334"
# Output: "IPv6"
# Explanation: This is a valid IPv6 address, return "IPv6".
#
#
# Example 3:
#
#
# Input: queryIP = "256.256.256.256"
# Output: "Neither"
# Explanation: This is neither a IPv4 address nor a IPv6 address.
#
#
# Example 4:
#
#
# Input: queryIP = "2001:0db8:85a3:0:0:8A2E:0370:7334:"
# Output: "Neither"
#
#
# Example 5:
#
#
# Input: queryIP = "1e1.4.5.6"
# Output: "Neither"
#
#
#  
# Constraints:
#
#
# 	queryIP consists only of English letters, digits and the characters '.' and ':'.
#
#


class Solution:
    def validIPAddress(self, IP: str) -> str:
        is_ip4 = True
        is_ip6 = True

        # checking IP 4
        if "." in IP and len(IP.split(".")) == 4:
            for i in IP.split("."):
                try:
                    x = int(i, 10)
                    print(x, i)
                    if str(x) != i or x > 255 or x < 0:
                    # if x > 0 and (len(i) > 3 or 10 ** (len(i) - 1) > x or x > 255):
                        is_ip4 = False
                        break
                except:
                    is_ip4 = False
                    break
        else:
            is_ip4 = False
            

        # checking ip 6

        if ":" in IP and len(IP.split(":")) == 8:
            for i in IP.split(":"):
                try:
                    if '-' in i:
                        is_ip6 = False
                        break
                    x = int(i, 16)
                    print(i, x)
                    if len(i) > 4 or int(i, 16) > 65535:
                        is_ip6 = False
                        break
                except:
                    is_ip6 = False
                    break
                

        else:
            is_ip6 = False
        print(is_ip4, is_ip6)
        if is_ip4:
            return "IPv4"
        elif is_ip6:
            return "IPv6"
        else:
            return "Neither"
            
        

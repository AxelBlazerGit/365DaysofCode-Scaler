class Solution:
    # @param A : integer
    # @param B : integer
    # @return a string
    def fractionToDecimal(self, A, B):
        if A == 0:
            return "0"
        if B == 0:
            return "undefined"  # or raise an exception
        
        result = []
        
        # Determine the sign of the result
        if (A < 0) ^ (B < 0):
            result.append('-')
        
        # Convert both numbers to positive
        A, B = abs(A), abs(B)
        
        # Add the integral part
        integral = A // B
        result.append(str(integral))
        
        # Calculate the initial remainder
        remainder = A % B
        if remainder == 0:
            return ''.join(result)  # No fractional part
        
        result.append('.')
        
        # To detect repeating remainders
        remainder_map = {}
        
        while remainder != 0:
            # If the remainder is already seen, it's the start of a repeating part
            if remainder in remainder_map:
                result.insert(remainder_map[remainder], '(')
                result.append(')')
                break
            
            # Store the current position of the remainder
            remainder_map[remainder] = len(result)
            
            # Perform long division
            remainder *= 10
            digit = remainder // B
            result.append(str(digit))
            remainder %= B
        
        return ''.join(result)

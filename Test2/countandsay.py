
def stringCompression(s):
   current  = s[0]
   count = 0
   output = ""
   for letter in s :
      if letter == current :
         count += 1
      else:
         output += str(count) + current
         count = 1
         current = letter
   output += str(count) + current
   return output



def writeAsYouSpeak(n):
   n = n-1
   output = "1"
   while n > 0:
      output = stringCompression(output)
      n -= 1
   return  output





print(writeAsYouSpeak(int(input())))






